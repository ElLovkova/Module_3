x = float(input("Введите x: "))
y = float(input("Введите y: "))
p = float(input("Введите p: "))
i = 0
while x < y:
    if (x == int(x + x*(p/100))):
        print("При данных условиях никогда")
        break
    i += 1
    x = int(x + x*(p/100))
    #print(x)
else:
    print("Через ", i, " лет")


