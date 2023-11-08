# СПИСОК
a = list("Это список")
a[0] = 'a'
print(a[1], type(a))
b = [2, 4, 4, 'hi']
print(b, type(b))

b.append(10)
for item in b:
    print(item, "и его индекс: ", b.index(item))
    # i = i + 1
    # print(item, "и его индекс: ", i)

# КОРТЕЖ
'''a = tuple("string")
print(a, type(a))
b = ("Это кортеж", 3)
print(b, type(b))'''

# СЛОВАРЬ
'''a = {"name": "Ivan", "age": 18, "isHuman": True}
print(a, type(a))
b = dict(name="Vitalik", age=18)
print(b, type(b))'''



