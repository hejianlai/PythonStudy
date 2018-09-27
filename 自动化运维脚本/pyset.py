some_list = ['a', 'b', 'c', 'd', 'm', 'm']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        duplicates.append(value)
print(duplicates)