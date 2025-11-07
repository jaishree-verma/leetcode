// 2704
// Example 
// Input: func = () => expect(5).toBe(5)
// Output: {"value": true}
// Explanation: 5 === 5 so this expression returns true.
var expect = function(val) {
    return {
        toBe: function(otherVal) {
            if (val === otherVal) return true;
            else throw new Error("Not Equal");
        },
        notToBe: function(otherVal) {
            if (val !== otherVal) return true;
            else throw new Error("Equal");
        }
    };
};