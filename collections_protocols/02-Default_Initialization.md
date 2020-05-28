## Default Initialization

There should also be the ability to construct an empty `SortedSset` with no arguments.  Though that is not mandted by any of the collection protocols, it would make the collection consistent with teh existing Python collections, which will eliminate a potential surprise to users of the class:

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

    def test_default_empty(self):
        s = SortedSet()

if __name__ == '__main__':
    unittest.main()
```
This fails at runtime because the existing initializer implementation expects exactly one argument:
```
$ python test_sorted_set.py
```
Updating the implementation of `__init__()` will fix this:

```py
# sorted_set.py
# UTF-8

class SortedSet:

    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []
```

`None` is deliberately used as the default argument rather than an empty `list`, to avoid inadvertently mutating the default argument object which is only created once when the method is first defined.