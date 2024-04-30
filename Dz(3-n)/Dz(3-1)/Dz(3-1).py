a = int(input("Введите первое число: "))

sign = input("Введите знак операции(+, -, *, /, ^, exit): ")


def exit_prog():
    return "Выход из программы"


if sign == "exit":
    print(exit_prog())

else:
    b = int(input("Введите второе число: "))

    def sum_ab(a, b):
        c = a + b
        return c

    def diff_ab(a, b):
        c = a - b
        return c

    def multiply_ab(a, b):
        c = a * b
        return c

    def division_ab(a, b):
        c = a / b
        return c

    def power_ab(a, b):
        c = a ** b
        return c


    if sign == "+":
        print(sum_ab(a, b))
    elif sign == "-":
        print(diff_ab(a, b))
    elif sign == "*":
        print(multiply_ab(a, b))
    elif sign == "/":
        try:
            print(division_ab(a, b))
        except ZeroDivisionError:
            print("Невозможная операция, повторите снова.")
    elif sign == "^":
        print(power_ab(a, b))
    else:
        print("Такого знака нет, попробуйте снова.")
