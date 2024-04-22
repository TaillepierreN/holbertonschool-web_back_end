# Python - Async Comprehension

Welcome to the "Python - Async Comprehension" project! This project will help you get acquainted with asynchronous programming concepts like async generators and async comprehensions in Python. By the end of this project, you should be able to build efficient asynchronous code that can handle multiple operations simultaneously.

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives

By the end of this project, you should be able to:
- Write and understand asynchronous generators.
- Use async comprehensions effectively.
- Type-annotate generators to enhance code readability and maintainability.

## Requirements

### General

- **Environment**: All code will be tested on Ubuntu 18.04 LTS using Python 3.7.
- **Style**: Code must adhere to the Pycodestyle (PEP 8) guidelines.
- **Documentation**:
  - Every module must have a docstring.
  - Every function and coroutine must include a docstring that explains its purpose.
- **Execution**: All files must be executable.
- **Typing**: All functions and coroutines must be type-annotated.

### Tasks

1. **Async Generator**:
   - Write a coroutine named `async_generator` that asynchronously yields a random number between 0 and 10 after waiting for 1 second. This coroutine should iterate 10 times.

2. **Async Comprehensions**:
   - Use the `async_generator` you created in the previous task to write another coroutine, `async_comprehension`, that collects these random numbers using an async comprehension.

3. **Parallel Async Comprehensions**:
   - Measure the runtime of executing the `async_comprehension` coroutine four times concurrently. Observe and understand why the runtime behaves as it does.
