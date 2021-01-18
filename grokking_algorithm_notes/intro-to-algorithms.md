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

## Binary Search?

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


