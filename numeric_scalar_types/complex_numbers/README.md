# Complex Numbers

Complex numbers are built into the Python language and don't need to be imported from a module.  Each complex number has a real part and an imaginary part, and Python provides a special literal syntax to produce te imaginary part: planing a j suffix onto a number, where j represents the imaginary square-root of -1.  Python uses the convention adopted by the electrical engineering community for denoting complex numbers - where complex numbers have important uses, rather than the convention used by the mathematics community.

## The cmath module

The functions of the math module cannot be used with complex numbers, so a module cmath is provided containing versions of the functions which both accept and return complex numbers.

## Polar coordinates

In addition to complex equivalents of all the standard math functions, cmath contains functions for convrting between the standard cartesian form and polar coordinates.

### Cartesian form:

A Cartesian coordinate system (US: /kɑːrˈtiʒən/) is a coordinate system that specifies each point uniquely in a plane by a set of numerical coordinates, which are the signed distances to the point from two fixed perpendicular oriented lines, measured in the same unit of length.  https://en.wikipedia.org/wiki/Cartesian_coordinate_system