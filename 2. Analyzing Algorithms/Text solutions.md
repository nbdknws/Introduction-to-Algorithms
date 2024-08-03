# Exercises

**2.2-1** O(n^3/1000 + 100n^2 -100n + 3) = O(n^3)

**2.2-2**  The code itself:

```python
def selection_sort(a):
    for j in range(len(a) - 1):
        smallest_i = j
        for i in range(j+1, len(a)):
            if a[smallest_i] > a[i]:
                smallest_i = i
        a[j], a[smallest_i] = a[smallest_i], a[j]
    return a
```

**The loop invariant**: After the *k*-th iteration of the outer *for* loop, the subarray *a[0:k]* contains the elements from *a* but in the ascending order.

Why we run until the *(n-2)*. At the last step of the algorithm, when j=(n-2), the subarray a[0:n-2] contain the elements from a but in the ascending order, such that a[n-1] is bigger then any element from the a[0:n-2], so the whole array a[0:n-1] is sorted in ascending order.

**Order of growth**: O(n^2)

```python
def selection_sort(a):
    for j in range(len(a) - 1): # n
        smallest_i = j  # (n-1)
        for i in range(j+1, len(a)): # (n(n-1)/2) + 1 
            if a[smallest_i] > a[i]: # (n(n-1)/2)
                smallest_i = i # (n(n-1)/2)
        a[j], a[smallest_i] = a[smallest_i], a[j] # (n-1)
    return a
```

In the final formula, the leasing term will have n^2, so the order of growth is O(n^2)

The best case scenario has the same O as worst case, becasue we alway have to go through the whole array [j:len(a)]

**2.2-3** We consider the linear search from the previous chapter.

On average we need to check (n+1)/2 elements, becasue the expected value of checked elements is (1 + 2 + ... + n)/n 

Worst case is n.

O((n+1)/2) = n - average case

O(n) = n - worst case

**2.2-4**

- Check if array is already sorted
- Add some hardcoded case that will return the array imidiately