import random
import time
def bubble_sort(arr, n=None, num_swaps=0):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr, num_swaps

    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            num_swaps += 1
            swapped = True

    if not swapped:
        return arr, num_swaps

    return bubble_sort(arr, n - 1, num_swaps)


def selection_sort(arr, end=None, num_swaps=0):
    if end is None:
        end = len(arr)

    if end <= 1:
        return arr, num_swaps

    max_index = 0
    for i in range(1, end):
        if arr[i] > arr[max_index]:
            max_index = i

    arr[end - 1], arr[max_index] = arr[max_index], arr[end - 1]
    num_swaps += 1

    return selection_sort(arr, end - 1, num_swaps)


def insertion_sort(arr, n=None, num_swaps=0):
    if n is None:
        n = len(arr)

    if n <= 1:
        return arr, num_swaps

    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        num_swaps += 1

    arr[j + 1] = key

    return insertion_sort(arr, n - 1, num_swaps)