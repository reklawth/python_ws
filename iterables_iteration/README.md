Python's concept of iteration and iterable objects is fairly simple and adbstract, not involving much more than the idea of a sequence of elements that can be accessed one at a time, in order.  

Some if the ideas on how to work it iterables were originally developed in the functional programming community.  So some people may refer to the use of these techniques as "functional-style" Python.  Whether you think of these as a separate programming paradigm or just as moe tools in the programming arsenal, these functions can be very useful and are often the best way to express certain computations.

## map()

The map() function is probably one of hte most widely recognized functional programming tools in Python.  Given a callable object and a sequence of objects, map() calls the function once for every elemement in the source series, producing a new series containing the return values of the function.  In functional programming jargon, we "map" a function over a sequence to produce a new sequence.

### Multiple input sequences

Generally you need to provide as many input sequences as there are arguments in the mapped function.  When map() is given multiple input secuences it takes an element from each sequence and passes it as the corresponding argument to the mapped function to produce each output value.