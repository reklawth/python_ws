## The _iterable_ protocol

Provide the special `__iter__()` method which must return an iterator over the series of items.  One of the following tests in the `TestIterableProtocol` class will call the `iter()` built-in and one which uses a for-loop:

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
```
```py
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

if __name__ == '__main__':
    unittest.main()
```

The `test_iter()` method obtains an iterator using the `iter()` built-in.  The method asserts that each value is the expected one, and that the iterator terminates the series normally by raising a `StopIteration` exception.

The `assertRaises()` method of `TestCase` returns a context manager, so it can be used in conjunction with a `with` statement.  The code inside the `with`-block is expected to raise the specified exception. 

Both tests fail because iteration has not yet been implemented:

```
$ python test_sorted_set.py
```
The simple implementation of `__iter__()` will delegate to the underlying list:

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
```
```py
def __iter__(self):
    return iter(self._items)
```
Most implementations of __iter__() will either delegate in this way to some underlying collection, or be implemented as a generator function.  Generator functions return generator objects, which are by definition iterators.  This means that generator functions fulfill the requirements of `__iter__()`.  If a generator function was used in this case, __iter__() _could_ look like this:
```py
def __iter__(self):
    for item in self._items:
        yield item
```
or with consideration for _PEP 380 - Syntax for Delegating to a Subgenerator_, the loop can be eliminated by using the `yield from` syntax for delegating to an iterable:
```py
def __iter__(self):
    yield from self._items
```
The first of these two suggested forms (the one using the list iterator), may be faster and perhaps less obtuse.