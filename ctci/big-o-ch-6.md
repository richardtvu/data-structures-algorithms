# Chapter 6: Big O

## Ankified Examples from the Chapter

### What is the **time** complexity and **space** complexity of this code fragment? 

```java
int sum(int n) { /* Ex. 1*/ 
    if (n <= 0) {
        return 0; 
    }
    return n + sum(n-1); 
}
```

- Time complexity: O(n). I think it is because the conditional `if` takes O(1) time and the return statement is made up of `n + sum(n-1)`, which is broken down into an O(1) operation to retrieve n and then an O(n-1) operation to retrieve (n-1), (n-2)...1 values and add them together. 

- Space complexity: O(n). For each additional n, where n is the size of the number, an additional call is added. Each additional call must maintain space to keep track of current value of _n_. For instance:
    - n = 0, takes one call sum(0)
    - n = 1, takes two calls: sum(1), sum(0)
    - n = 2, takes three calls: sum(2), sum(1), sum(0)
    - n = X, takes x+1 calls: sum(x), sum(x-1), ... sum(0)

- ![](images/2021-02-14-08-51-44.png)


### This function has _n_ total calls. What is the space complexity? Why doesn't it take O(n) space? 

```java
int pairSumSequence(int n) { 
    int sum = 0; 
    for (int i = 0; i < n; i++) {
        sum += pairSum(i, i+1); 
    }
    return sum; 
}

int pairSum(int a, int b) {
    return a + b;
}
```

- O(1). The `pairSum()` function is called about _n_ times. However, the `pairSum()` calls don't exist at the same time. When the `pairSum()` function is called, it performs and returns a calculation before being removed from the call stack. Thus, there is only ever one `pairSum()` call on the call staack at any point in time, for O(1) space. 

### Why is an algorithm that is O(2N) actually O(N)? 

![](images/2021-02-14-09-02-07.png)

- The left fragment is O(n), in that it does two operations per each x. The right fragment is also O(n), but people might think it is O(2n) because it has two `for` loops that each do some operation n times (i.e. O(n+n) = O(2n)). However, if you look at the operations, the total number of operations performed are basically the same, so they're both O(n). 

### Why do you drop the **non-dominant terms** when expressing Big Oh? e.g. O(N<sup>2</sup> + N) => O(N<sup>2</sup>)? 

As the size of the input increases, the **growth** of the N<sup>2</sup> term becomes so large that it dwarfs the smaller term. 

![](images/2021-02-14-09-06-30.png)

### What is **Amortized Time**? 

Amortized time is the idea that an operation that takes O(N) time in the worst case and O(1) in the average case, will average out to O(1) because the worst case will happen less and less. 

- [ ] Check out other resources on **amortized time** because my grasp of this is still loose. It seems like amortized time is basically averaging 



