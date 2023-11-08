# a = int(input('Input variable: '))
# print(type(a))
# # c:int = 5.2
# # b = c/2
# b = a/2
# print(b)
# print(type(b))

a = int(input('Input variable a: '))
b = int(input('Input variable b: '))

# Вывести сумму всех чисел в диапозоне [a, b]
# Если a > b, то вывести сообщение об ошибке

sum = 0
if a > b: 
    print ('error')
else:
    for i in range(a, b):
        sum = sum + i
        print(i)
    sum = sum + b
    print (sum)
