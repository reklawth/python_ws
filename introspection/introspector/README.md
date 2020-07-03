# Object Introspection tool

Create a function, which when passed a single object, prints out a nicely formatted dump of that objects attributes and methods, similar to `getmembers()` but with more finesse.

Create a module `introspector.py` and define a `dump()` method that prints the outline of the object dump:
```py
# introspector.py

def dump(obj):
     print("Type")
    print("====")
    print(type(obj))
    print()
```
Four section headings are printed and the only object detail printed is the type retrieved using the `type()` built-in function.

## Introspecting documentation

The easiest thing to do for the documentation section would be to simply print the `obj.__doc__` attribute, which would be a good start.  A better thing would be to use a function from the `inspect` module called `cleandoc()` which deals with tricky topics like uniformly removing leading whitespace from docstrings.  Even better, there is a function called `getdoc()` in the inspect module that will combine the operatons of retrieving and tidying up the docstring.  That will be used instead, providing very straightforward code in the documentation section:
```py
def dump(obj):
# ...
    print("Documentation")
    print("=============")
    print(inspect.getdoc(obj))
    print()
```

## Attributes and methods

There is now a need to product a list of attributes and their values.  The _right_ course of action is to use `inspect.getmembers()`, however this example will code up its own routine to apply other previously learned techniques.

Getting a list of attributes can be done using the `dir(obj)`.  Put the attribute names into one of the SortedSet collections defined earlier:
```py
all_attr_names = SortedSet(dir(obj))
```

Now produce another `SortedSet` of all _method_ names by determining which of those attributes, when retrieved with `getattr()`, is _callable_.  Use `filter()` to select those attributes which are callable, and the predicate which acts on the attribute _name_ will be a lambda function:
```py
method_names = SortedSet(
    filter(lambda attr_name: callable(getattr(obj, attr_name)),
    all_attr_names))
```

The next part of the program will assume that `method_names` is a subset of `all_attr_names`, check that that is the case at this juncture by using an `assert` statement.  Recall that the relational operators on a `SortedSet` can be used to implement the subset test efficiently between two objects of the same type:
```py
assert method_names <= all_attr_names
```
Now use a set difference operation, called through the infix subtraction operator, to produce a `SortedSet` of all regular attributes - that is, those which are not callable - by subtracting the `method_names` from `all_attr_names`:
```py
attr_names = all_attr_names - method_names
```
Now print the attributes and their values.  Do this by building a list of name-value pairs using a list comprehension.  An attribute value could potentially have a huge text representation, which would spoil output without adding much value.  Use the Python Standard Library `reprlib` module to cut the values down to a reasonable size in an intelligent way:
```py
attr_names_and_values = [(name, reprlib.repr(getattr(obj, name))) for name in attr_names]
```
Then print a table of names and values, using a putative `print_table()` function to be implemented later:
```py
print_table(attr_names_and_values, "Name", "Value")
```
The function will need to accept a sequence of sequences representing rows of columns along with the requisite number of column headers as strings.

With the regular attributes dealt with move onto methods. From the list of `method_names` generate a series of method objects, simply by retrieving each one with getattr():
```py
methods = (getattr(obj, method_name) for method_name in method_names)
```
The for each method object, build a full method signature and a brief documentation string, using functions to be defined later.  The signature and documentation will be assembled into a list of tuples using this list comprehension:
```py
method_names_and_doc = [(full_sig(method), brief_doc(method)) for method in methods]
```
Finally, print the table of methods using the yet-to-be implemented `print_table()` function:
```py
print_table(method_names_and_doc, "Name", "Description")
```

## `full_sig()`

The `dump()` function is complete, now implement `full_sig()` one of three functions on which `dump()` depends:
```py
# introspector.py
# ...
def full_sig(method):
    try:
        return method.__name__ + inspect.signature(method)
    except ValueError:
        return method.__name__ + '(...)'
```
In the above function, retrieve the name of the method via the special `__name__` attribute, and then try to get the argument signatures using `inspect.signature()`.  If that fails, fall back in the exception handler to return a string indicating that the signature could not be determined. This is an example of _Easier to Ask Forgiveness than Permission_ programming style.

## `brief_doc()`

Now move onto implementing `brief_doc()`.  Documentation strings can be very lengthy, and in the table only a brief description is desired.  Fortunately, there is a widely followed convention tht the first line of a docstring contains exactly such a brief description.  This function attempt sto extract that line and return it:
```py
# introspector.py
# ...
def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            return lines[0]
    return ''
```
Account for the fact that the docstring attribute may be set to `None`, in which case `splitlines()` cannot be called on it.  Likewise the docstring may be defined but empty, in which case `splitlines()` would return an empty list.  In either of these eventualities an empty string is returned.  This function follows a _Look Before You Leap_ style of programming, because the result was clearer than the alternative.

## `print_table()`

Recall that the `print_table()` function accepts a sequence of sequence as its first argument, with the outer sequence representing rows of the table and the innner sequences representing the columns within those rows.  In addition the function accepts as many string arguments as are necessary to provide column headings. 

Use extended argument syntax to accept any number of header arguments.  Next, perform some basic validation by ensuring that the number of header values supplied is compatible with the first row of the table.  Follow the lead of the built-in functions and raise a `TypeError` if too few arguments are provided:
```py
# introspector.py
# . . .
def print_table(rows_of_columns, *headers):

    num_columns = len(rows_of_columns[0])
    num_headers = len(headers)
    if len(headers) != num_columns:
        raise TypeError("Expected {} header arguments, got {}".format(num_columns, num_headers))
```
Note that the long `raise` statement can be split over several lines.  Now determine the width of each column in the table, taking into account the width of each item in the `rows_of_columns` data structure, but also the header widths.  To do this, lazily concatenate the header row and the data rows into a value `rows_of_columns_with_header` using `itertools.chain()`:
```py
rows_of_columns_with_header = itertools.chain([headers], rows_of_columns)
```
Notice how a list containing the single headers row is made for the first argument.  Next use the zip-star idiom to transpose the rows-of-columns into columns-of-rows.  Force evaluation of the otherwise lazy `zip()` by constructing a `list`, binding the result to the name `columns_of_rows`:
```py
columns_of_rows = list(zip(*rows_of_columns_with_header))
```
To find the maximum width of a column use this expression:
```py
max(map(len, column))
```
To break this down. pass the `len` function, without calling it, to `map()`, which applies `len()` to each item in the `column` sequence, in effect yielding a series of widths.  Then use `max()` to fid the maximum widto of the column.  Apply this approach to each column, so put this expression in a list comprehension which does exactly that:
```py
column_widths = [max(map(len, column)) for column in columns_of_rows]
```
Note that `map()` and list comprehensions are often considered to be alternatives.  In the above, both have been comboined because the result is more readable than using nested comprehensions or using two applications of `map()`.  The resulting `column_widths` object is a list containing one integer for each column.

To print fixed width columns, do that with format specifiers and the format() string method.  However there is a variable number of columns so there is a need to build up the format string programmatically.  Each column will need to have a format specifier like this "{:13}" (for a column width of thirteen).

To do this use the `format()` function to insert the width, but there is a need to escape the outer curly-braces so they carry through to the result;  this escaping is performed by doubling the curly brace character.  Applying this over all columns using a generator exprerssion produces:
```py
column_specs = ('{{:{w}}}'.format(w=width) for width in column_widths)
```
Concatenate all these column format specifications together using the `str.join()` method, inserting a space between each column:
```py
format_spec = ' '.join(column_specs)
```
Now to begin printing the table. First, use the `format_spec` to print the column headers, using extended argument unpacking to supply each header string as a separate argument to `format()`:
```py
print(format_spec.format(*headers))
```
Now print horizontal rules under the headers to separate them from the data below. Use string repetition with the multiply operator to create the individual rules by repeating hyphens, then generate a rule for each column using a generator expression:
```py
rules = (' ' * width for width in column_widths)
```
Then it is a simple matter to print the rules:
```py
print(format_spec.format(*rules))
```
Finally, print each row of data:
```py
for row in rows_of_columns:
    print(format_spec.format(*row))
```