# Defining Context Managers

Context managers are those objects designed to be used as the argument to a _with-statement_.  
* A `with-statement` is a statement of the form `with EXPR as NAME:`
* A `with-block` is a `with-statement` plus an associated code block.

The distinction between a `with-statement` and a `with-block` is important because the `with-statement` is where Python directly interaces with context managers, while the entire `with-block` defines the lifetime of the context manager.

## What is a context manager?

A context manager is an object that is designed to be used in a `with-statement`.  A `with-statement` has the following syntax:
`with EXPR [as NAME]:`

When a `with-statement` is executed, the EXPR part of the statement - that is, the expression following the `with` keyword - evaluates to a value.  This value must be a context manager, and the underlying mechanics of the `with-statement` use this value in specific ways to implement the semantics of the `with-statement`.

Conceptually a context manager implements two methods which are used by the `with-statement`.  The first method is called before the code-blcok of the `with-statement` begins, and hte second method is called after execution of the code in the `with-block` finishes, whether by running to completion, returning early from the enclosing function, or by the rasiing of an exception which is allowed to propogate out of the with-block.

A context manager represents code that runs before and after the code-block of the `with-statement`.  These operations can be thought of as set-up and tear-down, construction and destruction, resource allocation and deallocation or any number of other ways.

## Files as context managers

Python developers will have used files in a with-statement like this:
```py
with open('important_data.txt', 'wt') as f:
    f.write('The secret password is 12345')
```
The benefit of using files in a with-statement is that htey are automatically closed at the end of the with-block.  This workds because file objects are context managers.  That is, files have methods which are called by the with-statement before the block is entered, and after the block exits.  The _exit_ method for a file (the code executed after the with-block exits) does the work of closing the file, and this is how files work with with-statements to ensure proper resource management.

## The context manager protocol

For an object to be a context-manager, it needs to support the _context-manager protocol_ which consists of two methods, `__enter__()` and `__exit__()`.

## `__enter__()`

The `__enter__()` method is called on the context-manager just before entering the with-block, and its return value is bound to the as-variable of the with-statement.

`__enter__()` is allowed to return anything it wants, including `None`, and the with-statement itself does not ever access or use this value.  It is very common, however, for context-managers to simply return themselves from `__enter__()`. 

## `__exit__()`

The `__exit__()` method is substantially moe complex that `__enter__()` because it poerforms several roles in the execution of a with-statement.  Its first and primary role is that it is executed after the with-block terminates, so it is responsible for cleaning up whatever resources the context-manager controls.

Its second role is to properly handle the case where the with-block exits with an exception.  To handle this caxe, `__exit__()` accepts three arguments:
* The type of the exception that was raised
* The value of the exception  (that is, the actual exception instance)
* The traceback associated with the exception

When a with-block exits without an exception, all three of these arguments are set to `None`, but when it exits exceptionally these arguments are bound to the exception which terminated the block.

In many cases a context-manager needs to perform different `__exit__()` code depending on whether an exception was raised or not, so it is typical for `__exit__()` to first check the exception information before doing anything else.  A common idiom is to check the type arguement to detect an exceptional exit.