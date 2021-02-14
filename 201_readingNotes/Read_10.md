# Read 10


JavaScript Chapter 10 

## Error Handling & Debugging

<ol>
<li> The Console & Dev Tools </li>
Tools built into the browser that helps you hunt for errors.
<ul>
<li> Order of execution </li>
To find the source of an error, it helps to know how scripts are processed. The order in which statements are executed can be complex; some tasks cannot complete until another statement or functions has been run:

<li> Execution Contexts </li>
The JavaScript interpreter uses the concept of execution contexts. There is one global execution contexts; plus, each function creates a new execution context. They correspond to variable scope.

<li> The Stack </li>
The JavaScript interpreter processes one line of code at a time. When a statement needs data from another function, it stacks (or piles) the new function on top of the current task. 

<li> Execution Context & Hoisting </li>
Each time a script enters a new execution context, there are two phases of activity.
<ol>
<li> Prepare </li>
The new scope is created
Variables, functions, and arguments are created
<li> Execute </li>
now it can assign values to variables
reference functions and run their code
execute statements
</ol>
</ul>

<li> Common Problems </li>
Common sources of errors, and how to solve them.
<ul>
<li> Syntax Error </li>
"syntax is not correct" This is caused by incorrect use of the rules of the language. It is often the result of a simple typo.

<li> Reference Error </li>
"Variable Doesnt Exists" This is caused by a variable that is not declared or is out of scope.

<li> Type Error </li>
"value is unexpected data type" This is often caused by trying to use an object or method that does not exsist.

<li> Range Error</li>
"Number Outside of Range" If you call a function using numbers outside of its accepted range.

<li> Eval Error</li>
"Incorrect use of eval() function" The eval() function evaluates text through the interpreter and runs it as code. 

<li> URI Error</li>
"incorrect use of URI functions" If these characters are not escaped in URIs, they will cause an error: / ? & # : ; 

<li> Error </li>
"generic error object" The generic error object is the template or prototype from which all other error objects are created.

<li> NaN </li>
"Not an Error" (note if you perform a mathematical operation using a value that is not a number, you end up with the value of Nan, Not a type error. 
</ul>

<li> Handling Errors </li>
How code can deal with potential errors gracefully.
<ol>

<li> Debug the script to fix errors. </li>
If you come across an error while writing a script (or when someone reports a bug), you will need to debug the code, track down the source of the error, and fix it. Every major modern browser will help you with finding these errors by utilizing the Developer Tools. 

<li> Handle Errors Gracefully </li>
You can handle errors gracefully using try, catch, throw and finally statements. Sometimes an error may occur in the script for a reason beyond your control. for example, you might request data from a third party, and their server may not respond. in such cases, it is particularly important to write error-handling code. 

<li> Debugging WorkFlow </li>
Debugging is about deduction: eliminating potential causes of an error. Try to narrow down where the problem might be, than look for clues. 
<ol>
<li> Where is the problem? </li>
First you should try and narrow down the area where the problem seems to be. 
Look at the error message, and find what it is telling you. 
<li> What exactly is the problem? </li>
Once you think you might know what the rough area is. And where your problem is located, you can then try to find the actual line of code that is causing the error. 
</ol>
</ol>
</ol>
