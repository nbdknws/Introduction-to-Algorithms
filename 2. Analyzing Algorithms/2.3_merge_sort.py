def merge(a, p, q, r):
    left = a[p:q+1]
    right = a[q+1:r+1]
    
    i, j, k = 0, 0, p
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

a = [6, 5, 4, 3, 2, 1]
merge_sort(a, 0, len(a) - 1)
print(a)