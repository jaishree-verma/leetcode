// // 2619

// Example 
// Input: nums = [null, {}, 3]
// Output: 3
// Explanation: Calling nums.last() should return the last element: 3.

// Example 
// Input: nums = []
// Output: -1
// Explanation: Because there are no elements, return -1.

Array.prototype.last = function() {
  if (this.length === 0) {
    return -1;
  } else {
    return this[this.length - 1];
  }
};