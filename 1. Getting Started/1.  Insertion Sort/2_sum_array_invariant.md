# Exercicse 2 
**INPUT**: array of numbers *A[1:n]*

**OUTPUT**: the sum of the n numbers in array *A[1:n]*

```python
sum = 0
for i = 1 to n
    sum = sum + A[i]
return sum 
```
#### Loop Invariant

At the start of each iteration of the for loop, the sum variable contains the sum of the first *i−1* elements of the array A.

#### Initialization

+ Before the first iteration:
    + `i == 0` 
    + `sum == 0`
    + According to the loop invariant the `sum` should contain the sum of the first `i - 1 == 1 - 1 == 0` elements
    + The sum of the first 0 elements of the array is indeed 0
    + **Conclusion**: The invariant holds true before the first iteration 

#### Maintenance

+ Assume, the invariant holds before the *k*-th iteration
    + Before the *k*-th iteration of the loop, the `sum` variables contains the sum of the first *k-1* elements of the array A.
    
    + During the *k*-th iteration:
        + the A[k] element is added to the `sum` variable
        + So now the `sum` contains the sum of the first *k* elements
    + Before the *k+1*-th iteration:
        + the `i-1 == k` and the `sum` contains the sum of the first k elements of the array A
    + **Conclusion**: We have shown that invariant is true before the *k*-iteration, implies that invariant is true before the *k+1*-th iteration

#### Termination

The loop variable *i* starts at 1 and increases by 1 in each iteraion, once *i* exceeds n, loop terminates. 

+ When loop terminates:
     + `i == n+1`  
     + At this moment the `sum` variable contains the sum of the first `(i-1) == n` elements of the array.
+ **Conclustion**: the invariant insures that upon termination the `sum` conatains the sum of all n elements of the array.