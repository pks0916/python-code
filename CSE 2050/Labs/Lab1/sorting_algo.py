def mergesort(L):
    if len(L) <= 1:
        return L
    
    median = len(L) // 2

    A = L[:median]
    B = L[median:]

    A = mergesort(A)
    B = mergesort(B)

    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i + j] = A[i]
            i += 1
        else:
            L[i + j] = B[j]
            j += 1
    while i < len(A):
        L[i + j] = A[i]
        i += 1
    while j < len(B):
        L[i + j] = B[j]
        j += 1
    
    return L



L = [3, 5, 1, 0 , 9 , 3, 4]
print(mergesort(L))



def quicksort(L, left = 0, right = None):
    if right is None:
        right = len(L)
    
    if right- left <= 1:
        return None
    
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
    
    quicksort(L, left, pivot)
    quicksort(L, pivot+1, right)