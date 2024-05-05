def fibonacci(n):
    i = 0
    n1 = 1
    n2 = 1
    print(n1)
    print(n2)
    while i < n - 2:
        n12 = n1 + n2
        n1 = n2
        n2 = n12
        i = i + 1
        yield n12


n = int(input("Введите кол-во чисел Фибоначчи: "))

k = 0
l1 = fibonacci(n)
while k < n - 2:
    k += 1
    print(next(l1))
