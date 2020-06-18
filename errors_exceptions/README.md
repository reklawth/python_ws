## Exceptions
* Avoid handling all exceptions, especially so called system-exit excepions such as `KeyboardInterrupt`
* Understand standard built-in exception heirarchy
* Catching base class exceptions can be used to catch multiple related exception types
* Almost never need to catch the `BaseException` or `Exception` types since they have subclasses which are almost always programming errors such as `IndentationError`.
* Investigate exceptions payloads, and how to use them effectively
* Inherit from `Exception` to create user-defined exception classes
* At its most basic an `Exception` subclass need only contain a `pass` statement.
* Implement rich attributes on custom exceptions.
* Exception chaining:
  - _Implicitly_ chained exceptions, which set the `__context__` attribute on successor exception objects.
  - _Explicitly_ chained exceptions, which set the `__cause__` attribute on successor exception objects.

## `traceback` module

https://realpython.com/python-traceback/
* Extract traceback objects from the `__traceback__` attribute of exceptions
* Render tracebacks to strings rather than keeping references to them, to avoid space-leak problems with large object graphs reachable from the traceback instance.
* Understand key features of the standard `traceback` module.
* Understand how and _when_ to use assertions