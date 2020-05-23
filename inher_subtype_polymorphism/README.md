## Inheritance and Subtype Polymorphism 

Developers of languages like C++ and Java may expect Python to also call the initializer from Base when creating a Sub instance, however this is not how Python behaves. Rather, Python treats the `__init__()` method like any other method and it does not automatically call base-class initializer for subclasses that define initializers. If there is a need to define an initializer in a subclass and still call the initializer of a base-class then call it explicitly using the super() function.


## issubclass()

There is another built-in fuction related to isinstance() which bcan be used for type checking.  issubclass(), operates on types only, rather than operating on instances of types.  issubclass() is used to determine if one class is a subclass of another.  issubclass() takes two arguments, both of which need to be type objects, and it will return True if the first argument is a direct or indirect subclass of the second.

## Multiple inheritance

Multiple inheritance simply means defining classes with more than one direct base-class.  This feature is not universal among OO languages.  C++ suports multiple inheritance while Java does not.  Multiple inheritance can lead to certain complex situations - for example, deciding what to do when more than one base class defines a particular method.  The syntax for defining a class with multiple inheritance is similar to single inheritance, simply use a comma separated list of classes in the parentheses after the class name:

```
class Subclass(Base1, Base2, Base3):
     # ...
```

## MRO: Method Resolution Order

The MRO of a class is the ordering of a class's inheritance graphu used to determine which implementation to use when a method is invoked.  When you invoke a method on an object which has one or more base-classes, the actual code that gets run may be defined on:
  - the class itself
  - one of its direct base-classes
  - a base-class of a base-class
  - any other member of the class's inheritance graph

The MRO of a class determines the order in which the inheritance graph is searcehed to fine the correct implementation of this method.  When you call a method on an object in Python it looks at the MRO for that object's type.  For each entry in the MRO, starting at the front and working in order to the back, Python checks if that class has the requested method.  Once Python finds a class with a matching method it uses that method and the search stops.

### How is MRO calculated?

Python uses an algorithm known as C3 linearization for determining MRO.  A few of the important qualities of the MRO that it produces are:

1. A C3 MRO ensures that subclasses come before their base-classes
2. C3 ensures that the base-class order as defined in a class definition is also preserved.
3. C3 preserves the first two qualities independent of where in an inheritance graph you calculate the MRO.  The MROs for all classes in a graph agree with respec to relative class order.

### Inconsistent MROs

One outcome of the C3 algorithm is that not all inheritance declarations are allowed in Python.  Some base-class declarations will violate C3 and Python will refuse to compile them.

# super()

Given a method resolution order and a class C in that MRO, super() gives you an object which resolves methods usng only the part of the MRO which comes after C.

In other words, super() does not work iwth the base-classes of a class, but instead it works with the MRO of the type of the ovject on which a method was originally invoked.

super() can be called in several forms.  All of them return a so-called super proxy object.  You can call any method on a super proxy, and it will route that call to the correct method implementation if one exists.

There are two high-level types of super proxies, bound and unbound.  Bound proxies are bound to instances or class objects.  Unbound proxies are not connect to any instance.  Unbound proxies ar primarily an implementation detail for other Python features.  They seem to be considered insignificant.

## class-bound proxies

To create a class-bound proxy use this form:

`super(base-class, derived-class)`

Here, both arguments are class objects.  The second class must be a subclass of (or the same class as) the first argument.

When you invode a method on the proxy here is what happens:
1. Python finds the MRO for derived-class
2. It then finds base-class in that MRO
3. It takes everything after base-class in the MRO and finds the first class in that sequence with a method name matching the request.