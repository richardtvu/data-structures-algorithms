# Ankified Insertion Sort

This document will contain variations on Anki cards to test knowledge of insertion sort from p. 84 of Wengrow (2020). 

```py
def insertion_sort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1

        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else: 
                break
        
        array[position + 1] = temp_value
    
    return array 
```

## Variations

```py
# Python: Fill in the blank
def insertion_sort(arr):
    ____________________________
        temp_value = arr[i]
        position = i - 1

        while position >= 0:
            if arr[position] > temp_value:
                arr[position + 1] = arr[position]
                position = position - 1
            else: 
                break
        
        arr[position + 1] = temp_value
    
    return arr 
```
- `for i in range(1, len(arr)):`


```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp_value = ______
        position = i - 1

        while position >= 0:
            if arr[position] > temp_value:
                arr[position + 1] = arr[position]
                position = position - 1
            else: 
                break
        
        arr[position + 1] = temp_value
    
    return arr 
```
- `arr[i]`


```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        _____________
        position = i - 1

        while position >= 0:
            if arr[position] > temp:
                arr[position + 1] = arr[position]
                position = position - 1
            else: 
                break
        
        arr[position + 1] = temp
    
    return arr 
```
- `temp = arr[i]`

```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp_value = arr[i]
        ___________

        while pos >= 0:
            if arr[pos] > temp_value:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            else: 
                break
        
        arr[pos + 1] = temp_value
    
    return arr 
```
- `pos = i - 1`

```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp_value = arr[i]
        pos = ______

        while pos >= 0:
            if arr[pos] > temp_value:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            else: 
                break
        
        arr[pos + 1] = temp_value
    
    return arr 
```
- `i - 1`

```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp_value = arr[i]
        pos = i - 1

        _______________
            if arr[pos] > temp_value:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            else: 
                break
        
        arr[pos + 1] = temp_value
    
    return arr 
```
- `while pos >= 0:`

```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        pos = i - 1

        while pos >= 0:
            ___________________
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            else: 
                break
        
        arr[pos + 1] = temp
    
    return arr 
```
- `if arr[pos] > temp:`


```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        pos = i - 1

        while pos >= 0:
            if arr[pos] > temp:
                _______________________
                pos = pos - 1
            else: 
                break
        
        arr[pos + 1] = temp
    
    return arr 
```
- `arr[pos + 1] = arr[pos]`

```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        pos = i - 1

        while pos >= 0:
            if arr[pos] > temp:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            else: 
                break
        
        arr[pos + 1] = temp
    
    return arr 
```


```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        pos = i - 1

        while pos >= 0:
            if arr[pos] > temp:
                arr[pos + 1] = arr[pos]
                _____________
            else: 
                break
        
        arr[pos + 1] = temp
    
    return arr 
```
- `pos = pos - 1`

```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        pos = i - 1

        while pos >= 0:
            if arr[pos] > temp:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            _____ 
                _____
        
        arr[pos + 1] = temp
    
    return arr 
```
- `else: break`


```py
# Python: Fill in the blank
def insertion_sort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        pos = i - 1

        while pos >= 0:
            if arr[pos] > temp:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            else: 
                break
        
        ___________________
    
    return arr 
```

- `arr[pos + 1] = temp`
