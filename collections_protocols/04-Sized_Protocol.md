## The _sized_ protocol

The _sized_ protocol determines how many items are in a collection.  The built-in `len()` function delegates to this protocol and must always return a non-negative integer.  Tests for this are in the `TestSizedProtocol` class

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
```
```py
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

if __name__ == '__main__':
    unittest.main()
```
The preceding tests three cases - zero, one, and 10.  The fourth test ensures that duplicate items passed to the constructor are only counted once.  Running this form will produce four failures:

```
$ python test_sorted_set.py
```
To get the tests passing there is a need to implement the special `__len__()` method to which the len() built-in delegates:
```py
# sorted_set.py
# UTF-8

class SortedSet:

    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []

    def __contains__(self, item):
        return item in self._items
```
```py
   def __len__(self):
       return len(self._items)
```
The fourth _sized_ protocol tests still fails, as this counts covers initializer behaviour rather than conformance to the _sized_ protocol.  To fix i duplicate items in the series passed tot he constructor must be eliminated.  The easiest way to do that is to construct a regual set with these items.  That can be used to construct the sorted list.

```py
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []
```
This has the added advantage that the `set()` constructor is a good model for what the constructor should support.  By delegating to it directly, it is ensured that the `SortedSet` constructor is compatible with the `set()` constructor.  Now all tests should pass.