## Inheritance and Subtype Polymorphism 

Developers of languages like C++ and Java may expect Python to also call the initializer from Base when creating a Sub instance, however this is not how Python behaves. Rather, Python treats the init() method like any other method and it does not automatically call base-class initializer for subclasses that define initializers. If there is a need to define an initializer in a subclass and still call the initializer of a base-class then call it explicitly using the super() function.
