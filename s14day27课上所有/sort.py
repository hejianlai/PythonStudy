import random
import time
import copy
import sys

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper

@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

@cal_time
def bubble_sort_1(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break

def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]


def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1]=li[j]
            j = j - 1
        li[j + 1] = tmp


def quick_sort_x(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort_x(data, left, mid - 1)
        quick_sort_x(data, mid + 1, right)

def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


@cal_time
def quick_sort(data):
    return quick_sort_x(data, 0, len(data) - 1)

@cal_time
def sys_sort(data):
    return data.sort()


def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high: #只要没到子树的最后
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:#如果领导不能干
            data[i] = data[j] #小领导上位
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp


def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
        for i in range(n - 1, -1, -1):
            data[0], data[i] = data[i], data[0]
            sift(data, 0, i - 1)





sys.setrecursionlimit(100000)
data = list(range(1000, 1, -1))
data.sort()
#random.shuffle(data)
data1 = copy.deepcopy(data)
data2 = copy.deepcopy(data)
data3 = copy.deepcopy(data)

bubble_sort(data1)
quick_sort(data2)
sys_sort(data3)


