
from random import randint

n = int(input("Введите n: "))
m = [[randint(0,100) for i in range(n)] for j in range(n)]
m_max = []
print(m)

for i in m:
    m_max.append(max(i))
print("Максимальный элемент: ", max(m_max))


