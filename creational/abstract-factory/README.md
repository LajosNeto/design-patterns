![alt text](https://res.cloudinary.com/lajosneto/image/upload/v1593301817/patterns-101/creational/abstract-factory.png)


![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/focus.png)

_**"Provide an interface for creating families of related or dependent objects without specifying their concrete classes"**_ - GoF

The abstract factory pattern, aka "Kit", has the main goal of ecapsulating individual factories that have a common behaviour, thus not being necessary the understanding of their concrete implementations from the client using them. It is almost like a _factory that produces other factories_ with the same behaviour.

<br>

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/problem.png)

Consider the following example : we are building a game and our character, Hephaestus, is a forger master, a really famous blacksmith, being able to build a wide range of different equipments such as armors, shields, swords, spears and bows.  
Living at our game world's capital, he has clients from several tribes and each one of those tribes has their own **variant from each of the base equipments**, with different attributes, for example : sword from tribe A has 15 of attack damage while sword from tribe B has a value of 20 of the same attribute.

It would a big problem for us, as the game developers, to hard-code each of those variants and instantiate them differently across our code would make our life really harder once it is necessary to change the behaviour from any of those equipments.  
Our "client" code shoud not see the equipments objects as "SwordTribeA" or "ShieldTribeC", they should only be a "sword" or a "shield" regardless the tribe variant they belong to.

<br>

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/solution.png)

Our forge problem van be solved once we define an abstract ForgeFactory class that declares an interface for creating each basic kinf od equipment.  
We also have one abstract class for each base equipment (armor, shield, sword, spear and bow), followed by concrete subclasses that implement the real behaviour from each one of our base equipments for each tribe variant.  
ForgeFactory has a method that returns a new object for each base equipment abstract class. Our final client code will call those methods for retrieving the instance of each equipment.

Ok, but how will our client have access to the tribe variants from each equipment? Well, this behaviour can be achieved because we will also have a concrete subclass implementing the ForgeFactory for each tribe variant group. And this concrete forge subclass will also implements the operations to create each of of the base equipments following their own behaviour described by the tribe's preferences.

The keypoint from the abstract factory pattern is that users create factories for each tribe solely through the ForgeFactory interface and have no knowledge of the classes that implement the concrete logic for each equipment variant. This aspect makes the usage of this whole structure easir because the user commits to only one interface, defined by an abstract class. 

**The user does not need the details of how a TribeAForge works, it is important to know how a Forge works, regardless the variant it belongs to.**

<br>

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593300689/patterns-101/prosandcons.png)

### Pros
- The concrete code/classes are completely isolated from the user during the instantiation process, once a factory encapsulates the responsability and the process of creating objects
- Objects instances are manipulated through their abstract interfaces, isolating the user from the necessity of understanding the details of the concrete implementation, avoiding __tight coupling__.
- Classes names do not appear in client code : a user treats a shield as a shield, not as a TribeAShield, once all shields variants follow the same interface.
- Naming refactor is easier : as an equipment variant class name only appears at its related factory, we dot not need to update its name across the client code, we only update the factory in charge of its creation.
- When the desired behaviour is to maintain the consistency across all ibjects (belonging to the same variant), the abstract factory makes it easier.
- Single Responsibility Principle - all object creation code is concentrated in one place
- Open/Closed Principle - it is easier to add new product variants without breaking existing client code

### Cons
- Adding new kinds of equipments or removing existing ones for example, is not easy. Adding/removing an equipment makes it necessary to update factories interfaces and all concrete subclasses that implement them.

<br>

![alt text](https://res.cloudinary.com/lajosneto/image/upload/c_scale,w_686/v1593361293/patterns-101/example.png)


<br>
