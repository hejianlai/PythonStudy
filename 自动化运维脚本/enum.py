my_list = ['apple', 'banana', 'grapes', 'per']
for c, value in enumerate(my_list, 1):
    print(value, c)
counter_list = list(enumerate(my_list, 1))
print(counter_list)
print(id(my_list))