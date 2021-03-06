# Strings for developers with repr()

repr() is an abbreviation for representation.  The repr() function is intended to make an unambigious representation of an object, within reason.  In this context unambiguous means that it should include the type of the object along with any identifiying fields.

repr() is important for situations where exactness is more important than brevity or readibility.  repr() is well suited for debugging because it tells you all of the important details of an object.  if an object's repr() tells you its type and important details, you can spend less time inspecting objects and more time debugging logic.

repr() should contain more information than the str() representation of an object, so repr() is best suited for situations where explicit information is needed.

The repr() of an object should tell a developer everything they need to know about an object to fully identify it and, as much as is practical, see where it come from and how it fits into the larger program context.  The repr() of an object is what a developer will see in a debugger, so when deciding what to put into a repr(), think about what you'd want to know when debugging code that uses the class you are developing.

The repr of an object is inteded to be used by developers for logging, debugging and other activities where an unambiguous format is more important than a human-friendly one.  Often this means that the repr of an object is larger than the str, if only because the repr contain extra identifying information.

## Always implement a repr() for your classes

All objects come with a defual implementation of `__repr__()`, but you'll almost always want to overide this.  The default representation tells you the class name and the ID of the object, but it tells you nothing about the important attributes.

It is a good idea to always implement `__repr__()` for any class that you write.  It does not take much work to write a good repr(), ahd the work pays of whe you are debugging or scanning logs.

# Leveraging reprlib for large strings

The reprlib module provides an alternative implementation of the built-in repr function.

The primary feature of the implmentation of reprlib is that it places limits on how large a string can be. For example if it is used to print a large list it will only print a limited number of the elements.

## reprlib.Repr

While reprlib.repr() is the main entry point into reprlib for most people, there is significantly more ot the module.  The functionality of reprlib is built around a class, reprlib.Repr.  This class implements all of the support for customizing representations, Repr is designed to be customized and subclassed so you can create your won specialized Repr generators if you want to.

The reprlib module instantiates a singleton instance of this Repr class for you.  It is named reprlib.aRepr and reprlib.repr() actually just calls the reprlib.aRepr.repr() function.  So you can manipulate this pre-made instance if you want to control default reprlib behaviour throughout your program.
