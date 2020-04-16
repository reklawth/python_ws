# Object Oriented Design
Consider that overuse of getters and setters can lead to poor object-oriented designs with tightly coupled classes.  Such designs expose to many details, albeit thinly wrapped in properties.  A recommendation is to reduce coupling between objects by implementing methods which allow clients to tell objects what to do, rather than having clients request internal data so they can themselves perform actions.

# So what can super() do for you in single inheritance?

Like in other object-oriented languages, it allows you to call methods of the superclass in your subclass. The primary use case of this is to extend the functionality of the inherited method.
