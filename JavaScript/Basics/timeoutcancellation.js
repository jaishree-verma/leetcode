// // 2715

// Example 
// Input: fn = (x) => x * 5, args = [2], t = 20
// Output: [{"time": 20, "returned": 10}]
// Explanation: 
// const cancelTimeMs = 50;
// const cancelFn = cancellable((x) => x * 5, [2], 20);
// setTimeout(cancelFn, cancelTimeMs);

// The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened after the execution of fn(2) at 20ms.
// Example 
// Input: fn = (x) => x**2, args = [2], t = 100
// Output: []
// Explanation: 
// const cancelTimeMs = 50;
// const cancelFn = cancellable((x) => x**2, [2], 100);
// setTimeout(cancelFn, cancelTimeMs);
// The cancellation was scheduled to occur after a delay of cancelTimeMs (50ms), which happened before the execution of fn(2) at 100ms, resulting in fn(2) never being called.