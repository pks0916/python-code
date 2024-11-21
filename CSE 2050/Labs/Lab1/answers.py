import time
import random 



# Include your answers for this lab in the dictionary below.
# The keys of the dictionary are the pre-numbered algorithms.
# The values are your answers. Use:
#     'bubble'
#     'selction'
#     'insertion'
#     'merge'
#     'quick'

# #For instance, if you though all the algorithms  were bubble sort (they are not), this file should read:
# answers = {'alg_a': 'bubble',
#            'alg_b': 'bubble',
#            'alg_c': 'bubble',
#            'alg_d': 'bubble',
#            'alg_e': 'bubble'}


def selection(L): #selection
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L 


def merge(A, B, L):
    """
    Merges contents from sorted lists A and B into list L, such that
    L is sorted upon return.
    When called by mergesort, we have that len(L) == len(A) + len(B).
    """
    i = 0 
    j = 0

     

    while i < len(A) or j < len(B):
        if (j == len(B)) or (i <  len(A) and A[i] < B[j]):
            L[i + j] = A[i]
            i += 1
        else:
            L[i + j] = B[j]
            j += 1


def merge_sort(L):   #merge
    """Sorts the input list L."""
    # base case
    if len(L) < 2:
        return
    # divide
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    # conquer
    merge_sort(A)
    merge_sort(B)
    # combine
    merge(A, B, L)


def quick(L): #quick
    if len(L) < 2:
        return L 
    pivot = L[-1]
    LT = merge_sort([i for i in L if i < pivot])
    EQ = merge_sort([i for i in L if i == pivot])
    GT = merge_sort([i for i in L if i > pivot])
    return LT + EQ + GT

def insertion (arr, n=None, num_swaps=0): #insertion 
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

    return insertion (arr, n - 1, num_swaps)


def bubble(arr, n=None, num_swaps=0): #bubble
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

    return bubble(arr, n - 1, num_swaps)

# Fill in your answers as the values in the dict below
answers = {'alg_a': 'selection',
           'alg_b': 'quick',
           'alg_c': 'bubble',
           'alg_d': 'merge',
           'alg_e': 'insertion'
          }

valid_ans = {'bubble', 'selection', 'insertion', 'merge', 'quick'}
# Run this file in terminal to see if you used the correct formatting in your answer.
for k, v in answers.items():
    if v not in valid_ans:
        raise ValueError(f"Value '{v}' for key '{k}' is not in {valid_ans}")

print("Valid answer! Find out if it's right after the due date.")


def time_f(func, args, trials=5):
    """Returns minimum time trial of func(args)"""
    t_min = float('inf')

    for i in range(trials):
        start = time.time()
        func(args)
        end = time.time()
        if end-start < t_min: t_min = end - start

    return t_min

