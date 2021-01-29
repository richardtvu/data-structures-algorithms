# Takes in a list and the current max, which starts at the smallest negative number. 
def max(list, currMax):
    # If the list is empty, then the max of that list is 0. 
    if len(list) == 0: 
        return currMax
    # If the list has only one element and it's greater than the current max, then that element is the current max. 
    if len(list) == 1:
        if list[0] > currMax: 
            return list[0]
        return currMax
       
    # If the list has more than one element, then max is the max between the first element in the list and the current maximum for the list. 
    if list[0] > currMax:
        return max(list[1:len(list)], list[0])
    
    return max(list[1:len(list)], currMax)

list = [2, 4, 6]
list_two = [1, 5, 123, 1, 22, -102, 154]
list_three = [] 
list_four = [-11]
smallest_int = sys
maxNumber = max(list, 0) # should return 6
print(maxNumber)

maxNumber = max(list_two, 0) # should return 154
print(maxNumber)

maxNumber = max(list_three, 0) # should return 0
print(maxNumber)

maxNumber = max(list_four, 0) # should return -11
print(maxNumber)