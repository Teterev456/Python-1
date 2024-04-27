ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
target = str(input("Введите поле (формат - А1/а1): "))
target = target.upper()
if len(target) < 2 or len(target) > 3:
    print("Неверный формат, попробуйте снова")
else:
    if target in ship:
        print("Вы попали!")
    else:
        print("Промах!")
