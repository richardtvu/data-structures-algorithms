# Remove Duplicates from Sorted Array 

https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

## Prompt 

> Given a sorted array _nums_, remove the duplicates _in-place_ such that each element appears only _once_ and returns the new length. 
> 
> Do not allocate extra space for another array, you must do this by **modifying the input array in-place with O(1) extra memory.**
> 
> **Clarification**: 
> 
> Confused why the returned value is an integer but your answer is an array? 
> 
> Note that the input array is passed in by **reference**, which means a modification to the input array will be known to the caller as well. 
> 
> Internally you can think of this: 

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

> **Example 1**: 

```
**Input:**          nums = [1, 1, 2]
**Output:**         2, nums = [1, 2] 
**Explanation:**    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
```

> **Example 2**:
```
**Input:** nums = [0,0,1,1,1,2,2,3,3,4]
**Output**: 5, nums = [0,1,2,3,4]
**Explanation**: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
```

> **Constraints**:

- `0 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in ascending order.


## Preliminary Thoughts 

The list can be up 30_000 numbers, although it might just have no numbers. The numbers can range from negative ten thousand to positive ten thousand. The list is sorted from least to greatest. 

Well, the base case is an empty list or a list with only one element. If it is empty or has only one element, then just return the current length and the list. 

Otherwise, there can be 2 elements. If the 1st element is equal to the 2nd, then remove the 2nd element and subtract one from the list length. Then return the list length and the list. Else, return the current list and list length. 

If there are 3 elements, then check the first against the second. If they aren't equal, do nothing. Move on to compare the 2nd and third. If they are equal, pop the third element and subtract one from the list length. 

For every element in the list, check if it is equal to the next element. If it is, then remove the next element from the list. Return the len(arr). 
```python 
def removeDuplicates(arr):
    # Base Case
    if len(arr) < 2:
        return len(arr)
    # Iterative Case: 
    for i in range(len(arr)): 
        if i+1 < len(arr) and arr[i] == arr[i+1]:
            arr.pop(i+1) # Remove the duplicate value. 
    return len(arr)
```

### Accepted Submission

```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = nums
        # Base Case
        if len(arr) < 2:
            return len(arr)
        # Iterative Case: 
        i = 0
        while ( i < len(arr)): 
            if i+1 < len(arr) and arr[i] == arr[i+1]:
                # print("i:", i, "i+1:", i+1)
                # print("arr: ", *arr)
                arr.pop(i) # Remove the duplicate value. 
                i = i -1
            i = i+1
        return len(arr)
        
```

### Revisiting Problem 

The hint #2 says that we ought to use a two-pointer approach. 

So... pointer #1 would be uniqueI. 
Pointer #2 would be currI. 

### Solution
https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/

> Since the array is already sorted, we can keep two points _i_ and _j_, where _i_ is the slow-runner while _j_ is the fast-runner. As long as _nums[j] != nums[i]_, we increment j to skip the duplicate. 
>
> When we encounter _nums[j] != nums[i]_, the duplicate run has ended so we must copy its value to _nums[i+1]_. _i_ is then incremented and we repeat the same process again until _j_ reaches the end of the array.

```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```

> Complexity analysis
> - Time complexity: _O(n)_. Assume that _n_ is the length of array. Each of _i_ and _j_ traverses at most _n_ steps. 
> - Space complexity: _O(1)_. 

### Trying to Grok the Explanation 

Why didn't the solution involve actually removing elements from the array and instead just shifting elements to the end? 
- While the question _did_ ask you to remove the duplicates, it also said that you should return the first 

# Continue expanding explanation for why we're not actually removing the elements... 

Why is having two pointers, _i_ and _j_ important? 
- Using two pointers will help us keep track of when a number is unique, with the _i_-th pointer, or if the number is a duplicate, with the _j_-th pointer. 

What is `removeDuplicates()` supposed to do? 
- `removeDuplicates()` should return the length of the array if there were no duplicates. 

How does `removeDuplicates()` determine the number of unique elements? 
1. `removeDuplicates()` takes in an array of integers, `nums`
2. Check for the base case: If the `nums` has no elements, then return 0. 
    - Duplicates require that there by two of the same elements. Since there are no elements, there cannot be duplicates. 
3. 


### What would the solution look like if it were converted to Python?

> Java Solution: 

```java
public int removeDuplicates(int[] nums) {
    if (nums.length == 0) return 0;
    int i = 0;
    for (int j = 1; j < nums.length; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
```

Python Attempt? 

```python 
def removeDuplicates(self, nums: List[int]) -> int: 
    # An empty list cannot have duplicates, as duplicates require a list to have two of the same element. 
    if len(nums) == 0: 
        return 0
    i = 0 
    for j in range(1, len(nums)): 
        if nums[j] != nums[i]: 
            i += 1
            nums[i] = nums[j] 
    
    return i + 1
```