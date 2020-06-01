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