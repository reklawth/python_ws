# Printing collections of Objects

When Python prints collections of objects it has to decide which representation to use. Python uses the repr() of an oject when it is preinted as part of a list, dict, or any other built-in type.

# Precise control with format()

The format() method on strings is another place where string representations are called behind the scenes

# Formatting instructions for __format__()

Unlike __str__() and __repr__(), __format__() accepts an argument, f.  This argument contains any special formatting options specified in the caller's format string.  If the caller puts a colon inside the curly braces of a formatting string (example: {:r}), anything after the colon is sent verbatim as the argument to __format__() (example: r).