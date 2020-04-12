# Static Method

This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.

# @staticmethod decorator

This decorator will transform a method into a static method

Like all decorators, it is also possible to call staticmethod as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:

class C:
    builtin_open = staticmethod(open)

# Static Methods with Inheritance

Static methods in Python can be overriden in subclasses