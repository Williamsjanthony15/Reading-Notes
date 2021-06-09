# In Tests We Trust — TDD with Python

## Unit Test
Unit tests are some pieces of code to exercise the input, the output and the behaviour of your code.

## Test-Driven Development (TDD) 
Test-Driven Development is a strategy to think (and write!) tests first.

<!-- Example 
def test_should_return_female_when_the_name_is_from_female_gender():
    detector = GenderDetector()
    expected_gender = detector.run(‘Ana’)
    assert expected_gender == ‘female’
    
     -->

     The test file name should follow the same name of module name. For instance, if our module is gender.py, our test name should be test_gender.py. It’s ideal to separate the tests folder from production code (the implementation) and to have something like this:

<!-- 
mymodule/
 — module.py
 — another_folder/
 — — another_module.py
tests/
 — test_module.py
 — another_folder/
 — — test_another_module.py
 -->

Other thing to care about is the structure. A convention widely used is the AAA: Arrange, Act and Assert.
### Arrange: 
  you need to organize the data needed to execute that piece of code (input);
### Act: 
here you will execute the code being tested (exercise the behaviour);
### Assert: 
after executing the code, you will check if the result (output) is the same as you were expecting.

### The Cycle
I hope at this time you didn’t give up of this text because this is an example of an important thing about TDD: the cycle.
The cycle is made by three steps:

🆘 Write a unit test and make it fail (it needs to fail because the feature isn’t there, right? If this test passes, call the Ghostbusters, really)

✅ Write the feature and make the test pass! (you can dance after that)

🔵 Refactor the code — the first version doesn’t need to be the beautiful one (don’t be shy)


## TDD is not about the money/tests
More than any checking, we need to think about our software design first.

<!-- Example

def test_should_return_male_when_the_name_is_from_male_gender():
    detector = GenderDetector()
    expected_gender = detector.run(‘Pedro’)
    assert expected_gender == ‘male’

-->

<!-- 

import requests

def run(self, name):
    result = requests.get('https://api.genderize.io/?name{}'
.format(name))
    return result['gender']
    
 -->

 ## Takeaways
I hope this was fun for you! To remember:
The greatest advantage about TDD is to craft the software design first
Your code will be more reliable: after a change you can run your tests and be in peace
Beginning may be hard — and that’s fine. You just need to practice!


 ---------------   Notes taken from https://code.likeagirl.io/in-tests-we-trust-tdd-with-python-af69f47e6932 --------------


## Remember This Bit. -- Recursion is Important to remember -- 

# Recursion

## What is Recursion? 

- The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive algorithm, certain problems can be solved quite easily.

### A Mathematical Interpretation

Let us consider a problem that a programmer have to determine the sum of first n natural numbers, there are several ways of doing that but the simplest approach is simply add the numbers starting from 1 to n. So the function simply looks like,

<!-- Example
approach(1) – Simply adding one by one

f(n) = 1 + 2 + 3 +……..+ n

but there is another mathematical approach of representing this,

approach(2) – Recursive adding 

f(n) = 1                  n=1

f(n) = n + f(n-1)    n>1

-->

## What is base condition in recursion?

In the recursive program, the solution to the base case is provided and the solution of the bigger problem is expressed in terms of smaller problems. 

