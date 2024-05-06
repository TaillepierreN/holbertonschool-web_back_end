# ES6 Basics Overview

This project introduces the basic concepts of ECMAScript 2015 (ES6), which is a significant update to JavaScript that includes numerous new features and enhancements. These new features make JavaScript more powerful and expressive, and easier to work with.

## Learning Objectives

- Understand the enhancements and new features introduced in ES6.
- Familiarize with new syntax and capabilities such as constants, block-scoped variables, arrow functions, default parameters, template literals, and more.
- Learn about iterators and for-of loops, which enhance JavaScript's ability to handle and iterate over data.
- Explore the use of new methods and properties in object handling.

## Requirements

- All code must be executed on Ubuntu 18.04 using NodeJS 12.11.x.
- Use ESLint to enforce Airbnb's JavaScript style guide.
- Make use of Babel to ensure backward compatibility.
- Ensure all functions are exported for modular use and testing.

## Setup

You're expected to set up your project environment to support modern JavaScript (ES6) features:

1. **Node.js**: Install Node.js to run JavaScript server-side.
2. **Babel**: Use Babel to transpile ES6 code to backward-compatible versions of JavaScript.
3. **ESLint**: Utilize ESLint for code quality and style compliance.
4. **Jest**: Implement Jest for testing JavaScript code.

## Configuration

Create configuration files for `package.json`, `babel.config.js`, and `.eslintrc.js` to set up your environment properly. This includes defining scripts for linting, development, and testing.

## Tasks Overview

1. **Const or let?**: Modify variables to use `const` or `let` for better scope management and to avoid issues related to hoisting.
2. **Block Scope**: Ensure variables inside a function are block-scoped using `let` to avoid unexpected global scope pollution.
3. **Arrow functions**: Convert standard functions to arrow functions to make the code cleaner and to handle `this` more predictably.
4. **Parameter defaults**: Simplify function parameters by setting default values.
5. **Rest parameter syntax**: Use the rest parameter syntax to handle function parameters more flexibly.
6. **Spread syntax**: Use spread syntax for merging arrays or objects succinctly.
7. **Template literals**: Utilize template literals for easier string interpolation.
8. **Object property shorthand**: Use ES6 shorthand syntax to clean up object initialization.
9. **Computed property names**: Use computed property names to dynamically create properties on objects.
10. **Method properties**: Define object methods using shorthand syntax introduced in ES6.

## Practical Example

Implement a function that uses template literals to format a message, demonstrating the straightforward and expressive nature of ES6:

```javascript
function greeting(name) {
  return `Hello, ${name}!`;
}
```

This function, which might seem trivial, represents the simplicity and power of ES6 in enhancing JavaScript readability and expressiveness.
