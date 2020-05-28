## Test First

In test_sorted_set.py, the goal is to ensure that we can successfully construct a SortedSet instance in a way that is typical for python collections  There is no particular protocol implemented here, however it is sensible to ensure that the collections can be constructed from existing iterable sequenses of various configurations, including being empty.  We do not want to rely onthe argument assed ot the constructor being anything more sophisticated than an iterable, and using a geretor function to produce a generator object is a good way to test for that.

```py
# test_sorted_set.py

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

if __name__ == '__main__':
    unittest.main()
```

Attempting to run the above fails with an inability to import SortedSet.  The tests in the exercise the initializer, checking that it can be called with these arguments without causing an exception to be raised.

## The initializer

To implement enough of SortedSet in sorted_set.py to pass the basic preceding tests:

```python
# sorted_set.py
# UTF-8

class SortedSet:

    def __init__(self, items=None):
        self._items = sorted(items)
```

The above list was created using the sorted() built-in function which always returns a list irrespective of which type of iterable object it is passed.  Now run the test by directly running the test module:

```
$ python test_sorted_set.py
```