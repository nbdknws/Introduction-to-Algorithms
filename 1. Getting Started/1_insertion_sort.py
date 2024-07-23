def insertion_sort(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i - 1
        while (j >= 0) and (A[j] > key):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


a = [10,9,8,7,6,5,4,3,2,1]
print(insertion_sort(a))
