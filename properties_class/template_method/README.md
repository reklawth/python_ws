# Template Method Pattern

The template meethod is a design pattern where we implement skeletal operations in base classes, deffering some details to subclasses.  This is achieved by calling methods in the base class which are either not defined at all or which have a trivial implementation.  Such methods must be overridden in subclasses in order to be useful.  