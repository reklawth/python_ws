# @classmethod

This decorator exists so you can create class methods that are passed to the actual class object within the function call, much like self is passed to any other ordinary instance method in a class.

In those instance methods, the self argument is the class instance object itself, which can then be used to act on instance data. @classmethod methods also have a mandatory first argument, but this argument isn't a class instance, it's actually the uninstantiated class itself.

Notice in the _get_next_serial(cls) function that we are passing a class (cls) as a parameter

If you need to refer to the class object within the method (for example to access a class attribute) prefer to use @classmethod.  If you don't need to access the class object use @staticmethod

# super() Function

At a high level, super() gives you access to methods in a superclass from the subclass that inherits from it.

super() alone returns a temporary object of the superclass that then allows you to call that superclass’s methods.

Why would you want to do any of this? While the possibilities are limited by your imagination, a common use case is building classes that extend the functionality of previously built classes.

Calling the previously built methods with super() saves you from needing to rewrite those methods in your subclass, and allows you to swap out superclasses with minimal code changes. 