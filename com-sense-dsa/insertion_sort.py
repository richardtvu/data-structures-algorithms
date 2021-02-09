# Insertion Sort from p. 85 of Wengrow (2020). 

"""
Pseudocode: 
# For each index, starting at 1:
    # Save the value of the i-th index in a temporary variable
    # The position for the first value to compare against the temp variable is i-1
    # While the position still represents a valid index: 
        # If the element in that position is greater than the temp value:
            # Shift that element one index to the right
            # Shift the position index one to the left 
            # Move the position pointer to the left by one. 
        # Else the element is less than the temp value
            # Prepare to insert the temp value back into the array
    # # Insert the temp value into the empty spot where it belongs
# Return the sorted array
""" 


def insertion_sort(arr): 
    for i in range(1, len(arr)):
        temp = arr[i]    
        position = i - 1 

        while position >= 0:
            if arr[position] > temp:
                arr[position + 1] = arr[position] 
                position = position - 1 
            else: 
                break 

        arr[position + 1] = temp 
    
    return arr

