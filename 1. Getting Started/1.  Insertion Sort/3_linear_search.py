# Finds only the first index
def linear_search(a, x):
    for i in range(len(a)):
        if (a[i] == x):
            return i
    return None

# Finds all indexes
def linear_search_many(a, x):
    i = 0
    indexes = []
    while (i < len(a)):
        if (a[i] == x):
            indexes.append(i)
        i += 1
    return indexes

a = [5, 10 , 21, 300, 43, 41 , 1 , -100, 0, 21]
x1 = 21
x2 = -45

print(linear_search(a, x1))
print(linear_search(a, x2))
print(linear_search_many(a, x1))