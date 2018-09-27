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
    while j <= high:    #孩子在堆里
        if j + 1 <= high and data[j] < data[j+1]:   #如果有右孩子且比左孩子大
            j += 1  #j指向右孩子
        if data[j] > tmp:   #孩子比最高领导大
            data[i] = data[j]   #孩子填到父亲的空位上
            i = j               #孩子成为新父亲
            j = 2 * i +1        #新孩子
        else:
            break
    data[i] = tmp           #最高领导放到父亲位置

@cal_time
def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
    #堆建好了
    for i in range(n-1, -1, -1):            #i指向堆的最后
        data[0], data[i] = data[i], data[0] #领导退休，刁民上位
        sift(data, 0, i - 1)                #调整出新领导

# def heap_sort(data):
#     n = len(data)
#     for i in range(n // 2 - 1, -1, -1):
#         sift(data, i, n - 1)
#     #堆建好了
#     li = []
#     for i in range(n-1, -1, -1):            #i指向堆的最后
#         li.append(data[0])
#         data[i] = data[0]
#         sift(data,0,i-1)


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp


def _mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _mergesort(li,low, mid)
        _mergesort(li, mid+1, high)
        merge(li, low, mid, high)

@cal_time
def mergesort(li):
    _mergesort(li, 0, len(li) - 1)

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1]=li[j]
            j = j - 1
        li[j + 1] = tmp

@cal_time
def shell_sort(li):
    gap = int(len(li) // 2)
    while gap >= 1:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[i - gap] = tmp
        gap = gap // 2


@cal_time
def count_sort(li, max_num):
    count = [0 for i in range(max_num + 1)]
    for num in li:
        count[num] += 1
    i = 0
    for num,m in enumerate(count):
        for j in range(m):
            li[i] = num
            i += 1

@cal_time
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1]=li[j]
            j = j - 1
        li[j + 1] = tmp


# def topk(li, k):
#     ltmp = li[0:k + 1]
#     insert_sort(ltmp)
#     for i in range(k, len(li)):
#         ltmp[k]=li[i]
#         tmp = ltmp[k]
#         j = k - 1
#         while j >= 0 and ltmp[j] > tmp:
#             li[j + 1] = ltmp[j]
#             j = j - 1
#         li  [j + 1] = ltmp
#     return ltmp

def topn(li, n):
    heap = li[0:n]
    for i in range(n // 2 - 1, -1, -1):
        sift(heap, i, n - 1)
    #遍历
    for i in range(n, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, n - 1)
    for i in range(n - 1, -1, -1):  # i指向堆的最后
        heap[0], heap[i] = heap[i], heap[0]  # 领导退休，刁民上位
        sift(heap, 0, i - 1)  # 调整出新领导
    return heap


#
# sys.setrecursionlimit(100000)
# #data = list(range(100000, 0, -1))
# data = []
# for i in range(100000):
#     data.append(random.randint(0,100))
# # data.sort()
# #random.shuffle(data)
# data1 = copy.deepcopy(data)
# data2 = copy.deepcopy(data)
# data3 = copy.deepcopy(data)
# #
# # bubble_sort(data1)
# #quick_sort(data2)
# count_sort(data1, 100)
# # sys_sort(data3)
# #mergesort(data3)
# sys_sort(data3)


# li=[1,4,5,6,2,3,7,8,9]
# merge(li, 0, 3, 8)
# print(li)
#

li = list(range(10000))
random.shuffle(li)
print(topn(li, 10))

