# UTF-8
from intlist import IntList
from SortedList import SortedList

class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))