while True:
    a = input("Введите трёхзначное число с неповторяющимися цифрами: ")
    try:
        a_list = list(a)
        a_int = int(a)
        if (a_int < 100 or a_int > 1000):
            print("Это не трёхзначное число, попробуйте снова: ")
        else:
            if a_list[0] != a_list[1] and a_list[0] != a_list[2] and a_list[1] != a_list[2]:
                i = 0
                print(a_list[0], a_list[1], a_list[2])
                print(a_list[0], a_list[2], a_list[1])
                print(a_list[1], a_list[0], a_list[2])
                print(a_list[1], a_list[2], a_list[0])
                print(a_list[2], a_list[1], a_list[0])
                print(a_list[2], a_list[0], a_list[1])
            else:
                print("Вы ввели число с повторяющимися цифрами, попробуйте снова.")
    except ValueError:
        print("Вы ввели не число, попробуйте снова.")
