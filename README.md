# ReviewIt-AI GitHub Actions

- The code is working and getting the PR details and suggesting improvements (please check the [sample PR](https://github.com/sachs7/reviewit-ai-git-actions/pull/20/checks#step:5:22))
- Facing an issue of posting a comment on the PR with the response from ReviewIt-AI (to be fixed soon!)

### Sample Output:

- Help:

```
(reviewit-ai-git-actions) ➜  reviewit-ai-git-actions git:(fix) ✗ python .github/actions/reviewit.py --help                                 

Usage: reviewit.py [OPTIONS]

Options:
  -r, --repo-name TEXT     The name of the repository  [required]
  -p, --pr-number INTEGER  The pull request number  [required]
  --help                   Show this message and exit.
```

- Example run:

```
(reviewit-ai-git-actions) ➜  reviewit-ai-git-actions git:(temp) python .github/actions/reviewit.py -r 'sachs7/reviewit-ai-git-actions' -p 10

def something(a, b):
  return a+b + c
The provided function `something` is intended to take two arguments, `a` and `b`, and return their sum along with an additional variable `c`. However, there are a few issues with this code:

1. **Undefined Variable**: The variable `c` is not defined within the function or passed as an argument, which will result in a `NameError` when the function is called.

2. **Function Naming**: The function name `something` is not descriptive of what the function does. A more descriptive name would be better, such as `sum_with_constant`.

3. **Documentation**: The function lacks a docstring, which is a good practice to explain what the function does, its parameters, and what it returns.

Here's an improved version of the function:
```

```python
def sum_with_constant(a, b, c):
    """
    Returns the sum of two numbers, a and b, with an additional constant c.

    Parameters:
    a (int/float): The first number to add.
    b (int/float): The second number to add.
    c (int/float): The constant to add to the sum of a and b.

    Returns:
    int/float: The sum of a, b, and c.
    """
    return a + b + c
```
```
In this improved version, I've added the following:

- A third parameter `c` to the function signature so that it is defined when the function is called.
- A descriptive function name.
- A docstring that explains the function's purpose, parameters, and return value.

Remember to always define all the variables you use and provide clear documentation for your functions.
```
