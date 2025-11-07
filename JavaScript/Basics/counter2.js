// 2665
// Example 
// Input: init = 5, calls = ["increment","reset","decrement"]
// Output: [6,5,4]
// Explanation:
// const counter = createCounter(5);
// counter.increment(); // 6
// counter.reset(); // 5
// counter.decrement(); // 4

var createCounter = function(init) {
    let a= init;
    return {
        increment : function(){
            return ++a;
        },
        decrement : function(){
            return --a;
        },
        reset : function(){
            a = init
            return a;
        }
    }  
};