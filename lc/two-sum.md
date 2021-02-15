# Two Sum


## Solution

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