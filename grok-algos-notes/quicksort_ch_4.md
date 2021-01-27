# Quicksort Chapter 4

## Learning Goals

- Learn about **divide-and-conquer**
- Learn about **quicksort**

What is _divide and conquer_ (D&C)? 
- A "recursive technique for solving problems". Recursion in this context means that the technique breaks down a problem into smaller problems. Then, it solves these smaller problems. Once it solves the smaller problems, it can solve bigger problems. It repeats this process of solving bigger and bigger problems based on the solutions it came up with for the smaller problems until it finishes solving the entire problem. 

Why is D&C important?
- D&C represents "another tool in your toolbox", so you can ask "'Can I solve this if I use divide and conquer?'". 

What is _quicksort_? 
- A D&C algorithm that lets you sort lists. 

## Divide & conquer 

1. Find the base case; the simplest case. 
2. Divide the problem until it becomes the base case. 

The example that the book gives is kind of mindblowing to me. For instance, using divide and conquer, you can quickly find the largest, even, subdivision of farmland into _square_ plots. That is, you can divide it up until every subdivision of the farmland is a square and every square is the largest square possible given that every subdivision is a square. 

![](images/2021-01-27-06-20-25.png)

You might try the following, which don't work:

![](images/2021-01-27-06-34-18.png)

However, D&C allows you to easily get to the correct answer, which is 80 x 80 m subdivisions: 

![](images/2021-01-27-06-33-18.png)

### How did that work? 
1. First, you find the _simplest_ base case, i.e. what's the easiest problem to solve? 
    - The easiest is a rectangle that turns into _n_ squares when divided by _n_. That is, one side is _n_ as long as the other. For instance, 50m x 25m square has one side 2x as long as the other, so if you divide it into two, you get two squares. 
    ![](images/2021-01-27-06-36-23.png)

2. Break down the problem until it gets to the base case. 
    1. Start with dividing the farmland using the largest boxes you can use. 
    ![](images/2021-01-27-06-37-52.png) becomes
    ![](images/2021-01-27-06-38-28.png), which is 640m x 400m
    2. Repeat that algorithm on the left-over land. The largest square box you can make using this left-over is 400x400, so you get a left-over of 240m x 400m. 
    ![](images/2021-01-27-06-39-42.png)
    3. Repeat the algorithm with 240x400m to get 240m x 160m.  
    ![](images/2021-01-27-06-40-29.png)
    4. Do it again to get 160m x 80m. You've found the base case because 160m is a multiple of 80m! 
    ![](images/2021-01-27-06-41-01.png)
    ![](images/2021-01-27-06-41-08.png)
3. Now, just divide the farm into plots of 80m x 80m to get the biggest square subdivisions of farmland possible. 

### Array Example 

Given an array of numbers, use recursion to add up all the numbers.
e.g. `2 4 6`

- **Base case**: An array of size 0 or 1. 
    - IF the array is size 0, return 0. 
    - ELSE IF the array is size 1, return that element. 
- **Recursive case**: Everything else. 
    - Get the sum of the 1th element and the sum of the rest of the elements. 

If the array has zero elements, return 0. Otherwise, return the sum of the first element plus the sum of the rest of the elements. 

![](images/2021-01-27-06-48-21.png)

![](images/2021-01-27-06-49-28.png)

### Exercises

> 4.1 Write out the code for the earlier `sum` function.

First Attempt
```py
def sum(list): 
    if len(list) == 0:
        return 0

    lastElement = list[len(list)-1]
    smallerList = list[0, len(list)-1]

    return sum(lastElement + sum(smallerList)))
```

> 4.2 Write a recursive function to count the number of items in a list. 

First attempt
```py
def count(list): 
    if len(list) == 0:
        return 0
    smaller_list = list[0, len(list)-1]
    else: 
        return 1 + count(smaller_list)
```

> 4.3 Find the maximum number in a list. 

First attempt
```py
def max(list): 
    if len(list) == 0: 
        return 0
    curr_max= list[0] # The first element in the list
    smaller_list = list[1:len(list)]
    if curr_max < smaller_list_max:
        curr_max = smaller_list_max
    else:
        return curr_max 
```

The sum function was to get a list:
- If the list is empty, return 0.
- Otherwise, the total sum is the first number in the list plus the sum of the rest of the list. 

How would I apply that to find the maximum number in the list? 

Get a list:
- If the list is empty, return 0.
- Else: 
    - The maximum number is the max between the first number in the list and the max number in the rest of the list. 

For [2, 4, 6]... 

max(2, 4, 6 ) ---->  
2, max(4, 6) ---> 6 > 2 --> 6
4, max(6) ------> 6 > 4 --> 6
6, max() ----> 6 > 0 ---> 6
base case: max() is 0 

To make things simpler, make the base case a list with one element.

max(2, 4, 6 ) ---->  6
2, max(4, 6) ---> 6 > 2 --> 6
4, max(6) ------> 6 > 4 --> 6
Base case: max(6) ---> 6 

In other words, the max of a list is the max of its sublists. 

```py
def max(list):
    if len(list) == 1: 
        return list[0] 

# Continue trying to solve 4.3 exercise... writing a recursive function for finding the max. 