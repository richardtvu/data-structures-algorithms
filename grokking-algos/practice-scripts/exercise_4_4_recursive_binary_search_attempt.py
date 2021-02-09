"""
# Recursive Binary Search Algorithm 

4.4. Remember binary search from chapter 1? It’s a divide-and-conquer
algorithm, too. Can you come up with the base case and recursive
case for binary search?

I went beyond the question to try and write the recursive version of the binary search. 

"""

def recursive_bs(list, lo, hi, target): 
    # Base case: There are no elements in the list. 
    if len(list) == 0: 
        return None 
    
    # Recursive case: There is at least one element in the list. 
    mid = (lo + hi) // 2 
    guess = list[mid] 
    if guess == target: 
        return mid 
    elif guess > target: 
        hi = mid-1
    else: # guess < target
        lo = mid+1 

    return recursive_bs(list, lo, hi, target) 



# Test Cases
list_one = [1, 2, 3]
hi = len(list)-1
assert recursive_bs(list_one, 0, hi, 3) == 2, "Should be 2 because target is in index 2"