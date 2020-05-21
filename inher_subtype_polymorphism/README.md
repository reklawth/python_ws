## Inheritance and Subtype Polymorphism 

Developers of languages like C++ and Java may expect Python to also call the initializer from Base when creating a Sub instance, however this is not how Python behaves. Rather, Python treats the init() method like any other method and it does not automatically call base-class initializer for subclasses that define initializers. If there is a need to define an initializer in a subclass and still call the initializer of a base-class then call it explicitly using the super() function.


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

The MRO of a class determines the order in which the inheritance graph is searcehed to fine the correct implementation of this method.  When you call a method on an object in Python it looks at the MRO for that object's type.  For each entry in the MRO, starting at the front and working in order to the back, Python checks if that class has the requested method.  Once Pythong finds a class with a matching method it uses that method and the search stops.