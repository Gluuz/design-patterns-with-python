# Strategy pattern

The Strategy pattern is very useful when we have a set of similar algorithms, and we need to switch between them in
different parts of the application.

Strategy gives us a flexible way to write many algorithms, and to pass those algorithms to client classes that
need them. These clients are unaware of the "real" algorithm being executed, and just tell the algorithm to run. This
causes the code of the client class to be quite decoupled from the implementations of the algorithms, thus enabling this
client to be able to work with N different algorithms without having to change its code.