# Insertion Sort Notes

What steps does insertion sort consist of? Here's what I recall: 
1. Store the value at index 1, i, in a temp variable, temp, so that the array will have free space to shift the position of elements. 
2. Compare the value in the temp variable with the index to the left of it, which we'll call _pos_, and is 0 to begin with.  
    - If the 0-th value is less than the 1-th value, then move the 0th value to the 1-th index, e.g. arr[1] = arr[0]
    - Since the 0-th index is the last element to check against the temp variable, we've found the place for our temp value. Insert it there. arr[pos+1] = arr[pos]. 
3. Increment i. Repeat the process of storing the i-th value in a temp variable. 
4. Set pos to be i-1, to start comparing the temp value with the value to the left of it. 
5. If the pos-th value is greater than the temp value, then shift its index one to the right. Then, decrement pos to compare the temp value with the next element to the left.
6. Repeat step #5  until a smaller value is found _or_ the pos has an index of -1, indicating there are no more values to compare the temp value to. In that case, insert the temp value into the pos+1-th index, which would be one to the right of the smaller value or the beginning of the array if there are no more values to compare. 

 What are the insertion sort steps according to Wengrow (2020, p. 79-80)? 

 