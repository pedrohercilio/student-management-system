dict1 = {"1": {"abc": 3},
        "2": {"def": 6},
        "3": {"ghi": 9},
        "12": "asda",
        "22": "asd"}

list1 = ["1", "2", 3]


print(list1[len(list1) - 1])

keys = list(dict1.keys())
ultimo_valor = keys[len(keys) - 1]

print(keys)
print(ultimo_valor)