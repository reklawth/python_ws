# sorted_set.py
# UTF-8

from collections import Sequence, Set
from bisect import bisect_left
from itertools import chain

class SortedSet(Sequence, Set):

  #  def __init__(self, items=None):
  #      self._items = sorted(items) if items is not None else []
    def __init__(self, items=None):
        self._items = sorted(set(items)) if items is not None else []
        
    def __contains__(self, item):
        index = bisect_left(self._items, item)
        return (index !=len(self._items)) and self._items[index] == item

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else '')

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))

    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def issubset(self, iterable):
        return self <= SortedSet(iterable)
    
    def issuperset(self, iterable):
        return self >= SortedSet(iterable)

    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedSet(iterable)

    def difference(self, iterable):
        return self - SortedSet(iterable)

    def _is_unique_and_sorted(self):
        return all(self[i] < self[i +1] for i in range(len(self) - 1))

    def index(self, item):
        assert self._is_unique_and_sorted()
        index = bisect_left(self._items, item)
        if (index != len(self._items)) and self._items[index] == item:
            return index
        raise ValueError("{} not found".format(repr(item)))

    def count(self, item):
        assert self._is_unique_and_sorted()
        return int(item in self._items)