// Question 4.  JavaScript
function weird(x) { 
    var tmp = 3; 
    return function (y) { 
        return x + y + ++tmp; 
    } 
} 
var funny = weird(2); 
var final_answer = funny(10);
// What is the value of final_answer at the end of this snippet ? Please explain your answer

// Answer of the above code is : ----------- 16 when wired(2) is called it return another function hence funny store another function which is further called with funny(10) hence the calculation inside inner function return 16
