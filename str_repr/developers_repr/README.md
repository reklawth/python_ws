# Strings for developers with repr()

repr() is an abbreviation for representation.  The repr() function is intended to make an unambigious representation of an object, within reason.  In this context unambiguous means that it should include the type of the object along with any identifiying fields.

repr() is important for situations where exactness is more important than brevity or readibility.  repr() is well suited for debugging because it tells you all of the important details of an object.  if an object's repr() tells you its type and important details, you can spend less time inspecting objects and more time debugging logic.