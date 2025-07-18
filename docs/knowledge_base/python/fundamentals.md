# Python Fundamentals

## Introduction
---

[Python](https://www.python.org/doc/essays/blurb/) is a dynamically typed and interpreted language that supports multiple programming paradigms such as:

- **Procedural programming**: a programming paradigm that involves breaking down a program into small, reusable parts called procedures or functions. Used in tasks that involve repetitive operations. However, this programming paradigm lacks features like **data hiding** and **modularity**, and treats data and functions as separate entities.
  
  ---
- **Object-oriented programming (OOP)**: a programming paradigm that organizes code around **objects** (instances of classes). Objects represent real-world entities and each object has its own **state** (data - stored as **attributes/properties**) and **behavior** (methods/functions). Emphasizes **modularity**, **reusability**, and **encapsulation**. OOP has four pillars including:
    - **Inheritance**: a new class (**subclass**) can inherit the properties and methods on an existing class (**superclass**). Helps with **reducing duplication** and **enhancing code reusability** through creating hierarchical relationships between classes.
    - **Encapsulation**: Imagine a capsule (class), where you bundle the attributes (data) and methods into it, all while restricting access to an object's internal state (with controlled access using methods). Helps to create **modular and secure code** thus promoting data integrity.
    - **Polymorphism**: Treat the objects of different classes as objects of a common superclass. This way, you can call methods that perform differently based on the objects they are invoked on. Helps with **extensibility and flexibility** of code.
    - **Abstraction**: Hiding implementation details and exposing only the essential functionalities of a given object. Helps create a clear and high-level view of an object's behavior.
  
  ---
- **Functional programming**: Declarative programming paradigm where you create programs using functions purely. Functions are treated as first-class citizens (meaning you can **pass them as arguments**, **return them from other functions**, and **bind them to names** including local identifiers). Functional programming allows you to write software in a declarative and composable style.
  
---
Python is an ideal language for scripting and [Rapid Application Development](https://www.geeksforgeeks.org/software-engineering/software-engineering-rapid-application-development-model-rad/). You can also use Python as an extension language for any customizable apps. You can easily [extend the Python interpreter](https://docs.python.org/3/extending/index.html#extending-index) with new functions and data types. That is, those that are implemented in C, C++, or even other languages callable from C.

Python is a high-level language with high-level data types built in, such as:

- Dictionaries
- Flexible arrays

These high-level data types gives you more leeway to express complex code as a single statement.

Additionally, Python comes with a large collection of standard modules that provide functionalities like:

- System calls
- File I/O
- Interfaces to graphical interface toolkits i.e., Tk

While building on top of a standard module, you can also split your programs into modules for further reuse with different Python programs.

## Key Language Features

Here are some notable language features to keep in mind:

- **Python is interpreted:** no compilation or linking (Python handles dependencies and module imports dynamically) is necessary.
- **Python is indented:** you don't need opening or closing brackets like in JavaScript
- **Python is extensible and usable for system-level programming:** you can [link a C/ C++ program](https://docs.python.org/3/extending/extending.html) and use Python as a command language or extension. This means that you end up using Python for high-level logic and C for performance-critical parts of your program.

## Python Data Types

Below is a high-level overview of Python data types with examples:
![Python Data Types](assets/python-data-types.jpg)
Source: [PYnative](https://pynative.com/python-data-types/)





## References

1. [What is Python? Executive Summary](https://www.python.org/doc/essays/blurb/)
2. [Rapid Application Development Model (RAD) - Software Engineering](https://www.geeksforgeeks.org/software-engineering/software-engineering-rapid-application-development-model-rad/)
3. [Extending Python with C or C++](https://docs.python.org/3/extending/extending.html)
4. [PYnative](https://pynative.com/python-data-types/)