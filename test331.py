def area(a, b, c):
    p = (a + b + c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5


A = float(input("Введите a: "))
B = float(input("Введите b: "))
C = float(input("Введите c: "))
print(area(A, B, C))
