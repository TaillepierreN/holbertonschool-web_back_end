# ES6 Classes Overview

This project involves implementing ES6 class features, including constructor methods, getters, setters, and inheritance, along with other modern JavaScript functionalities. The project aims to deepen understanding of ES6 classes and related concepts like metaprogramming and static methods.

## Learning Objectives

- How to define and implement a class in ES6.
- Adding methods to a class and understanding when to use static methods.
- Extending a class from another, including how to call the parent class constructor.
- Utilizing JavaScript metaprogramming techniques such as symbols.

## Requirements

- Code execution on Ubuntu 18.04 LTS using NodeJS 12.11.x.
- Proper coding style enforced by ESLint.
- Code verification through unit testing with Jest.

## Setup

1. **Node.js Installation**: Install Node.js to run the JavaScript code outside a browser environment.
2. **Babel and ESLint Setup**: Use Babel for ES6+ backward compatibility and ESLint for code linting.
3. **Jest Installation**: Setup Jest for testing JavaScript code to ensure correctness.

## Task Descriptions

1. **ClassRoom Class**: Define a class that initializes with a `maxStudentsSize` attribute and includes appropriate getters and setters.
2. **Multiple ClassRooms**: Utilize the `ClassRoom` class to create multiple classroom objects with different sizes.
3. **HolbertonCourse Class**: Create a class with multiple attributes and ensure type-checking for attribute values during object creation.
4. **Currency and Pricing Classes**: Implement classes that deal with currency and pricing objects, involving getters, setters, and static methods.
5. **Building and SkyHighBuilding Classes**: Create an abstract class and extend it, ensuring the child class implements a specific method.
6. **Airport Class**: Define a class where the default string description should return a custom format based on the class properties.
7. **Advanced Classes**: Work with metaprogramming features and symbols to enhance class functionalities, such as creating cloneable object instances.

### Example Usage

```javascript
import ClassRoom from "./0-classroom.js";

const room = new ClassRoom(10);
console.log(room.maxStudentsSize); // Output should be 10
```

This example demonstrates how to create an instance of `ClassRoom` and access its `maxStudentsSize` property using a getter, assuming the class is defined with private variables and appropriate accessors.

### Further Instructions

- Ensure to handle errors or incorrect data types gracefully within class constructors or methods.
- Utilize modern JavaScript syntax and features such as template literals and arrow functions where appropriate.
- Focus on encapsulation and robustness of the class design to ensure that the class internals are protected from invalid external inputs.
