# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
import math

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
a = abs(k - list_1[0])
b = list_1[0]

for i in list_1:
    if a >= abs(k-i):
        a = abs(k-i)
        b = i
print(b)      
        
