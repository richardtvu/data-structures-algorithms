# 217. Contains Duplicate

## HashSet

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>(); 
        for (int i = 0; i < nums.length; i++){
            if (set.contains(nums[i])) return true; 
            set.add(nums[i]); 
        }
        return false; 
    }
}
```

Iterate through the array, nums. Add the number to a set, unless the number is already in the set. If the number is already in the set, there's a duplicate number. Otherwise, return false if we've iterated through the entire array. 

## Arrays.sort()

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) return true; 
        }
        return false; 
    }
}
```

Sort the numbers in the array, which takes O(n log n) time. For each index `i` in the array: If the the `i`-th value is equal to the previous value (`i-1`), then we've found a duplicate. Otherwise, if we've iterated through the entire array, then there are no duplicates. 

`Arrays.sort()` takes O(n<sup>2</sup>) time when the array is nearly sorted.On average, the time complexity is O(n log n). The `for` loop repeats a constant operation `n-1` times, which is O(n). For really big input, there will be O(n log n + n) steps. Since we drop the non-dominant terms, the **time complexity** for the algorithm is O(n log n) in the average case and O(N<sup>2</sup>) in the worst case. 

The version of Java used in Leetcode is [java 13.0.1](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-). It uses a "Dual Pivot Quicksort" strategy which offers "O(n log(n)) performance" according to the Java [doc for Java 13](https://docs.oracle.com/en/java/javase/13/docs/api/java.base/java/util/Arrays.html#sort(int%5B%5D)) and [Java 8](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#sort-int:A-). 

### Study Questions

1. What is the **time complexity** of the Dual Pivot Quicksort implementation of `Arrays.sort()` in Java 8? 
    - O(N<sup>2</sup>) in the worst case and O(n log n) in the average case. 
2. What is the **space complexity** of the Dual Pivot Quicksort implementation used for `Arrays.sort()` in Java 8? 
    - O(log n), assuming tail-end recursion. 
2. What is the **time complexity** for adding values to a **HashSet**? 
    - On average, `search()` and `insert()` operations in a HashSet or HashMap require O(1) time. 
