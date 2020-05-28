## The _container_ protocol

The container protocol is the most fundamental of the collection protocols and allows for the determination of whether a particular item is present in the collection.  The container protocol is what underpins the `in` and `not in` infix operators.  The following example appends the TestContainerProtocol class to test_sorted_set.py:

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
```
```py
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

if __name__ == '__main__':
    unittest.main()
```
In the preceding, the `setUp()` method is used tot create a SortedSet test fixture.  Next, four test methods are used to assert the four combinations of membership and non-membership, success and failure.

```
$ python test_sorted_set.py
```

Running the tests results in four failures.  The error messages not that making SortedSet iterable could fix problem rather than making it support the _container_ protocol.  For this example to get the test passing the more restrictive _container_ protocol will be implemented.  This is implemented by the special `__contains__()` method, which accepts a single argument which is the item for which to test for, and returns a boolean.  Internally the `__contains__()` implementation will just delegate to the membership test on the enclosed `list` object:

```py
# sorted_set.py
# UTF-8

class SortedSet:

    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []
```
```py
    def __contains__(self, item):
        return item in self._items
```

Now the tests will pass again:

```
$ python test_sorted_set.py
```

Do not be tempted to have `SortedSet.__contains__(self, item)` delegate directly to `self._items.__contains__(item)`:

```py
# sorted_set.py
# UTF-8

class SortedSet:
    # ...
    def __contains__(self, item):
        return self._items__contains__(item) # Do not do this!
```
The preceding will work, however it is not recommended to invoke special methods directly, as this can bypass various optimizations and standard behavors implemented in the global functions or operators which delegate to them.