

## Recursion
Recursive functions can be infinite, just like infinite while loops. These often occur when you forget to implement the base case. 
Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.

 EXAMPLE ----- 
What is the result of this code?
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))
8

fib(4) = fib(3) + fib(2) = (fib(2) + fib(1)) + (fib(1) + fib(0)) = ((fib(1) + fib(0)) + 1) + (1 + 1) = ((1+1)+1) + 2 = 3 + 2 => fib(4) = 5
 ------- 




 ## Sets
 Basic uses of sets include membership testing and the elimination of duplicate entries.


Sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function. They share some functionality with lists, such as the use of in to check whether they contain a particular item.
To create an empty set, you must use set(), as {} creates an empty dictionary.

<!-- What is the output of this code?

letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)

Answer -- 1  -->


Sets differ from lists in several ways, but share several list operations such as len.
They are unordered, which means that they can't be indexed.
They cannot contain duplicate elements.
Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
Instead of using append to add to a set, use add.
The method remove removes a specific element from a set; pop removes an arbitrary element.







## Fibonacci -- 

<!-- Not 100% on this concept.  -->

<!-- Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).

num = int(input())

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
for i in range(num):
	print(recur_fibo(i)) -->



# Classes

### Paradigms of programming

  #### imperative 
(using statements, loops, and functions as subroutines),

  #### functional 
(using pure functions, higher-order functions, and recursion).

  #### object-oriented programming (OOP).
(Objects are created using classes, which are actually the focal point of OOP.)


The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the keyword class and an indented block, which contains class methods (which are functions).
Below is an example of a simple class and its objects.

<!-- ------ Example -------
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3) -->

What type of object is a method?
-- Function]

  ### __init__

The __init__ method is the most important method in a class.
This is called when an instance (object) of the class is created, using the class name as a function.

All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self argument to the list for you; you do not need to include it when you call the methods. Within a method definition, self refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.
In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.

<!-- Example

class Cat:
  def__init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = cat("giners", 4)
print(felix.color)
 -->

  
  
  ## Methods

Classes can have other methods defined to add functionality to them.
Remember, that all methods must have self as their first parameter.
These methods are accessed using the same dot syntax as attributes.

<!-- Example 

class Cat:
  def__init__(self, color, legs):
    self.color = color
    self.legs = legs   -->
  def meow(self):
  print("meow")

<!-- felix = cat("giners", 4)
print(felix.color) -->
felix.meow()

<!-- EXAMPLE END -->

Classes can also have class attributes, created by assigning variables within the body of the class. These can be accessed either from instances of the class, or the class itself.


<!-- class Cat:
      legs = 4
      ...
      
      print(felix.legs)
      print(Cat.legs)  -->


## Attributes 

Trying to access an attribute of an instance that isn't defined causes an AttributeError. This also applies when you call an undefined method. IE: using the wrong callback function in render


What error is caused by trying to access unknown attributes
AttributeError


## Inheritance


Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name).
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
To inherit a class from another class, put the superclass name in parentheses after the class name.

<!-- EXAMPLE
  class Animal:
    def __init__(self,name,color):
      self.name = name
      self.color = color

  class Cat(Animal):
    def purr(self):
      print("Purr...")

  class Dog(Animal):
    def bark(self):
      print("woof")

  fido = dog("fido", "brown")
  print(fido.color)
  fido.bark()
 -->

 What code would show a new class Spam inheriting from Egg?

 class Spam(egg):

 A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods, it overrides them.

<!-- 
class Cat:
  def__init__(self, color, legs):
    self.color = color
    self.legs = legs

  def meow(self):
  print("meow")

class Kitten(Cat):
  def meow(self):
    print("rrrrr")

bengal = kitten("Theo", "grey / white")
bengal.meow()

felix = cat("giners", 4)
print(felix.color)
felix.meow() -->


Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.

However, circular inheritance is not possible.

<!-- class A: 
  def method(self):
    print("a method")

class B: 
  def another_method(self):
    print("b method")

class C: 
  def third_method(self):
    print("c method")

c = C()
c.method()
c.another_method()
c.third_method() -->


What is the result of this code?

class A:
  def a(self):
    print(1)
class B(A):
  def a(self):
    print(2)
	
class C(B):
  def c(self):
    print(3)
		
c = C()
c.a()

Answer - 2


The function 
## super 
is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.

<!-- class A:
  def spam(self):
    print(1)

class B:
  def spam(self):
    print(2)
    super().spam()

B().spam()

super().spam() calls the spam method of the superclass. -->

What is the superclass of a class?

answer - The calls it inherits from


