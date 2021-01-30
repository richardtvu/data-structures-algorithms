# Selection Sort from Chapter 2, p. 35

"""
This selection sort algorithm takes an unsorted list and returns a list sorted 
from least to greatest. 

First, the algorithm creates a new array, which will store the sorted values.
Second, the algorithm will loop through the unsorted list:
    On each iteration, the smallest number will be found.
    The smallest number will be removed from the unsorted list.
    It will then be added to the sorted list.
Third, once there are no more unsorted values, the sorted list will be complete 
and returned. 

This is slightly modified from the original, as I tried to recall it 
and used variable names that made more sense to me. 
""" 

def selection_sort(arr): 
    sorted = [] 
    for i in range (0, len(arr)): 
        smallest = findSmallest(arr)
        sorted.append(arr.pop(smallest))
    return sorted


def findSmallest(arr): 
    least = arr[0]
    least_i = 0
    for i in range(1, len(arr)):
        if arr[i] < least: 
            least = arr[i]
            least_i = i
    return least_i

print(selection_sort([5, 3, 6, 2, 10])) 