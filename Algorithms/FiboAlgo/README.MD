# Fibonacci Sequence Printer

**Fibonacci Sequence Printer** is a minimal Python utility that prints the Fibonacci series up to a given limit. It provides a simple demonstration of iterative control flow and number generation, great for educational use or basic scripting.
![Fibonacci spiral](https://upload.wikimedia.org/wikipedia/commons/9/93/Fibonacci_spiral_34.svg)


---

## Features

- Prints all Fibonacci numbers **less than a specified value**
- Uses a **while loop** for efficient iteration
- Outputs the series in a clean, single-line format
- Simple to extend or embed in larger scripts

---

## How It Works

The script defines a function `fib(n)` which initializes two variables (`a` and `b`) representing the current and next numbers in the sequence. It iterates while `a < n`, printing each number and updating the state.

### Sample Output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

## How to Use

1. Clone or download the script.
2. Open it in any Python environment (Python 3.x recommended).
3. Run the script with a chosen upper limit:

   ```python
   fib(2000)

## Requirements
1. Python 3.6 or higher
2. No external dependencies

## Run it
    python3 Fibo.py
