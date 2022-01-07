# random module
The random module provides access to functions that support many operations. Perhaps the most important thing is that it allows you to generate random numbers.

## When to use it?

Pick a random element from a list, pick a random card from a deck, flip a coin etc. When making your password database more secure or powering a random page feature of your website.


## Randint
If we wanted a random integer, we can use the randint function Randint accepts two parameters: a lowest and a highest number. Generate integers between 1,5. The first value should be less than the second.

import random
print random.randint(0, 5)
This will output either 1, 2, 3, 4 or 5.

## Random
If you want a larger number, you can multiply it.
For example, a random number between 0 and 100:

import random
random.random() * 100

## Choice
Generate a random value from the sequence sequence.
The choice function can often be used for choosing a random element from a list.
random.choice( ['red', 'black', 'green'] ).

import random
myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
random.choice(myList)


## Shuffle
The shuffle function, shuffles the elements in list in place, so they are in a random order.
random.shuffle(list) Example taken from this post on Stackoverflow

from random import shuffle
x = [[i] for i in range(10)]
shuffle(x)
Output:
# print x  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]
# of course your results will vary


## Randrange
Generate a randomly selected element from range(start, stop, step)
random.randrange(start, stop[, step])

import random
for i in range(3):
    print random.randrange(0, 101, 5)

Code Example -------------

import random
import itertools

outcomes = { 'heads':0,
             'tails':0,
             }
sides = outcomes.keys()

for i in range(10000):
    outcomes[ random.choice(sides) ] += 1

print 'Heads:', outcomes['heads']
print 'Tails:', outcomes['tails']


There are only two outcomes allowed, so rather than use numbers and convert them, the words “heads” and “tails” are used with choice().
The results are tabulated in a dictionary using the outcome names as keys.


$ python random_choice.py
Heads: 4984
Tails: 5016





# What is Risk Analysis in Software Testing and how to perform it?
----- # The probability of any unwanted incident is defined as Risk. -----

## In Softwqare Testing, risk analysis is the process of identifying the risks in applications or software that you built and prioritizing them to test.



## Why use Risk Analysis?
In any software, using risk analysis at the beginning of a project highlights the potential problem areas. After knowing about the risk areas, it helps the developers and managers to mitigate the risks. When a test plan has been created, risks involved in testing the product are to be taken into consideration along with the possibility of the damage they may cause to your software along with solutions.


### possible risks

1. Use of new hardware
2. Use of new technology
3. Use of new automation tool
4. The sequence of code
5. Availability of test resources for the application

### certain risks that are unavoidable

1. The time that you allocated for testing

2. A defect leakage due to the complexity or size of the application

3. Urgency from the clients to deliver the project

4. Incomplete requirements

## ^^ Tackle the situation with care ^^

Conduct Risk Assessment review meeting

Use maximum resources to work on high-risk areas

Create a Risk Assessment database for future use

Identify and notice the risk magnitude indicators: high, medium, low.


## what are these risk magnitude indicators?

### High:
  means the effect of the risk would be very high and non-tolerable. The company might face loss.

### Medium: 
it is tolerable but not desirable. The company may suffer financially but there is a limited risk.

### Low:
it is tolerable. There lies little or no external exposure or no financial loss.

## Risk Identification

### Different sets of risks

1. Business Risks: This risk is the most common risk associated with our topic. It is the risk that may come from your company or your customer, not from your project.

2. Testing Risks: You should be well acquainted with the platform you are working on, along with the software testing tools being used.

3. Premature Release Risk: a fair amount of knowledge to analyze the risk associated with releasing unsatisfactory or untested software is required

4. Software Risks: You should be well versed with the risks associated with the software development process.

## The perspective of Risk Assessment
### perspectives of Risk Assessment:

Effect

Cause

Likelihood

Effect – To assess risk by Effect. In case you identify a condition, event or action and try to determine its impact.

Cause – To assess risk by Cause is opposite of by Effect. Initialize scanning the problem and reach to the point that could be the most probable reason behind that.

Likelihood – To assess risk by Likelihood is to say that there is a probability that a requirement won’t be satisfied.


## How to perform Risk Analysis?
### Step:

Searching the risk

Analyzing the impact of each individual risk

Measures for the risk identified





















