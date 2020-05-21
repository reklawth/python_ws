# Two String Representations

Python supports two primary ways of making string representations of objects, the built-in functions repr() and str().  Each of these can take any object as an argument and produce a string representation of some form.

These two functions rely on the special methods `__repr__()` and `__str__()` of the object passd to them to generate the strings they produce.
