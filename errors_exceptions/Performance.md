# Performance

The precondition assertions performed to test the sorted set assumptions are relatively expensive. In the case that the class is working as expected, each tet walks through the whole collection. Worse from a performance standpoint is that sometimes the test is performed more than once. There is the option to run Python programs with all assertions disabled, using the -O flag on the command line:

```
python3 -m timeit -n 1 -s "from random import randrange; from sorted_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000))" "[s.count(i) for i in range(1000)]"
```
```
python3 -O -m timeit -n 1 -s "from random import randrange; from sorted_set import SortedSet; s = SortedSet(randrange(1000) for _ in range(2000))" "[s.count(i) for i in range(1000)]"
```
Notice that the result with -O is in milliseconds, so it is rought 1000 times faster than the version where assertions are enabled.  Use this option only if performance concerns demand it.  Running with assertions enabled in production can be a fabulous way of flushing out problmens in code.  The majority of Python code that is run will have assertions _enabled_ for this reason.

## Avoiding side effects

Because `assert` statments can be removed from a program with a simple command line flag, it is crucial that hte presence or absense of assertions does not affect the correctness of the program.  For this reason avoid assertion conditions which have side effects.  For example, refrain from:
```py
assert my_list.pop(item)
```