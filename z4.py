import random # модуль рандома
num = [] # создаем пустой список
for _ in range(10):
    num.append(random.randint(1,100)) # генерация случайных чисел от 1 до 100
print("Случайный список из 10 чисел:", num)

max_num = max(num)
min_num = min(num)
print("Наибольшее число:", max_num)
print("Наименьшее число:", min_num)

t = sum(num)
print("Сумма элементов списка:", t)

num.sort() # sort по умолч. сортирует по возрастанию. можно сортировать по убыванию с помощью reverse
print("Отсортированный список:", num)
