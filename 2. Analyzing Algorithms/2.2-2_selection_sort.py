def selection_sort(a):
    for j in range(len(a) - 1):
        smallest_i = j
        for i in range(j+1, len(a)):
            if a[smallest_i] > a[i]:
                smallest_i = i
        a[j], a[smallest_i] = a[smallest_i], a[j]
    return a

a = [10, 9 , 8, 7, 6 , 5 , 4 , 3]
b = [1]
c = [1,1,1,1]
d = [1,2,3,4]
e = []

print(selection_sort(a))
print(selection_sort(b))
print(selection_sort(c))
print(selection_sort(d))
print(selection_sort(e))