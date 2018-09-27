def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            left = mid
            right = mid
            while left >= 0 and data_set[left] == val:
                left -= 1
            while right < len(data_set) and data_set[right] == val:
                right += 1
            return (left + 1, right - 1)
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return (-1, -1)


def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low+high)//2
        if data_set[mid] == val:
            left = mid
            right = mid
            while left >= 0 and data_set[left] == val:
                left -= 1
            while right < len(data_set) and data_set[right] == val:
                right += 1
            return (left + 1, right - 1)
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return



li = [1,2,3,3,3,4,4,5]
print(bin_search(li, 5))