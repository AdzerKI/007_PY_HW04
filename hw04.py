# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
d = input("введите точность d: ")
temp = d.split(".") 
temp = len(temp[1])
result = round(math.pi, temp)
print(f"при d = {d}, π = {result}")

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите N: "))
arr = []
for i in range (1, n - 1):
    if n % i == 0:
        arr.append(i)
print(arr)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

#на семнаре с set подсказали, но он не понял как можно и Вы сказали не получится, я думал как красивее) 
# можно с set, интересно было, вот решение красивое без библиотек внешних
arr = [1, 2, 4, 6, 2, 3, 1]
newArr = []
num = set(arr)
for n in num:
    newArr.append(n) 
print(f"{arr} -> {newArr}")


# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# тут я ещё на уроке уловил смысл, мы берем формируем степень и добавляем ее к строке,
# когда это понимаешь то задача абсолютно простой становится
from  random import randrange

k = int(input("Введите k: "))
func = ""

if k < 1:
    print("error")
else:
    for i in range (k, 0, -1):
        temp = randrange(0,9)
        if temp != 0 and temp != 1:
            func += f"{temp}*x**{i} + "
        if i != 0 and temp != 0:
            func += f"{temp}"
func += " = 0"
print(func) 

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# работать в конкретной системе будет, не вижу смысла в её решении, скучно, обычный парсер, давай лучше твою распарсим