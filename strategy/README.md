# Pattern of Strategy

The strategy pattern is very useful when we have a set of similar algorithms and we need to switch between them in
different parts of the application.

Strategy allows us to write many algorithms in a flexible manner and then pass those algorithms to client classes.
need them. These clients are unaware of the "real" algorithm being executed and just tell the algorithm to run. This
causes the code of the client class to be quite decoupled from the implementations of the algorithms, thus enabling this
client to be able to work with N different algorithms without having to change its code.

### Potential drawbacks and limitations

Increased Complexity: Implementing the strategy pattern can increase the complexity of the codebase by requiring the
creation of multiple classes to represent each strategy, which can be difficult to understand and maintain over time.

Overhead: The use of the strategy pattern can introduce additional overhead in the system, especially if the
The decision-making process for selecting a particular strategy is complex or resource-intensive.

Object Creation: Each strategy typically requires its own class, which can increase the number of objects created in the
system, potentially leading to performance issues or memory overhead.

Runtime Overhead: The process of selecting a strategy at runtime can introduce additional overhead, which may be
problematic in real-time or high-performance systems.

Inflexibility: The strategy pattern can be inflexible if the strategies are defined at compile time and cannot be
changed at runtime. This can limit the adaptability of the system to changing conditions or requirements.

Potential Over-Abstraction: Overuse of the Strategy pattern can lead to over-abstraction, where the code becomes more
complex than necessary and may be difficult to understand or maintain.