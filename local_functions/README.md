# Chapter 3 Summary

What is covered:
- Local functions:
    - def is executed at runtime
    - def definces functions in the scope in which it is called, and this can be inside of other functions
    - Functions defined inside other functions are commonly called local functions
    - A new local function is created each time the containing function is executed.
    - Local functions are no different from other local name bindings and can be treated like any other object
    - Local functions can access names in other scopes via the LEGB rule
    - The enclosing scope for a local function includes the parameters of its enclosing function
    - Local functions can be usefule for code organization
    - Local functions are similar to lambdas, but are more general and powerful
    - Functions can return other fucntions, including local function defined in their body

# Decorators

https://realpython.com/primer-on-python-decorators/