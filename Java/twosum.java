// 1
// optimal approach is using Hash Map 
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // create a hash map to store numbers
        Map<Integer,Integer> map = new HashMap<>();
        for ( int i = 0;i<nums.length;i++){
            // calculate remainder of current number
            int remainder = target - nums[i];
            // check if remainder is in hash map already 
            if (map.containsKey(remainder)){
                // if yes return index and current no
                return new int [] {map.get(remainder),i};
            }
            // else add the current no and its index to hash map
            map.put(nums[i],i);
        }
        // return empty array if no solution if found (worst case)
        return new int [] {};
    }
}