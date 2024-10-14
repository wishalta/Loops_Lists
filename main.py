from collections import Counter
from inspect import istraceback
from operator import index

# 1

# list = ["Rolandas", "Lukas", "Staniulis"]
#
# print(list)
# print(list[0])
# print(list[2])
# print(len(list))

# 2

# high = [182, 170, 200]
# print(high)
# print(len(high))

# 3


# # creating an empty list
# lst = []
#
# # number of elements as input
# n = int(input("Enter number of elements : "))
#
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
#     # adding the element
#     lst.append(ele)
#
# print(lst)
# sk = len(lst)
# print(f'{sk} Pazymiu kiekis')

# 4

# list = ['Vilnius', 'Kaunas', 'Klaipeda', 'Panevezys']
# print(list)
# add = input('Miestas: ')
# a = int(input('Vieta: '))   #int jei nori ivesti skaiciu (input kai zodis)
# print(a)
# list.insert(a, add)
# print(list)
# # a = print('miesto vieta: ')
# #
# # list.insert[1, 2]
# # print(list)

# 5

# list = [0, 1, 2, 3, 4, 5, 6, 7]
# print('Yra 7 duomenys')
# list.pop()
# a = int(input('Kiek norit istrinti: '))
# for x in range(a):
#     list. pop()
# print(list)

# 6

# list = [1, 2, 3, 4, 5, 6, 7]
# g = len(list)
# print(g)
# if len(list) > 5:
#     list.clear()
#     print(list)
# else:
#     print(True)

# 7

# list = ['opa', 'gola', 'hola', 'goal', 'meaning']
# element = input('Jusu norimas zodis: ')
# g = list.index(element)
# print(f'Positiot: {g}')
# if element in list:
#     print(True)

# 8

list = []
n = int(input('Kiek pazymiu jus turite: '))
for i in range (0, n):
    variable = int(input('Grade: '))
    list.append(variable)
print(list)

y = 10

x =[i for i in list if i==y]
print(len(x))

# 9

