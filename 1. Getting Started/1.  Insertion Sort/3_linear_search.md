# Exercicse  3
**INPUT**: A sequence of n numbers *[a1, a2, . . . , an]* stored in the array *A[0:n]* and a value *x*.

**OUTPUT**: An index *i* such that *x* equals *A[i]* or the special value *None* if *x* does not appear in A.

```python
def linear_search(a, x):
    for i in range(len(a)):
        if (a[i] == x):
            return i
    return None
```

#### Loop Invariant

At the start of the *i*-th iteration of the loop, there is no element in the subarray A[0:i-1] that is equal to *x*.

#### Initialization

+ Before the first iteration:
    + `i - 1 == 0` 
    + the subarray `a[0:0]` is empty
    + there is no element in the empty arrat that is equal to *x*
    + **Conclusion**: The invariant holds true before the first iteration 

#### Maintenance

+ Assume, the invariant holds before the *k*-th iteration
    + Before the *k*-th iteration of the loop, the subarray a[0:k-1] does not contain the element that is equal to *x*.
    
    + During the *k*-th iteration:
        + we compare the next a[k] element to the value *x*. 
            + If x is equal to the a[k], the algorithm terminates
            + Otherwise x is not equal to the a[k] element and the loop proceeds
    + Before the *k+1*-th iteration:
        + `i-1 == k`
        + x is not equal to any element any element of the a[0:k-1] subarray and is not equal to the a[k] element, so it is not equal to any element in the a[0:k] subarray.
    
    + **Conclusion**: We have shown that invariant is true before the *k*-iteration, implies that invariant is true before the *k+1*-th iteration

#### Termination

The loop variable *i* starts at 0 and increases by 1 in each iteraion. The loop terminates if the a[i] is equal to x or if i exceeds the length of the array.

+ When loop terminates:
    + Case 1: a[i] is equal to x
        + In this case, the index i is returned such that a[i] is equal to x.
    + Case 2: i exceeds the array length
        + `i == n+1`  
        +  And the subarray a[0:n] does not contain the value that is  equal to x
        + The None value is returned
+ **Conclustion**: the invariant insures that upon termination either the index i is returned such that a[i] = x or the None value, if x is not in a.