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

`Arrays.sort()` takes O(n<sup>2</sup>) time when the size of the array is 10 or less because insertion sort is used. However, arrays with more than 10 items require O(n log n) time to sort. The `for` loop repeats a constant operation `n-1` times, which is O(n). For really big input, there will be O(n log n + n) steps. Since we drop the non-dominant terms, the **time complexity** for the algorithm is O(n log n). 

The version of Java used in Leetcode is [java 13.0.1](https://support.leetcode.com/hc/en-us/articles/360011833974-What-are-the-environments-for-the-programming-languages-). It uses a "Dual Pivot Quicksort" strategy which offers "O(n log(n)) performance" according to the Java [doc for Java 13](https://docs.oracle.com/en/java/javase/13/docs/api/java.base/java/util/Arrays.html#sort(int%5B%5D)) and [Java 8](https://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#sort-int:A-). 