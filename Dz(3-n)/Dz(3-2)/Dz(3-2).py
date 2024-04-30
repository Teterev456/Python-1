list1 = list(input("Введите список элементов: "))


def func1(list1: list, a: int) -> list:
    res = list1 * a
    return res


try:
    a = int(input("Введите число: "))
    print(func1(list1, a))
except ValueError:
    print("Ошибка, неверно введённый коэффицент, ваше значение изменено на 2:")
    print(func1(list1, 2))

# Lambda-функция
#func2 = lambda list1, a: list1 * a
#print(func2(list1, a))
