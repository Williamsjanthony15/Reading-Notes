# Read 10

## In Asynchronous JavaScript, we have a callback function, an event loop, and a task queue. The callback function is acted upon by the call stack during execution after the call back function has been pushed to the stack by the event loop.

## What is a Call Stack?
At the most basic level, a call stack is a data structure that uses the **Last In, First Out (LIFO)* principle to temporarily store and manage function invocation (call)

What is **Last In, First Out*? 
LIFO: When we say that the call stack, operates by the data structure principle of Last In, First Out, it means that the last function that gets pushed into the stack is the first to be pop out, when the function returns.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*Example*
function firstFunction(){
  throw new Error('Stack Trace Error');
}

function secondFunction(){
  firstFunction();
}

function thirdFunction(){
  secondFunction();
}

thirdFunction();
*Example*

When the code is run, we get an error. A stack is printed showing how the functions are stack on top each other. Take a look at the diagram.


Stack trace error
You will notice that the arrangement of the functions as a stack begins with the firstFunction() (which is the last function that got into the stack, and is popped out to throw the error), followed by the secondFunction(), and then the thirdFunction() (which is the first function that gets pushed into the stack when the code is executed).

Temporarily store: When a function is invoked (called), the function, its parameters, and variables are pushed into the call stack to form a stack frame. This stack frame is a memory location in the stack. The memory is cleared when the function returns as it is pop out of the stack.


Image Credit: CMU
Manage function invocation (call): The call stack maintains a record of the position of each stack frame. It knows the next function to be executed (and will remove it after execution). This is what makes code execution in JavaScript synchronous.

Think of yourself standing on a queue, in a grocery store cash point. You can only be attended to after the person in front of you have been attended to. That’s synchronous.

This is what we mean by “manage function invocation”.

------------------------------------------ Section above taken directly from https://www.freecodecamp.org/news/understanding-the-javascript-call-stack-861e41ae61d4/ ----------
