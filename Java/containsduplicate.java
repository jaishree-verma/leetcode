// 217

// brute force 
// class Solution:
//     def containsDuplicate(self, nums: List[int]) -> bool:
//         n = len(nums)
//         for i in range(n-1):
//             for j in range(i+1,n):
//                 if (nums[i] == nums[j]):
//                     return True
                
//         return False

// optimal approach is to use hashset

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // create a hash set
        HashSet<Integer>number = new HashSet <>();
        // iterate through element
        for (int num : nums){
            // if no in num then return true
            if (number.contains(num)){
                return true;
            }
            // if not add it to hash map
            number.add(num);
        }
        // if all distinct then retrun false
        return false;
    }
}