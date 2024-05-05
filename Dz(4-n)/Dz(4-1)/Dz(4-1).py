# 1
numbers = [i ** 2 for i in range(1,11)]
print(numbers)

# 2
list_keys = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
v = 1
v1 = list_keys[v]
keys_dict = {v: list_keys.index(v, 0, 7) + 1 for v in list_keys}
print(keys_dict)

# 3
list_base = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
set_list = set(i.lower() for i in list_base)
print(set_list)
