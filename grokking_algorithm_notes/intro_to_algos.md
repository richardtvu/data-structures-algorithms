# Introduction to Algorithms - Chapter 1

## Learning Goals

- Be able to write a search algorithm from scratch: **binary search**
- Review Big O notation, running time
- Review **recursion**

## Introduction 

Algorithms are concrete, unambigious, and finite collections of steps taken to solve a problem. They help us in many real-world situations, such as:
- Finding the shortest path from your house to the grocery store, e.g. GPS navigators use _graph_ algorithms to map this distance
- Figuring out friends of friends on Facebook, e.g. graphs

### What's important to know about algorithms? 

Each data structure or algorithm has **trade-offs** that make them useful for one situation but inefficient for another. Therefore, knowing these trade-offs will help you select an algorithm that will be suited to your problem. 

### What are some problems that algorithms can help you solve? 

- Making a video game AI
- Making a recommendation system using k-nearest neighbors
- Efficiently approximating solutions to problems using greedy algorithms 

## Binary Search

### What is it? 
It's a much more efficient search than **sequential search**, which is looking at the indexes in an array one by one, which would take O(n) time to find a search value. 

**Binary search** is an algorithm for finding a value in a sorted array in O(log n) time. Basically, you:
1. pick a number in the middle of the array. 
2. If the number is lower than the search value, repeat the search in the upper half of the array. 
3. If the number is higher than the search value, repeat the search in the lower-half of the array. 
4. Repeat steps 2 or 3 until you've: 
    a. found the search value, return the index of that value
    b. searched the last possible spot in the array and didn't find it, return null. 

The difference between O(n) and O(log n) performance is huge! For a list of numbers of size 240,000, it would take up to 240,000 comparisons to find the search value. By contrast, O(log n) performance means it would only take up to 18 comparisons to figure out the location of the search value or say it doesn't exist there. 

What's a requirement/assumption for the binary search? 
- It requires the list be **sorted**, in some order. Otherwise, you can't eliminate half the indexes to search through because the search value might be in _any_ of the indexes. In a randomized list, binary search won't work. 


### The Binary Search Code (Practice/Recall):

```python 
# Binary Search 
def binary_search(list, item): 
    lo = 0
    hi = len(list)-1

    while (lo <= hi):
        mid = (lo+hi) // 2
        guess = list[mid] 
        if guess == item:
            return mid
        if guess > item:
            hi = mid-1
        if guess < item:
            lo = mid+1
    return None
```

### Exercises

#### 1.1 Suppose you have a sorted list of 128 names, and you're searching through it using binary search. What's the maximum number of steps it would take? 

Binary search should take O(log<sub>2</sub>n) steps in the worst case. It should take O(log<sub>2</sub>128) steps, which is 2<sup>steps</sup> = 128. Therefore, the maximum number of steps takenw ould be 7. 

#### 1.2 If you double the size of the list, w at's the maximum number of steps now? 
- If you double the size of the list, then the maximum number of steps goes up by one, to 8. 

#### For 2<sup>n</sup> = steps
| n | steps | 
| 1 | 2 | 
| 2 | 4 | 
| 3 | 8 | 
| 4 | 16 | 
| 5 | 32 | 
| 6 | 64 | 
| 7 | 128 | 
| 8 | 256 | 



### Running Time 

What is **running time**? 
- The number of steps it will take to run an algorithm, which will depend on the size of the input, n. 

What is **linear time**? 
- Taking as many steps to complete an algorithm as there are items in the input. 
- To be more precise, the time it takes to complete an algorithm grows at the same rate as the size of the input. If it takes one second to process a list of one item, then it'll take one million seconds to process a list of one million items. 

What is **logarithmic time** (aka log time)? 
- The time it takes to complete an algorithm will be O(log n), the growth rate of the running time will grow slowly relative to how big n gets. 

## Big O notation

A way of telling you how fast an algorithm is, as the input grows. 

### Why is it important? 

The run time of algorithms differ drastically when the size of the list grows to massive proportions. For instance, a list with a hundred items will take 100 steps for linear time and 7 steps with log<sub>2</sub>n time. That's only about 15x difference in run time. _However_, the run time becomes 1,000,000,000 steps for O(n) where n = 1,000,000,000. By contrast, log n time would take only 32 steps, which is 33 million times faster. U

Understanding Big O allows you to choose the appropriate algorithm as n becomes very large. 

### What does Big O mean? 

It means that in the _worst case_, the algorithm will never take more than the number of steps indicated by the Big O notation. For instance, O(n) means that the algorithm will never take more than n steps to complete. Even if you find what you're looking for in one step, it's still O(n) because it could take n steps in the worst case. 

### What are some Big O run times? 
- O(log n) - log time, e.g. binary search
- O(n) - linear time, e.g. sequential search
- O(n log n) - e.g. quicksort
- O(n<sup>2</sup>) - exponential time, e.g. selection sort
- O(n!) - factorial time, super slow

![Visual from Grokking Algos](\images\o-runtimes-chapter-1-visual.png)