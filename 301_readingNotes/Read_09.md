# Reading 09 
Concepts of Functional Programming in Javascript

What is functional programming?
Functional programming is a programming paradigm — a style of building the structure and elements of computer programs — that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data — Wikipedia

So how do we know if a function is pure or not? 

It returns the same result if given the same arguments (it is also referred as deterministic)
It does not cause any observable side effects

It returns the same result if given the same arguments
Imagine we want to implement a function that calculates the area of a circle. An impure function would receive radius as the parameter, and then calculate radius * radius * PI:

/////////////////////// EXCERT FROM READING MEDIUM.COM
let PI = 3.14;

const calculateArea = (radius) => radius * radius * PI;

calculateArea(10); // returns 314.0
//////////////////////
