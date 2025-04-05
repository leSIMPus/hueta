import random
num = []
for _ in range(20):
    num.append(random.randint(1,100))
print("Случайный список из 20 чисел:", num)

print("Чётные числа из списка:")
for cn in num:
    if cn % 2 == 0: # проверяем, делится ли число на 2
       print(cn)

print("Числа из списка, кратные трём:")
for zn in num:
    if zn % 3 == 0: # проверяем, делится ли число на 3
       print(zn)

s = sum(num) / len(num)  # формула среднего арифметического..
print("Среднее арифметическое чисел из списка:", s)