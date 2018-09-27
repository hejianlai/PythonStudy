import time
import random

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper

@cal_time
def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid]['id'] == val:
            return mid
        elif data_set[mid]['id'] < val:
            low = mid + 1
        else:
            high = mid - 1
    return


def binary_search(dataset, find_num):
    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == find_num:
            #print("Find it")
            return dataset[mid]
        elif dataset[mid] > find_num:
            return binary_search(dataset[0:mid], find_num)
        else:
            return binary_search(dataset[mid + 1:], find_num)
    else:
        if dataset[0] == find_num:
            #print("Find it")
            return dataset[0]
        else:
            pass
            #print("Cannot find it.")

@cal_time
def binary_search_alex(data_set, val):
    return binary_search(data_set, val)




def random_list(n):
    result = []
    ids = list(range(1001,1001+n))
    a1 = ['zhao','qian','sun','li']
    a2 = ['li','hao','','']
    a3 = ['qiang','guo']
    for i in range(n):
        age = random.randint(18,60)
        id = ids[i]
        name = random.choice(a1)+random.choice(a2)+random.choice(a3)





data = list(range(100000000))

print(bin_search(data, 173320))
print(binary_search_alex(data, 173320))