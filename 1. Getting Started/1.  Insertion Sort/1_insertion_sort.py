class InsertionSort:
    def sort(self, a, direction = "asc"):
        if direction == "asc":
            return self._insertion_sort_asc(a)
        elif direction == "desc":
            return self._insertion_sort_desc(a)
        else:
            return ValueError("Invalid direction. Possible values are: asc, desc")
        
    def _insertion_sort_asc(self, A):
        for i in range(1,len(A)):
            key = A[i]
            j = i - 1 
            while (j >= 0) and (A[j] > key):
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        return A
    
    def _insertion_sort_desc(self, A):
        for i in range(1,len(A)):
            key = A[i]
            j = i - 1
            while (j >= 0) and (A[j] < key):
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key
        return A


a = [10,9,8,7,6,5,4,3,2,1]
b = [1,2,3,4,5,6]

sorter = InsertionSort()
print(sorter.sort(a))
print(sorter.sort(b, "desc"))