def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert average_num(list1) == 5

list2 = ['a', 2, 3, 4, 5, 6, 7, 8, 9]
assert average_num(list2) == "Bad request"

list3 = [1, -2]
assert average_num(list3) == -0.5

list4 = [list1, list2, list3]
assert average_num(list4) == "Bad request"

list5 = [True, False, True, True]
assert average_num(list5) == 0.75

list6 = [list1]
assert average_num(list6) == "Bad request"

list7 = ["Bad request"]
assert average_num(list7) == "Bad request"

list8 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
assert average_num(list8) == 0.55

list9 = [list1[0], list1[1], list1[2], list1[3], list1[4], list1[5]]
assert average_num(list9) == 3.5

list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert average_num(list10) != 50
