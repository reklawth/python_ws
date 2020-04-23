# Strings for clients with str()

str() is intended to provide readable, human-friendly output.  It does not need to be as precise as repr()

The str() representation is used in sutations where, it might be integrated into normal text or where the programming-level details such as "class" might be meaningless.  Relcall that the str() function is acutally the constructor for the str type.

## When is str() used?

### print() uses str()

An obvious place to look is the print() function.  print(), since it is generally deisnged to provide console output to users, uses the human-friendly str() representation.

### str() defaults to repr()

The default implementation of str() simply calls repr().  Meaning that if you do not define __str__() for a class then that class will use __repr__() when str() is requested.

### .format()
.str.format() uses an object's __format__() method when inserting it into string templates

The default implemntation of __format__() is to call __str__()

The argument to the __format__() method contains any special formatting instructions frmo the format string