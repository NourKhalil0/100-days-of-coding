def fib(n):
    """Print a Fibonacci series less than n."""
    a, b = 0 ,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
fib(2000)