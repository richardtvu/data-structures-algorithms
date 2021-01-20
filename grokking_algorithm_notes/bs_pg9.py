# Binary Search from Grokking Algorithms P.9

def binary_search(list, item): 
    lo = 0                  # lo and hi keep track of which part of the list
    hi = len(list)-1        # you'll search in 

    while lo <= hi:         # while you haven't narrowed it down to one element ...
        mid = (lo + hi) // 2 
        guess = list[mid]   # check the middle element 
        if guess == item:   # Found the item.
            return mid
        if guess > item:    # The guess was too high.
            hi = mid - 1      
        else:               # The guess was too low. 
            lo = mid + 1 
    
    return None             # The item doesn't exist 

my_list = [1, 3, 5, 7, 9]   # Test the function 

print(binary_search(my_list, 3)) # => 1 List indices start at 0, 
                                # so the second slot has an index of 1
print(binary_search(my_list, -1)) # => None, the item wasn't found. 
