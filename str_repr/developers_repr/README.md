# Strings for developers with repr()

repr() is an abbreviation for representation.  The repr() function is intended to make an unambigious representation of an object, within reason.  In this context unambiguous means that it should include the type of the object along with any identifiying fields.

repr() is important for situations where exactness is more important than brevity or readibility.  repr() is well suited for debugging because it tells you all of the important details of an object.  if an object's repr() tells you its type and important details, you can spend less time inspecting objects and more time debugging logic.

repr() should contain more information than the str() representation of an object, so repr() is best suited for situations where explicit information is needed.

The repr() of an object should tell a developer everything they need to know about an object to fully identify it and, as much as is practical, see where it come from and how it fits into the larger program context.  The repr() of an object is what a developer will see in a debugger, so when deciding what to put into a repr(), think about what you'd want to know when debugging code that uses the class you are developing.

## Always implement a repr() for your classes

All objects come with a defual implementation of __repr__(), but you'll almost always want to overide this.  The default representation tells you the class name and the ID of the object, but it tells you nothing about the important attributes.

It is a good idea to always implement __repr__() for any class that you write.  It does not take much work to write a good repr(), ahd the work pays of whe you are debugging or scanning logs.