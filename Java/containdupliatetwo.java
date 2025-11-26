// 219

// brute force 

// class Solution:
//     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
//         n = len(nums)
//         for i in range(n-1):
//             for j in range(i+1,n):
//                 if (nums[i] == nums[j] and abs(i-j)<=k):
//                     return True
//         return False

// optimise would be to do with hash map or hash set 

class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set <Integer> set = new HashSet<>();
        for (int i = 0;i<nums.length;++i){
            if(set.contains(nums[i])) return true;
            set.add(nums[i]);
            if (set.size()>k){
                set.remove(nums[i-k]);
            }
        }
        return false;
    }
}