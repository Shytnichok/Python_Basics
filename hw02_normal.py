# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано:
from math import sqrt
temp_in = [2, -5, 8, 9, -25, 25, 4]
temp_out = []
for itm in temp_in:
    if itm>0 and sqrt(itm)%1 == 0:
        temp_out.append(int(sqrt(itm)))
print(temp_out)
#Результат: [3, 5, 2]

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
'''
from num2words import num2words
print(num2words(1, lang='ru',to='ordinal'))
'''
# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
from random import randint

i = int(input()) - 1 #n - элементов
temp_ls = []
while i:
    temp_ls.append(randint(-100,100))
    i -= 1
print(temp_ls)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
lst_in = [1, 2, 4, 5, 6, 2, 5, 2]
lst_out1 = list(frozenset(lst_in))
lst_out2 = []
for itm in lst_in:
    if lst_in.count(itm) == 1:
        lst_out2.append(itm)
print(lst_out1)
print(lst_out2)