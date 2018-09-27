import copy
li = [1, 5, 4, 2]
target = 3
max_num = 100

def func1():
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == target:
                return (i,j)



def bin_search(data_set, val, low, high):
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return

def func2():
    li2 = copy.deepcopy(li)
    li2.sort()
    for i in range(len(li2)):
        a = i
        b = bin_search(li2, target - li2[a], i+1, len(li2)-1)
        if b:
            return (li.index(li2[a]),li.index(li2[b]))

def func3():
    a = [None for i in range(max_num+1)]
    for i in range(len(li)):
        a[li[i]] = i
        if a[target-li[i]] != None:
            return (a[li[i]], a[target-li[i]])


print(func3())



data_dict = {}
for i in range(len(data_list)):
    if data_list[i] in data_dict:
        print(data_dict[data_list[i]], i)
    else:
        data_dict[13 - data_list[i]] = i