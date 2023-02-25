def binary_search_2(arr, x):
    """
    Функция для бинарного поиска элемента x в отсортированном массиве arr
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

