import time
n = int(input("Введите число: "))
i = n
while i >= 1:
    print(i)
    i -= 1
    time.sleep(0.3)

f = 1
e = 1
while e <= n:
    f *= e
    e += 1
print("Факториал числа", n, "равен:", f)