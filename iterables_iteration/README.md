Python's concept of iteration and iterable objects is fairly simple and adbstract, not involving much more than the idea of a sequence of elements that can be accessed one at a time, in order.  

Some if the ideas on how to work it iterables were originally developed in the functional programming community.  So some people may refer to the use of these techniques as "functional-style" Python.  Whether you think of these as a separate programming paradigm or just as moe tools in the programming arsenal, these functions can be very useful and are often the best way to express certain computations.

## map()

The map() function is probably one of hte most widely recognized functional programming tools in Python.  Given a callable object and a sequence of objects, map() calls the function once for every elemement in the source series, producing a new series containing the return values of the function.  In functional programming jargon, we "map" a function over a sequence to produce a new sequence.

### Multiple input sequences

Generally you need to provide as many input sequences as there are arguments in the mapped function.  When map() is given multiple input secuences it takes an element from each sequence and passes it as the corresponding argument to the mapped function to produce each output value.

## filter()

As its name implies, fitler() looks at each element in an iterable series and skips those which don't meet some criteria.  Like map() filter() applies a callable to each element in a series, and also like map(), filter() produces its results lazily.  Unlike map(), filter() only accepts a single input sequence, and the callable it takes must only accept a single argument.  The filter() function (really class) applies its first argument to each element in the input series, and returns a series containing only those elements of the input for which the function returns True.

## Differences between Python 2 and 3

In Python 3 the map and filter functions return a lazily-produced series of values.  In Python 2, these functions actually return list sequences.

## functools.reduce()

The reduce() function is in the funtools standard library module.  You can iplemnet both map and filter in terms of reduce.  reduce() repeatedly applies a function of two argument to an interim accumulator value and the elements of the series, updating - or accumulating - the interim value at each step with the result of the called function.  Ultimately the final value of the accumulator is returned, thereby reducing the series down to a single value.