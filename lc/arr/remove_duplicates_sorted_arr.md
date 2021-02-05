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

> Since the array is already sorted, we can keep two pointers iii and jjj, where iii is the slow-runner while jjj is the fast-runner. As long as nums[i]=nums[j]nums[i] = nums[j]nums[i]=nums[j], we increment jjj to skip the duplicate.
> When we encounter nums[j]≠nums[i]nums[j] \neq nums[i]nums[j]​=nums[i], the duplicate run has ended so we must copy its value to nums[i+1]nums[i + 1]nums[i+1]. iii is then incremented and we repeat the same process again until jjj reaches the end of array.

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

    Time complextiy : O(n). Assume that n is the length of array. Each of i and j traverses at most n steps.

    Space complexity : O(1)

What does this mean? How does it work? 