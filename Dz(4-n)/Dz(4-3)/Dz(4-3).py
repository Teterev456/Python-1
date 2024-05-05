fileName = str(input("Введите имя файла: "))
text = str(input("Введите текст файла: "))


def function(file_name, text):
    with open(fileName, 'a') as file:
        file.write(text + '\n')
    file.readlines()
    enum = enumerate(file)
    enum_list = list(enum)
    i = 0
    for i, element in enum:
        if i % 2 == 0:
            print(enum_list[i])
    file.close()


print(function(fileName, text))
