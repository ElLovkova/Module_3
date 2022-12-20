l = [1, "b", 10, "a", 10, 4, "a", "b", 2, 3, "a"]
l_eq = []
for i in l:
    if l.count(i) > 1:
        if i not in l_eq:
            l_eq.append(i)
print("Исходный список: ", l)
print("Результат: ", l_eq)

