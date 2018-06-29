mem = {0: 0, 1: 1}

def fib(n):
    global mem
    f = mem.get(n)
    if f is not None:
        return f
    else:
        f = fib(n - 1) + fib(n - 2)
        mem[n] = f
        return f 

print(fib(8))
print(fib(15))
print(fib(100))
print(fib(200))
print(fib(500))
print(fib(1000))
