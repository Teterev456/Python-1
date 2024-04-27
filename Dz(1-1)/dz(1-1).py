cycle = str()
while cycle != "exit":
    a = input("Введите число: ")
    cycle = a
    if a == "exit":
        break
    try:
        a_int = int(a)
        a_list = list(a)
        if type(a_int) == int:
            print("Длина числа равна -", len(a_list))
    except ValueError:
        print("Вы ввели не число, попробуйте снова.")
