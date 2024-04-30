while True:
    try:
        numbers = input("Введите ряд чисел, разделяя их пробелом: ")
        numbers_list = list(numbers)
        power = int(input("Введите степень в которую вы возводите ранее введённый список чисел(): "))
        i_num = int()
        i = 0
        answer = []
        for i in range(len(numbers)):
            if numbers[i] != " ":
                i_num = int(numbers_list[i])
                answer.append(pow(i_num, power))
            i += 1
        print("Вывод: ", answer)
    except ValueError:
        print('Некорректный ввод, повторите попытку.')
