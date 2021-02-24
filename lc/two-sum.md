# Two Sum

This is the solution for the Two Sum problem from LeetCode, with some modifications to make it more readable for my purposes. 

## 1. Brute Force

Add each possible pair and return the pair whose sum is equal to the target. 

```java
public int[] twoSum(int[] nums, int target) {
    int sum; 
    for (int i = 0; i < nums.length; i++) {
        for (int j = 0; j < nums.length; j++) {
            sum = nums[i] + nums[j]; 
            if ( sum == target && i != j) {
                return new int[]{i, j}; 
            }
        }
    }
    return new int[]{};
}
```

Time complexity: O(n<sup>2</sup>). The inner for-loop repeats an O(1) operation, N, times. The outer for-loop repeats the inner for-loop N times. Therefore, the performance is O(N<sup>2</sup>). 

Space complexity: O(1). A variable is initialized, which takes constant space. And a int[] is initialized too. 

## 2. Two-pass Hash Table

```java
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>(); 
    
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }

    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i]; 
        if (map.containsKey(complement) && map.get(complement != i)) {
            return new int[]{i, map.get(complement)}; 
        }    
    }

    throw new IllegalArgumentException("No two sum solution"); 
}
```

## 3. Single-pass Hash Table

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int complement; // complement = target - nums[i]; 
        Map<Integer, Integer> map = new HashMap<>(); // <complement, index of complement>
        for (int i = 0; i < nums.length; i++) {
            complement = target - nums[i]; 
            if (map.containsKey(complement)) {
                int j = map.get(complement); // index of complement
                return new int[]{i, j};  
            }
            map.put(nums[i], i); // Save the current value and its index to the hash map. 
        }
        
        return new int[]{}; 
    }
}
```

## Study Questions 

Assuming that the context for the question is included: 
1. What does the **brute force solution** involve? 
2. How would you use a **two-pass** hash table to solve this question? 
3. How would you use a **single-pass** hash table to solve this problem?
4. (include code for single-pass solution). 
    - What is the time complexity for this solution? 
    - What is the space complexity?
    - What is the **trade-off** for the solution compared to a brute force solution? 
5. How would you make the **two-pass** solution more efficient? 
