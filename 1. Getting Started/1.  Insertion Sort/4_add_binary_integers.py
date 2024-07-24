# INPUT: two arrays A[0:n-1] and B[0:n-1] such that each element in A and B is either 0 or 1
# OUTPUT: C[0:n] that store the sum c = a + b of two binary integers a and b, where a = SUM(i=0 to n-1)(A[i]*2^i) and b = SUM(i=0 to n-1)(B[i]*2^i) 

def add_binary_integers(A, B):
    C = [0 for x in range(len(A) + 1)]
    acc = 0
    for i in range(len(A)):
        sum = A[i] + B[i] + acc
        C[i] = sum % 2
        acc = 0 if sum  < 2 else 1
    C[len(A)] = acc
    return  C

A = [1, 1, 1, 0, 1, 1]
B = [1, 1, 1, 0, 0, 1]
print(add_binary_integers(A, B))