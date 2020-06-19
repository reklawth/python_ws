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