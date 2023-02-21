# Decorator Pattern

Whenever we resist, we have behaviors that can be formed by behaviors from other classes involved in the same authority,
as was the case with taxes, which can be composed of other taxes. The Decorator introduces flexibility in the
composition of these behaviors, simply choosing at the time of instantiation which instances will be used to perform the
work.

### when should you use decorator

In the Decorator Pattern, the decorator objects have the same interface as the original object they are decorating,
which allows them to be used interchangeably. Each decorator object adds new functionality to the object it is wrapping,
and the result is a layered or composite object that provides the original functionality as well as the additional
features provided by the decorators.

The Decorator Pattern is often used when you want to add functionality to an object without modifying its existing code,
or when you want to add new behavior to individual objects, but not to the entire class. It is also useful when you have
a large number of subclasses, and you want to avoid creating a new subclass for every possible combination of behaviors.

Overall, the Decorator Pattern provides a flexible and extensible way to add new behavior to an object at runtime,
without modifying its underlying structure. It promotes a design that is open for extension but closed for modification,
which makes it easier to maintain and update over time.

### Potential drawbacks and limitations

Increased complexity: Because the Decorator Pattern involves wrapping objects in layers of decorators, it can add
complexity to your code. This can make it harder to understand and maintain, particularly if you have a large number of
decorators.

Performance overhead: The Decorator Pattern can introduce a performance overhead, particularly if you have a large
number of decorators. Each decorator adds an additional layer of processing, which can slow down the execution of your
code.

Inflexibility in some cases: The Decorator Pattern works best when you want to add functionality to an object without
modifying its underlying structure. However, in some cases, you may need to modify the structure of an object, which the
Decorator Pattern does not allow.

Design complexity: The Decorator Pattern can sometimes result in a complex design, particularly if you have a large
number of decorators. This can make it harder to understand the relationships between objects in your code.

Potential for confusion: Because the Decorator Pattern can involve multiple layers of objects and decorators, it can be
easy to lose track of what each object is doing and which decorator is responsible for which behavior.