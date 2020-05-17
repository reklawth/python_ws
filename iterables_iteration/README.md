Python's concept of iteration and iterable objects is fairly simple and adbstract, not involving much more than the idea of a sequence of elements that can be accessed one at a time, in order.  

Some if the ideas on how to work it iterables were originally developed in the functional programming community.  So some people may refer to the use of these techniques as "functional-style" Python.  Whether you think of these as a separate programming paradigm or just as moe tools in the programming arsenal, these functions can be very useful and are often the best way to express certain computations.

## Comprehension

Comprehensions can process more than on input series

Multiple input series in comprehensions work like nested for-loops

Comprehensions can also have multiple if-clouses intersperse with the for-clauses

Later clauses in comprehension can reference variables bound in earlier clauses

Comprehension can also appear in the result expression of a comprehension, resulting in a nested result series.

## map()

The map() function is probably one of hte most widely recognized functional programming tools in Python.  Given a callable object and a sequence of objects, map() calls the function once for every elemement in the source series, producing a new series containing the return values of the function.  In functional programming jargon, we "map" a function over a sequence to produce a new sequence.

### Multiple input sequences

Generally you need to provide as many input sequences as there are arguments in the mapped function.  When map() is given multiple input secuences it takes an element from each sequence and passes it as the corresponding argument to the mapped function to produce each output value.

## filter()

As its name implies, fitler() looks at each element in an iterable series and skips those which don't meet some criteria.  Like map() filter() applies a callable to each element in a series, and also like map(), filter() produces its results lazily.  Unlike map(), filter() only accepts a single input sequence, and the callable it takes must only accept a single argument.  The filter() function (really class) applies its first argument to each element in the input series, and returns a series containing only those elements of the input for which the function returns True.

## Differences between Python 2 and 3

In Python 3 the map and filter functions return a lazily-produced series of values.  In Python 2, these functions actually return list sequences.

## functools.reduce()

reduce() is a generalization of summation.  The reduce() function is in the funtools standard library module.  You can iplemnet both map and filter in terms of reduce.  reduce() repeatedly applies a function of two argument to an interim accumulator value and the elements of the series, updating - or accumulating - the interim value at each step with the result of the called function.  Ultimately the final value of the accumulator is returned, thereby reducing the series down to a single value.

## Iterables

An iterable object in Python is simply an object that supports the iterable protocol by implementing __iter__(). When you call iter(obj), this ultimately results in a call to obj.__iter__(), and iter() returns the result of this call .__iter__() is required to return an iterator

## Iterators

An iterator is simply an object that fulfills the iterator protocol.  he first part of the iterator protocol is the iterable protocol.  In other words, all iterators must also be iterable.  This means that all iterators must implement __iter__().  Often (but not always), iterators just return themselves from __iter__() . 

Iterators are also required to implement __next__(), the function called by next().  Like iter() and __iter__(), next (obj) results in a call to obj.__next__(), the result of which gets returned by next().

## __getitem__()

Rather than implementing the __iter__ method, an object can implement the __getitem__ method.  For this to work, __getitem__ must return values for consecutive integer indices starting at 0. When the index argument is out of the iterables range of data, then __getitem__ must raise IndexError.

## Extended iter() form

Normally iter() is called on objects that support the __iter__ method of the iterable protocol.  However, iter() supports a two-argument form that lets you iterate over some objects which do not directly support the iterable protocol.

In this exte ded form, the ifrst argumet is a callable which takes zero arguments.  The second argument is a sentinel value.  The return value from iter() in this case is an iterator which produces values by repeatedly calling the callable argument.  This iterator terminates when the value produced by the callable is equal to the sentinel.