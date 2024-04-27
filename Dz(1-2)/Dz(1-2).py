while True:
    print("")
    a = input("Введите число: ")
    try:
        a_list = list()
        a_int = int(a)
        sum_neg = int(0)
        sum_pos = int(0)
        for a in range(-a_int, a_int+1):
            a_list.append(a)
            if a < 0:
                sum_neg += a
            elif a > 0:
                sum_pos += a
        print(a_list, "\n")
        print("Сумма отрицательных чисел равна:", sum_neg)
        print("Сумма положительных чисел равна:", sum_pos)
    except ValueError:
        print("Вы ввели не число, попробуйте снова.")
