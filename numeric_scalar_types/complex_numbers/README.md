# Complex Numbers

Complex numbers are built into the Python language and don't need to be imported from a module.  Each complex number has a real part and an imaginary part, and Python provides a special literal syntax to produce te imaginary part: planing a j suffix onto a number, where j represents the imaginary square-root of -1.  Python uses the convention adopted by the electrical engineering community for denoting complex numbers - where complex numbers have important uses, rather than the convention used by the mathematics community.

## The cmath module

The functions of the math module cannot be used with complex numbers, so a module cmath is provided containing versions of the functions which both accept and return complex numbers.

## Polar coordinates

In addition to complex equivalents of all the standard math functions, cmath contains functions for convrting between the standard cartesian form and polar coordinates.

### Cartesian form:

A Cartesian coordinate system (US: /kɑːrˈtiʒən/) is a coordinate system that specifies each point uniquely in a plane by a set of numerical coordinates, which are the signed distances to the point from two fixed perpendicular oriented lines, measured in the same unit of length.  https://en.wikipedia.org/wiki/Cartesian_coordinate_system

## abs()

abs() returns the magnitude of a number, which is always positive.  When used with integers, floats, decimals or fractions, it simply returns the absolute alue of the number, which is the non-negative magnitude without regards to its sign.  In effect, for all number tupes including complex, abs() returns the distance from zero.

## round()

round() will rounds to a given number of decimal digits.  To avoid bias, when there are two equally close alternatives rounding is towards even numbers.  So round(1.5) rounds up, and round(2.5) rounds down.

as with abs(), round() is implemented for int (where it has no effect), float, and Decimal.  It is also implemented for Fraction.  round() is not supported for complex.  Be aware that when used with float, which uses a binary representation, round() - which is fundamentally a decimal operation - can give surprising results.  If avoiding quirks is import for your application, use the decimal type.

## datetime module

The types in the datetime module should be the first resort when you need to represent time related quantities.  The types are:

date - a Gregorian calendar date

time - the time within an ideal day which ignores leap seconds

datetime - a composite of date and tme

tzinfo (abstract) and timezone (concrete) - classes that are used for representing time zone information required for 'aware' time objects.

timedelta - a duration expressing the difference between two date or datetime instances.

all objects of these types are immutable - once created their values cannot be modified.