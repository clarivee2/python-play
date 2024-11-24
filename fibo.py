# module example - see helloworld.py for implementation

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# make the module executable from cli - ie.  python fibo.py 50
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
