# Insertion Sort from p. 85 of Wengrow (2020). 

def insertion_sort(arr): 
    for i in range(1, len(arr)):
        temp = arr[i]
        position = i - 1 # The position, index to compare. 
        
        while position >= 0:         # While there are indices to check
            if arr[position] > temp: # If the number in that index is greater than the temp variable
                arr[position + 1] = arr[position] # Move that number to the right by one. 
                position = position - 1 # Move the position pointer to the left by one. 
            else: # The numbers remaining are already sorted. 
                break 
        
        arr[position + 1] = temp # Insert the temp variable we inititally took out
    
    return arr

