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

By default, when an exception is raised from a with-block, the `__exit__()` method of the context-manager is executed and afterward the originial exception is re-raised.

## `contextlib.contextmanager`

The `contextlib` package is part of the Python standard library.  It provides utilities for common tasks involving the `with` statement.  Focusing on th `contextmanager` decorator, it is a docorator that can be used to create new context managers.  The concept behind `contextmanager` is simple.  Define a generator function - that is, a function which uses `yield` instead of `return` - and decorate it with the `contextmanager` decorator to create a context-manager factory.  This factory is a callable object which returns context-managers, making it suitable for use in a with-statement.

Code example:
```py
@contextlib.contextmanager
def my_context_manager():
    # <ENTER>
    try:
        yield [value]
        # <NORMAL EXIT>
    except:
        # <EXCEPTIONAL EXIT>
        raise
```
Notice in the above, that the `contextmanager` decorator is applied to a generator called my_context_manager.  now use my_context_manager just like any other context-manager:

```py
with my_context_manager() as x:
    # . . .
```
To describe the function: 
First the genreator function is executed up to its yield statement.  Everything before the yield is equivalent to the `__enter__()` method on a normal contextmanger.  Next the yield statment supplies the value which will be bound to any name given in the as-clause of the with-statement.  In other words, the yield is like the return vlaue from `__enter__()` in a normal context-manager definition.

Once `yield` is called, control leaves the context-manager function and goes to the with-block.  If the with-block terminates normally, then execution flow returns to the context-manager function immediiately after the `yield` statment.  In the above code, this is the secont marked `# <NORMAL EXIT>`.  If the with-block raises an exception, then that exception is re-raised from the `yield` statment in the context-manager.  In the above code block, this means that execution would go to the except block and into the section labeled `# <EXCEPTIONAL EXIT>`.

In other words, the `contextmanger` decorator allows for the definition of context-managers control flow in a single generator function via the `yield` statement rather than breaking it up across two methods.  Since generators remember their state between calls to `yield`, there is no need to define a new class to create a stateful context-manager.

## Multiple context-managers in a with-statement

Use as many contexts-managers are needed in a single with-statement.  The syntax for this is like this:
```py
with cm1() as a, cm2() as b, . . .:
  BODY
```
Each context-manager and optional variable binding is separated by a comma.  From an execution point of view, this is exactly equivalent to using nested with-statements, with earlier context-managers "enclosing" later ones.

So this is multi-context-manager form:
```py
with cm1() as a, cm2() as b:
  BODY
```

It is the same as this nested form:
```py
with cm1() as a:
    with cm2() as b:
        BODY
```

## Do not pass a collection

When using multiple context-managers with a single with-statment do not try to use a tuple or some other sequence of context-managers.