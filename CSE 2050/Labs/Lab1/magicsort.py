import math
from enum import Enum

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """
    An enumeration class representing different cases for the input list.
    """
    GENERAL = 0
    SORTED = 1
    CONSTANT_NUM_INVERSIONS = 2
    REVERSE_SORTED = 3


def linear_scan(L):
    """
    Perform a linear scan on the input list to determine its case.

    Args:
        L (list): The input list.

    Returns:
        MagicCase: An enum representing the case of the input list.
    """
    num_swaps = 0
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            
            num_swaps += 1

    if num_swaps == 0:
        return MagicCase.SORTED
    elif num_swaps == len(L) - 1:
        return MagicCase.REVERSE_SORTED
    elif num_swaps <= INVERSION_BOUND:
        return MagicCase.CONSTANT_NUM_INVERSIONS
    else:
        return MagicCase.GENERAL


def reverse_list(L, alg_set=None):
    """
    Reverse the input list in-place.

    Args:
        L (list): The input list to be reversed.
        alg_set: Unused parameter. Included for consistency with other functions.
    """
    if alg_set is None:
        alg_set = set()
    
    k = 0
    j = len(L) - 1
    while k < j:
        L[k], L[j] = L[j], L[k]
        k += 1
        j -= 1


def magic_insertionsort(L, left, right, alg_set=None):
    """
    Perform insertion sort on the specified range of the input list."""
    if alg_set is None:
        alg_set = set()
    
    for i in range(left + 1, right):
        key = L[i]
        j = i - 1
        while j >= left and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key
    alg_set.add("magic_insertionsort")
    return alg_set


def magic_mergesort(L, left, right, alg_set=None):
    """
    Perform merge sort on the specified range of the input list.

    

    Returns:
        list: The sorted sublist.
    """
    if alg_set is None:
        alg_set = set()
    L2 = L[left:right+1]  
    
    if len(L2) <= 1:
        return L2
    
    if right - left <= 20:
        alg_set.add("magic_insertionsort")
        return magic_insertionsort(L, left, right, alg_set)
    
    median = len(L2) // 2

    A = L2[:median]
    B = L2[median:]
    magic_mergesort(A, 0, len(A)) 
    magic_mergesort(B, 0, len(B)) 

    i = 0
    j = 0
    k = left  

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1
        k += 1

    
    while i < len(A):
        L[k] = A[i]
        i += 1
        k += 1
    while j < len(B):
        L[k] = B[j]
        j += 1
        k += 1

    alg_set.add("magic_mergesort")
    return alg_set
    return L2


def magic_quicksort(L, left, right, depth=0, alg_set=None):
    """
    Perform quicksort on the specified range of the input list.

    
    """
    if alg_set is None:
        alg_set = set()
    if right - left <= 20:
        magic_insertionsort(L, left, right)
        alg_set.add("magic_insertionsort")
        return alg_set
        return
    
    if depth > 2 * (math.log2(right - left) + 1):
        magic_mergesort(L, left, right)
        alg_set.add("magic_mergesort")
        return alg_set
        return
    
    pivot = right - 1
    i = left
    j = right - 2

    while i < j:
        while L[i] < L[pivot]:
            i += 1
        while L[j] > L[pivot] and i < j:
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    
    magic_quicksort(L, left, pivot, depth + 1)
    magic_quicksort(L, pivot + 1, right, depth + 1)
    alg_set.add("magic_quicksort")
    return alg_set


def magicsort(L, alg_set=None):
    """
    Perform a sorting algorithm based on the type of input list.

    
    Returns:
        set: A set containing the names of sorting algorithms used.
    """
    if alg_set is None:
        alg_set = set()
    case = linear_scan(L)
    if case == MagicCase.SORTED:
        alg_set.add('linear_scan')
        return alg_set
    elif case == MagicCase.REVERSE_SORTED:
        reverse_list(L, alg_set)
        alg_set.add('reverse_list')
        return alg_set
    elif case == MagicCase.CONSTANT_NUM_INVERSIONS:
        magic_insertionsort(L, 0, len(L), alg_set)
        alg_set.add('magic_insertionsort')
        return alg_set
    else:
        magic_quicksort(L, 0, len(L), alg_set=alg_set)
        alg_set.add('magic_quicksort')
        return alg_set
    

