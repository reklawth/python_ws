# The _sequence_ protocol

The sequence protocol requires that - in additon to being an _iterable_, _sized_, and _container_ - the collection supports element access with square brackets, slicing with square brackets and production of a reverse iterator when passed to the `reversed()` built-in function.  The collection should also implement `index()` and `count()` and if it needs to support the informally defined _extended sequence_ it should support concatenation and repitition through the addition and multiplication infix operators.

Both indexing and slicing using postfix square brackets are supported by the `__getitem__()` special method.  The `__getitem__()` will provide for regular forward indexing and reverse indexing with negative integers.  The `TestSequenceProtocol` class includes tests for the various edge cases:

```py
# test_sorted_set.py
# UTF-8

import unittest

from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):
    
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([7, 8, 3, 1])

    def test_with_duplicates(self):
        s = SortedSet([8, 8, 8])

    def test_from_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2
        g = gen6842()
        s = SortedSet(g)

    def test_default_empty(self):
        s = SortedSet()
        
class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(2 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(9 not in self.s)

class TestSizedProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([42])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_with_duplicates(self):
        s = SortedSet([5, 5, 5])
        self.assertEqual(len(s), 1)

class TestIterableProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([7, 2, 1, 1, 9])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        with self.assertRaises(StopIteration):
            next(i)

    def test_for_loop(self):
        index = 0
        expected = [1, 2, 7, 9]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1
```
```py
class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_the_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

if __name__ == '__main__':
    unittest.main()
```
These 6 new tests will fail:
```
$ python test_sorted_set.py
```
For the tests to pass the special `__getitem__()` method needs to be implemented:
```py
# sorted_set.py
# UTF-8

class SortedSet:

    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []

    def __iter__(self):
        return iter(self._items)
```
```py
    def __getitem__(self, index):
       return self._items[index]
```
The tests will pass here.  Now add tests for slicing to the `TestSequenceProtocol` class:
```py
class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_the_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]
```
```py
    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1, 4, 9]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedSet([13, 15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedSet([9, 13]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)

if __name__ == '__main__':
    unittest.main()
```
These 5 additional tests fail because the implementation which delegates to `list` returns list slices.  To remedy this there needs to be a slightly more sophisticated version of `__getitem__()` which detects whether it is being called with an index or a slice and acts accordingly.  

To see what the index argument of the __getitem__() method will contain when called with the slice syntax, temporarily print the index value and the type of the index value:
```py
    def __getitem__(self, index):
        print(index)
        print(type(index))
        return self._items[index]
```
The dominate purpose of the above is to detect when a `slice` object has been passed to `__getitem__()`.  With a new `SortedSet`, the list returned from delegating to the `list slice` can now be wrapped:
```py
    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result
```
The above tests will now fail, and we will need to implement the `__repr__()` special method.

## repr()

Create the `TestReprProtocol` class in `test_sorted_set.py`
```py
class TestReprProtocol(unittest.TestCase):

    def test_repr_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr)one(self):
        s = SortedSet([42, 40, 19])
        self.assertEqual(repr(s), "SortedSet([19, 40, 42])")
```

Including the above code block increases the number of failed tests from five to seven.  Implementing `__repr__()` in the 'SortedSet` class will reduce failed tests back down to five:
```py
class SortedSet:
    
    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else '')
```
Follow the lead of the built-in collections and render an argumentless constructor call into the string if the collection is empty.  If there are aitems in the collection delegate to the list repr() to render the argument.  Notice the implicit conversion of the self._items list to the bool in the conditional; if the collection is empty this expression evalutates to `False` in this boolean context.

The above code will allow the repr() tests to pass, it will also give more verbose output on issues with the remaining tests.  From the output it seems that there is an equality issue occurring.

## equality

Python equality comparisions - which are inherited from the ultimate base class object - are for reference equality rather than value equality or equivalence.  For more information see `sequence_protocol_equality.ipynb`.  To get the desired behaviour for the `SortedSet` class, more tests will be created using the `list` equality to override the default equality implementation:
```py
class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(SortedSet([4, 5, 6]) == SortedSet([6, 5, 4]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([4, 5, 6]) == SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([4, 5, 6])) == [4, 5, 6])

    def test_identical(self):
        s = SortedSet([10, 11, 12])
        self.assertTrue(s == s)
```
In the above `assertTrue()` and `assertFalse()` are used rather than `assertEqual()` and `assertNotEqual()`.  This leaves the equality operator in plain sight and it ensures that the tests are couched in terms of the equality opertor only, not the inequality operator.

Now implement a specialized equality for SortedSet by overrideing the __eq__() special method.  The implmentation just delegates to the same operator with the enclosed lists of the left-hand-side operand (in this case self) and right-hand-side operand (abbreviated as rhs):
```py
class SortedSet:
    # ...
    def __eq__(self, rhs):
        return self._items == rhs._items
```
Now the `type-mismatch` test fails.  The implementation will need to be refined to include a type check.  Follow the Python convention of returning the special built-in singleton value `NotImplemented` if the types do not match:
```py
class SortedSet:

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self.items == rhs._items 
```
Notice the `NotImplemented` object is _returned_ rather than _raising_ a `NotImplementedError`.  In the Python language this is a curiousity, and the runtime will use it to retry the comparison once with the arguments reversed, potentially giving a different implementation of `__eq__()` on another object a chance to respond.  Read more at https://docs.python.org/3/reference/datamodel.html?highlight=eq#object.eq

## inequality

Add inequality tests in the `TestInequalityProtocol` class:
```py
class TestInequalityProtocol(unittest.TestCase):

    def test_positive_unequal(self):
        self.assertTrue(SortedSet([4, 5, 6]) != SortedSet(1, 2, 3]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([4, 5, 6]) != SortedSet([6, 5, 4]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])

    def test_identical(self):
        s = SortedSet([10, 11, 12])
        self.assertFalse(s != s)
```
The above tests require no additional changes to the implementation (`sorted_set.py`), demonstrating that Python will implement inequality by negating the equality operator.  However it is also possible to override the `__ne__()` special method if inequality needs its own implementation.

At the point the collection is an _iterable_, _sized_, _container_ which implements `__getitem__()` from the _sequence_ protocol.  It is lacking support for reverse iterators as well as `index()` and `count()`.  The `reversed()` built-in function should return an iterator which yields the collection items in reverse order.  Below, additional tests are appended to the `TestSequenceProtocol` class:
```py
class TestSequenceProtocol(unittest.TestCase):
    # ...
    def test_reversed(self):
        s = SortedSet([1, 3, 5, 7])
        r = reversed(s)
        self.assertEqual(next(r), 7)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 1)
        with self.assertRaises(StopIteration):
            next(r)
```
The above tests pass with no alternation to `sorted_set.py` needed.  By default, the implmeentation of `reversed()` will check for the presence of the `__reversed__()` special method and delegate to that.  However if `__reversed__()` has not been implemented but both `__getitem__()` and `__len__()` are supported, `reversed()` will produce an iterator that internally walkes back trhoug the sequence by decrementing an index.  

Next, create tests for `index()` and `count()` First the `index()` method, which should return the index of the first matching item in the collection or raise a `ValueError`:
```py
class TestSequenceProtocol(unittest.TestCase):
    # ...
    def test_index_positive(self):
        s = SortedSet([1, 5, 8, 9])
        self.assertEqual(s.index(8), 2)
    
    def test_index_negative(self):
        s = SortedSet([1, 5, 8, 9])
        with self.assertRaises(ValueError):
            s.index(15)
```
Both of the above test fail because `index()` has not been implemented, because it is a regular method there are no opportunities for fallback mechanisms in the Python implmeentation to kick it.  It is possible to implement index() in terms of methods that we have already in place, such as `__getitem__()`.

Such default implementations are available in the Python Standard Library in the base classes of the `collections.abc` module.  This module contains many classes which can be inherited by - or _mixed in_ to - classes, reducing some of the work in collection protocol implementation.

The following example uses the collections.abc.Sequence class, which by providing implementation of `__getitem__` and `__len__` will provide a whole raft of mixin methods, including `index()`.  `SortedSet` is made a subclass of `Sequence` in the example below:
```py
# sorted_set.py
# UTF-8

from collections import Sequence

class SortedSet(Sequence):

    # ...
```
Now the `index()` unit tests pass.

Next ensure that `count()` is also correctly implemented.  Recall that `count()` returns the number of times a specified item occurs in a list.  Below are appended tests in the `TestSequenceProtocol` class:
```py
class TestSequenceProtocol(unittest.TestCase):

    # ...
    def test_count_zero(self):
        s = SortedSet([1, 5, 7, 9])
        self.assertEqual(s.count(11), 0)

    def test_count_one(self):
        s = SortedSet([1, 5, 7, 9])
        self.assertEqual(s.count(7), 1)
```
Because of the inheritance of the `Sequence` abstract base class, the above tests work immediately.

## Improving `count()` implementation

Knowing that the `count()` operation on a `SortedSet` only ever returns a zero or one,  and knowing that the list inside of the set is always sorted, it should be possilbe to perform a bindary search for the element in a time proportional to _log^n_ rather than _n_ (where _n_ is the number of elements in the set, and _log^n_ will always be much smaller than _n_).

A binary search implmentation is available in the Python standard library in the bisect module.  Now override the `count()` implementation:

```py
# sorted_set.py
# UTF-8

from bisect import bisect_left

class SortedSet(Sequence):

    def count(self, item):
        index = bisect_left(self._items, item)
        found = (index != len(self._items)) and (self._items[index] == item)
        return int(found)
```

This method works by using the bisect_left() function to determine at which index `item` would need to be inserted into `self._items` in order to maintain sorted order.  Then check that `index` is within the bounds of the list and whether the element at that index is equivalent to the item being sought.  Assign this boolean value to the variable found.  Finally, convert the `bool` to an `int` which results in zero and ove for `False` and `True` respectively.

## Refactoring common code

The `found` variable in the new implementation of `count()` represents exactly the same result as would be obtained from the `__contains__()` method that was written for the implementation of the _container_ protocol.  Refactor by extracting the efficient search implementation into `__contains__()` and use the membership test withing `count()`.  The `__contains__()` method is now edited to:
```py
# sorted_set.py
# UTF-8

# ...
class SortedSet(Sequence):

# ...
    def __contains__(self, item):

        index = bisect_left(self._item)
        return (index !=len(self._items)) and self._items[index] == item
```
The `count()` method is now reduced to:
```py
def count(self, item):
    return int(item in self._items)
```

## Improving the implementation of index()

The `index()` implementation inherited from Sequence is not very efficient.  It performs a relatively inefficient linear search.  That can be fixed using the `bisect` module.  Becasue the tests are already in place, proceed with directly overriding the method:
```py
# sorted_set.py
# UTF-8

# ...
class SortedSet(Sequence):
    # ...
    def index(self, item):
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError("{} not found".format(repr(item)))
```
As there seems to be repition between `index()` and what is already in `__contains__()`, there is an option to implemet `__contains__()` in terms of `index()` like this:
```py
class SortedSet(Sequence):
    # ...
    def __contains__(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False
```
## Still need to use `collections.abc.Sequence`?

Add tests to cover inheritance from the `Container`, `Sized`, `Iterable`, and `Sequence` ABCs:
```py
# test_sorted_set.py
# UTF-8
from collections.abc import Container, Iterable, Sequence, Sized
# ...
class TestContainerProtocol(unittest.TestCase):
    # ...
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))

class TestSizedProtocol(unittest.TestCase):
    # ...
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))

class TestIterableProtocol(unittest.TestCase):
    # ...
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))

class TestSequenceProtocol(unittest.TestCase):
    # ...
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))
```
Originially, only the last of the above four tests fail.  As the SortedSet class is still a subclass of Sequence, even teh last class will pass.  A powerful feature of the `issubclass()` function allows it to take advantage of the duck-typing without explicit inheritance in relation to the Abstract Base Class system.

## Implementing concatenation and repition

Concatenation and repition of sequences can be performed with the add and multiply operators.  Neither of these two operators are enforced or supplied by the `Sequence` abstract base class, because they are part of the informally described _extended sequence protocol_, to which many Python sequence types such as `list` and `str` conform, but to which others, such as `range` do not.

Implement concatenation as a set-union operator which results in a set containing all elements from both operands.  Append additonal tests.
```py
# test_sorted_set.py
# UTF-8

class TestSequenceProtocol(unittest.TestCase):
    # ...

    def test_concatenate_disjoint(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([4, 5, 6])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 4, 5, 6]))

    def test_concatenate_equal(self):
        s = SortedSet([2, 4, 6])
        self.assertEqual(s + s, s)

    def test_concatenate_intersecting(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([3, 4, 5])
        self.assertEqual(s + t, SortedSet([1, 2, 3, 4, 5]))
```
To get these tests to pass, implement support for the infix plus operator, which is done via the special method `__add__()`:
```py
# sorted_set.py
# UTF-8

from itertools import chain

class SortedSet(Sequence):
    # ...
    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))
```
Rather than simply concatenating the enclosed list of the two operands, which could result in a large temporary intermediate list object use `itertools.chain()`.  This requires and additional import at the top of the module.  `chain` streams all values from one operand and then the other into the `SortedSet` constructor.  The tests should execute as expected.