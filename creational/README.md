# Creational Patterns

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/focus.png)

How objects are created

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/problem.png)

Objects creation are a potential place for several bugs and unecessary complexity. Imagine that your system has a class that holds instances of several other objects, including their associated instantiation process. This behaviour leads to a situation where the system becomes tightly coupled, making it extremelly hard to change or update a class implementation.

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/solution.png)

Decouple the client from the actual initialization process is what this group of patterns tries to achieve. The creational design patterns abstract the instantiation process, dealing with object creation, creating them in a manner that is suitable to the situation.

The main goal from creational patterns is to help making systems independent of how its objects are created.
This is achieved following to basic principles : 
- encapsulating knowledge about which concrete classes the system uses
- hiding how instances of these concrete classes are created and combined

This is a really important pattern group as systems are evolving to depend more on object composition than class inheritance.

The two main approaches: one focused on classes, where the pattern uses inheritance to vary the class that's instantiated. The second one is focus the objects, delegating the instantiation to another object.

### Patterns
- Abstract Factory
- Builder
- Factory Method
- Prototype
- Singleton


### References
- Design Patterns: Elements of Reusable Object-Oriented Software (https://www.amazon.com/Design-Patterns-Object-Oriented-Addison-Wesley-Professional-ebook/dp/B000SEIBB8)
- https://refactoring.guru/design-patterns/creational-patterns
- https://en.wikipedia.org/wiki/Creational_pattern
- https://sourcemaking.com/design_patterns/creational_patterns
