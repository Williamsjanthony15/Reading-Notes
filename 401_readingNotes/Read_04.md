# READ 4

## Classes and Objects
Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class.

## accessing Object Functions
To access a function inside of an object you use notation similar to accessing a variable:

# Naive Recursion is Naive

## fibonacci 
fibonacci numbers were originally deﬁned by the Italian mathematician Fibonacci in the thirteenth century to model the growth of rabbit populations. Fibonacci surmised that the number of pairs of rabbits born in a given year is equal to the number of pairs of rabbits born in each of the two previous years, starting from one pair of rabbits in the ﬁrst year.

-----Example-------
To count the number of rabbits born in the nth year, he deﬁned the recurrence relation:

Fn = Fn-1 + Fn-2
The base cases are:

F0 = 0 and F1 = 1
Let’s write a recursive function to compute the nth Fibonacci number:

def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
 
>>> fibonacci_recursive(5)
Calculating F(5), Calculating F(4), Calculating F(3), Calculating F(2), Calculating F(1), 
Calculating F(0), Calculating F(1), Calculating F(2), Calculating F(1), Calculating F(0), 
Calculating F(3), Calculating F(2), Calculating F(1), Calculating F(0), Calculating F(1),

5

-----Example-------

Naively following the recursive deﬁnition of the nth Fibonacci number was rather inefficient. As you can see from the output above, we are unnecessarily recomputing values. Let’s try to improve fibonacci_recursive by caching the results of each Fibonacci computation Fk:

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
 
>>> fibonacci_recursive(5)
Calculating F(5), Calculating F(4), Calculating F(3), Calculating F(2), Calculating F(1), Calculating F(0),

5
# Pesky Details

Python doesn’t have support for tail-call elimination. As a result, you can cause a stack overflow if you end up using more stack frames than the default call stack depth:

>>> import sys
>>> sys.getrecursionlimit()
3000


Also, Python’s mutable data structures don’t support structural sharing, so treating them like immutable data structures is going to negatively affect your space and GC (garbage collection) efficiency because you are going to end up unnecessarily copying a lot of mutable objects. For example, I have used this pattern to decompose lists and recurse over them:

>>> input_list = [1, 2, 3]
>>> head = input_list[0]
>>> tail = input_list[1:]
>>> print("head --", head)
head -- 1
>>> print("tail --", tail)
tail -- [2, 3]



