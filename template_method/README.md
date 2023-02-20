## Template method

The Template Method pattern is a design pattern in object-oriented programming that defines the basic steps of an
algorithm and allows subclasses to provide their own implementation for some or all of these steps.

The Template Method pattern is useful when you have an algorithm or a process that has a fixed sequence of steps, but
you want to allow some flexibility in how those steps are performed. This pattern can help you to reduce code
duplication and improve code reusability by abstracting away common functionality and allowing subclasses to provide
their own implementations.

### when should you use template method

You have a process or algorithm that has a fixed sequence of steps, but you want to allow some flexibility in how those
steps are performed.

You want to avoid code duplication by abstracting away common functionality into a base class.

You want to provide a framework for other developers to build upon by allowing them to customize certain aspects of the
algorithm.

You want to make it easier to modify or extend the algorithm in the future.

### Potential drawbacks and limitations

Overcomplication: Using the Template Method pattern can add additional complexity to your code, especially if you need
to create a large number of subclasses that override different parts of the template method. This can make your code
harder to understand and maintain.

Tight Coupling: The Template Method pattern can also result in tight coupling between the base class and its subclasses.
If the base class is changed, it can impact the behavior of all of its subclasses. This can make it harder to modify and
test your code.

Limited Flexibility: The Template Method pattern provides a fixed algorithm structure that may not be flexible enough to
handle all possible scenarios. If you need more flexibility, you may need to use a different design pattern or approach.

Inefficient for simple algorithms: The Template Method pattern is most useful when you have a complex algorithm with
many steps that can be customized by subclasses. If your algorithm is simple and has only a few steps, using the
Template Method pattern may be overkill and could make your code more complicated than it needs to be.