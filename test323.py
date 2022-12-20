d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3', 'name4': 'id4'}
d_new = {}

new_key = list(d.keys())
new_value = list(d.values())

for i in range(0, len(new_value)):
    d_new[new_value[i]] = new_key[i]

print("Исходный словарь: ", d)
print("Новый словарь: ", d_new)

