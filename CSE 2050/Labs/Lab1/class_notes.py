def binary_search(L, item):
    if len(L) == 0:
        return False
    mid = len(L) // 2
    if item == L[mid]:
        return True
    if item < L[mid]:
        return binary_search(L[:mid], item)
    else:
        return binary_search(L[mid+1:], item)
    

def binary_search_better(L, item):
    return _binary_search_better(L, item, 0, len(L))


def _binary_search_better(L, item, left, right):
    if left == right:
        return False
    mid = (right + left) // 2
    if item == L[mid]:
        return True
    elif item < L[mid]:
        _binary_search_better(L, item, left, mid)
    else: 
        _binary_search_better(L, item, mid+1, right)
    

def selection_sort(L):
    n = len(L)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L       
L = [3,5,1,0,23,54,11,90]
print(selection_sort(L))



def merge(A, B, L):
    """
    Merges contents from sorted lists A and B into list L, such that
    L is sorted upon return.
    When called by mergesort, we have that len(L) == len(A) + len(B).
    """
    i = 0 
    j = 0

     

    while i < len(A) and j < len(B):
        
        if A[i] < B[j]:
            L[i + j] = A[i]
            i += 1
        elif A[i] > B[j]:
            L[i + j] = B[j]
            j += 1
    while i < len(A):
        L[i + j] = A[i]
        i += 1
    while j < len(B):
        L[i + j] = B[j]
        j += 1





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


def mergesort(L):
    """Sorts the input list L."""
    # base case
    if len(L) < 2:
        return
    # divide
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]
    # conquer
    A = mergesort(A)
    B = mergesort(B)
    # combine
    merge(A, B, L)


def quick_sort(L):
    if len(L) < 2:
        return L 
    pivot = L[-1]
    LT = quick_sort([i for i in L if i < pivot])
    EQ = quick_sort([i for i in L if i == pivot])
    GT = quick_sort([i for i in L if i > pivot])
    return LT + EQ + GT


def _partition(L, Left, Right):
    pivot = Right - 1
    i = Left
    j = pivot - 1
    while i < j:
        while L[i] < L[pivot]:
             i += 1
        while i < j and L[j] >= L[pivot]:
             j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    

    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    
    return pivot     #O(n)

def quickselect(L, left=0, Rright=None):
    if right is None: right =len(L)
    pivot = right - 1
    i = left
    j = pivot - 1

    while i<j:
        while L[i] < L[pivot]:
            i += 1
        while i < j and L[j] >= L[pivot]:
             j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]

    if L[pivot] <= L[i]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i


    if pivot == len(L) //2:
        return L[pivot]
    elif pivot > len(L) // 2: 
        return quickselect(L, left, pivot)
    elif pivot < len(L) // 2: 
        return quickselect(L, pivot+1, right)
    
    

def greedy_fc(amt, coins):
    coins.sort(reverse=True)
    n = 0
    for c in coins:
        while c <= amt:
            amt -= c
            n += 1

    






if __name__ == "__main__":
    L = list(reversed(range(20)))
    print(f"before mergesort: {L}")
    mergesort(L)
    print(f"after mergesort: {L}")