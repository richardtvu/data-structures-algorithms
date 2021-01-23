# Binary Search Implementation
"""
The binary search takes as input a **sorted** list and a search value.
It uses two pointers, lo and hi, to keep track of the locations to check
for the item. On each iteration, the binary search algorithm
will check the middle value, i.e. the average of lo and hi divided by 2.

WHILE there are elements to check: 
    If the guess matches the item, then we return the index where of the guess. 
    If the guess is greater than the item, then we can eliminate the top
    half of the locations, i.e. set the hi pointer to mid - 1.
    Else, the guess is lower than the item, so eliminate the bottom half to
    search through: Set the lo pointer to mid + 1.

Once the while loop ends, there are no elements left to check, so just return
that we didn't find the item in our list. 
"""
def binary_search(list, item):
    lo = 0
    hi = len(list)-1

    while (lo<=hi):
        mid = (lo+hi)//2
        guess =list[mid]
        if guess == item:
            return mid
        if guess > item:
            hi = mid+1
        else:
            lo = mid-1

    return None
    
