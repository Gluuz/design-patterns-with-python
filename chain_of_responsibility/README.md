# Responsibility Chain

When we have a list of commands that must be executed in a specific order, the Chain of Responsibility pattern fits like a glove.
specific scenario, and we also know which scenario should be validated next, in case the previous one does not satisfy
the condition. allows us to separate responsibilities into small, lean classes, yet provides a flexible, decoupled way
to put these behaviors back together.

### Chain of responsibility vs. strategy

Chain of Responsibility enables multiple objects to handle a request, whereas Strategy enables a client to choose an object.
algorithm at runtime. Chain of Responsibility is used to avoid tight coupling between objects, whereas Strategy is used to avoid tight coupling between objects.
make a family of related algorithms interchangeable.

### Potential drawbacks and limitations

Increased Complexity: CoR can increase the complexity of the codebase because it involves creating a chain of objects.
that handle requests, which can be difficult to understand and maintain over time.

Performance Overhead: The process of passing a request through a chain of objects can be time-consuming, especially if
The chain is lengthy or complex. This can result in a performance overhead that impacts the overall efficiency of the
system.

Unhandled Requests: If the end of the chain is reached and no object has handled the request, it may be necessary to
have a default behavior to handle the unhandled request. This can lead to code duplication and further complexity.

Debugging can be challenging, especially if the chain of objects is long or complex.
Finding the exact object that caused an issue may require tracing the entire chain, which can be time-consuming and
error-prone.

Order Dependency: The order of objects in the chain is important because it determines which object will handle the
request. This can create dependencies between objects, which can make it difficult to modify or extend the chain.
time.