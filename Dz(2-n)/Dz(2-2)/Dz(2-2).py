my_str = str(input('Введите строку: '))
my_str = my_str.lower()
i = 0
sign = str()
for i in range(len(my_str)):
    if my_str[i] != ' ':
        if my_str[i] not in sign:
            sign += my_str[i]
            print(f'"{my_str[i].lower()}":  "{my_str.count(my_str[i])}"')
