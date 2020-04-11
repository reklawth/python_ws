# @classmethod

This decorator exists so you can create class methods that are passed to the actual class object within the function call, much like self is passed to any other ordinary instance method in a class.

In those instance methods, the self argument is the class instance object itself, which can then be used to act on instance data. @classmethod methods also have a mandatory first argument, but this argument isn't a class instance, it's actually the uninstantiated class itself.

Notice in the _get_next_serial(cls) function that we are passing a class (cls) as a parameter

If you need to refer to the class object within the method (for example to access a class attribute) prefer to use @classmethod.  If you don't need to access the class object use @staticmethod