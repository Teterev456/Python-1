dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
dct_keys = dct.keys()
dct_values = dct.values()
print(dct_keys, dct_values)
union = dct_keys | dct_values
print(union)  # Множество не может содержать повторяющиеся значения, поэтому в нём только неповторяющиеся значения
