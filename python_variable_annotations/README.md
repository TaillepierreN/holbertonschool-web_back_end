# Python - Variable Annotations

Welcome to the "Python - Variable Annotations" project! This project is part of Holberton School's curriculum designed to introduce you to type annotations in Python. By the end of this project, you'll have a practical understanding of how to use type annotations to specify the expected data types of variables, function parameters, and return types.

## Concepts

For this project, please review the following concept:
- [Advanced Python](https://intranet.hbtn.io/concepts/550)

## Resources

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives

After completing this project, you should be able to:
- Explain the purpose and benefits of type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand and explain the concept of duck typing.
- Validate your code with `mypy`, a static type checker for Python.

## Requirements

### General

- **Environment**: Ubuntu 20.04 LTS using Python 3.9
- **Style**: Code should follow the Pycodestyle (PEP 8) style (version 2.5).
- **Documentation**:
  - All modules, classes, and functions must include docstrings.
  - Use the Python interpreter to check documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- **Execution**: All your files should be executable (`chmod +x <filename>`).

### Tasks

0. **Basic annotations - add**: Create a function `add` that returns the sum of two floats.
1. **Basic annotations - concat**: Develop a function `concat` that concatenates two strings.
2. **Basic annotations - floor**: Implement a function `floor` that returns the floor of a float.
3. **Basic annotations - to string**: Write a function `to_str` that converts a float to a string.
4. **Define variables**: Annotate variables with specific values (integer, float, boolean, string).
5. **Complex types - list of floats**: Write a function `sum_list` that returns the sum of a list of floats.
6. **Complex types - mixed list**: Create a function `sum_mixed_list` that sums a list of integers and floats.
7. **Complex types - string and int/float to tuple**: Develop a function `to_kv` that returns a tuple containing a string and the square of an int/float.
8. **Complex types - functions**: Implement a function `make_multiplier` that returns a function multiplying a float by a given multiplier.
9. **Let's duck type an iterable object**: Annotate a function to specify that it takes an iterable of sequences and returns a list of tuples.
