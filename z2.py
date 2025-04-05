import time # время)
n = int(input("Введите число: "))
print("Все числа от 1 до",n,":")
for i in range(1, n+1):
    print(i)
    time.sleep(0.3) # это просто чтобы красиво медленно появлялись

print("Все квадраты чисел от 1 до",n,":")
for e in range(1, n+1):
    print(e**2)
    time.sleep(0.3)
s = 0 # переменная чтобы ввести в цикл
for o in range(1, n+1):
    s+=o
print("Сумма всех чисел от 1 до ",n,"равна:",s)
