def gen_fibonacci(n = None):
    k = 0
    num1 = 0
    yield num1
    num2 = 1
    yield num2
    while True:
        res = num1 + num2
        yield res
        num1 = num2
        num2 = res
        k += 1
        if k > n - 3:
            return


for i in gen_fibonacci(5):
    print(i)