# Python - Async

Welcome to the "Python - Async" project! This project is designed to introduce you to asynchronous programming in Python using the `asyncio` library. By the end of this project, you'll be proficient in writing asynchronous code that can perform multiple tasks concurrently.

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives

After completing this project, you should be able to:
- Explain and use the `async` and `await` syntax in Python.
- Execute an async program with `asyncio`.
- Run concurrent coroutines.
- Create `asyncio` tasks.
- Utilize the `random` module for generating random delays.

## Requirements

### General

- **Environment**: All files are tested on Ubuntu 18.04 LTS using Python 3.7.
- **Style**: Code must adhere to the Pycodestyle (PEP 8) style version 2.5.x.
- **Documentation**:
  - All modules must include a docstring.
  - All functions and coroutines must have a docstring.
- **Execution**: Files must be executable (`chmod +x <filename>`).
- **Typing**: All functions and coroutines must be type-annotated.

### Tasks

0. **The basics of async**: Write an asynchronous coroutine that waits for a random delay and returns that delay.
1. **Execute multiple coroutines**: Create a coroutine that spawns multiple `wait_random` coroutines and returns a list of the delays in ascending order.
2. **Measure the runtime**: Write a function to measure the execution time of `wait_n` and compute the average time per delay.
3. **Tasks**: Convert a coroutine into a task using `asyncio`.
4. **More tasks**: Modify the `wait_n` function to use tasks.
