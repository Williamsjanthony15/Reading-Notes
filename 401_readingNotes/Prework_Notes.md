

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


## Magic methods 
are special methods which have double underscores at the beginning and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__, but there are several others.
They are used to create functionality that can't be represented as a normal method.

One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +.


## Magic Methods

More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.


## Magic Methods


Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.

## Magic Methods


There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.





# Object Lifecycle


The lifecycle of an object is made up of its creation, manipulation, and destruction.

The first stage of the life-cycle of an object is the definition of the class to which it belongs.

The next stage is the instantiation of an instance, when __init__ is called. Memory is allocated to store the instance. 

Just before this occurs, the __new__ method of the class is called. This is usually overridden only in special cases.

After this has happened, the object is ready to be used.

Other code can then interact with the object, by calling functions on it and accessing its attributes.
Eventually, it will finish being used, and can be destroyed.

When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes.
Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object.
If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted.

In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well.

The del statement reduces the reference count of an object by one, and this often leads to its deletion.

The magic method for the del statement is __del__.

The process of deleting objects when they are no longer needed is called garbage collection.
In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python automatically deletes it.


## Data Hiding


A key part of object-oriented programming is encapsulation, which involves packaging of related variables and functions into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of a class should be hidden, and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here", meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no ways of enforcing a method or attribute be strictly private.

Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them.
Its only actual effect is that from module_name import * won't import variables that start with a single underscore.

Strongly private methods and attributes have a double underscore at the beginning of their names. This causes their names to be mangled, which means that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.


## Class Methods


Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self parameter of the method.
Class methods are different - they are called by a class, which is passed to the cls parameter of the method.
A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.
Class methods are marked with a classmethod decorator.


class Rectangle: 
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length,side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

new_square is a class method and is called on the class, rather than on an instance of the class. It returns a new object of the class cls.


Fille in the blanks to make sayHi() a class method. 
<!-- class Person:

  def __init__(self, name):

    self.name = name -->

    @classmethod  
     def   <!-- sayHi(cls):

    print("Hi") -->


## Static Methods


Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
They are marked with the staticmethod decorator.

Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.


## Properties

Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
One common use of a property is to make an attribute read-only.

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @property
  def pineapple_allowed(self):
    return False

pizza = pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True



class Person:

  def __init__(self, age):
    self.age = int(age)

  def isAdult(self):
    @property
    if self.age > 18:
      return True
    else: 
      return False



## Properties


Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.



## a simple game

Object-orientation is very useful when managing different objects and their relations. That is especially useful when you are developing games with different characters and features.

Let's look at an example project that shows how classes are used in game development.
The game to be developed is an old fashioned text-based adventure game.
Below is the function handling input and simple parsing.


def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

while True:
  get_input()

  <!-- The code above takes input from the user, and tries to match the first word with a command in verb_dict. If a match is found, the corresponding function is called. -->


  <!-- what does the split method called on the input do?

  divides the input into seperate words. -->
<!-- 
The next step is to use classes to represent game objects. -->
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)
PY
<!-- We created a Goblin class, which inherits from the GameObjects class.
We also created a new function examine, which returns the objects description.
Now we can add a new "examine" verb to our dictionary and try it out! -->
verb_dict = {
  "say": say,
  "examine": examine,
}
PY
<!-- Combine this code with the one in our previous example, and run the program. -->
>>>
: say Hello!
You said "Hello!"

: examine goblin
goblin
A foul creature

: examine elf
There is no elf here.
:
<!-- Combine this code with the one in our previous example, and run the program. -->

<!-- 
This code adds more detail to the Goblin class and allows you to fight goblins. -->


class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg


why was desc turned into a property?

So it could be dynamically created when accessed


## REGEX 

Regular expressions are a powerful tool for various kinds of string manipulation.
They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string (such as changing all American spellings to British ones).
Domain specific languages are highly specialized mini programming languages.
Regular expressions are a popular example, and SQL (for database manipulation) is another.
Private domain-specific languages are often used for specific industrial purposes.

Regular expressions in Python can be accessed using the re module, which is part of the standard library.
After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
If it does, match returns an object representing the match, if not, it returns None.
To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
Raw strings don't escape anything, which makes use of regular expressions easier.

------EXAMPLE---------

import re
pattern = r"spam"

if re.match(pattern, "spamsamspam"):
  print("match")
else:
  print("no match")

--------EXAMPLE--------
  The above example checks if the pattern "spam" matches the string and prints "Match" if it does.
Here the pattern is a simple word, but there are various characters, which would have special meaning when they are used in a regular expression.

Other functions to match patterns are re.search and re.findall.
The function re.search finds a match of a pattern anywhere in the string.
The function re.findall returns a list of all substrings that match a pattern.

-------EXAMPLE-------
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
  print ("match")
else 
  print ("no match")

if re.search(pattern, "eggspamsausagesoam"):
  print("match")
else
  print("no match")

print(re.findall(pattern, "eggspamsausagespam"))
-------EXAMPLE-------

In the example above, the match function did not match the pattern, as it looks at the beginning of the string.
The search function found a match in the string.
The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.


## REGEX SEARCH

The regex search returns an object with several methods that give details about it.
These methods include group which returns the string matched, start and end which return the start and ending positions of the first match, and span which returns the start and end positions of the first match as a tuple.

-----Example------
import re
pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
  print(match.group())
  print(match.start())
  print(match.end())
  print(match.span())

  ## Search and Replace

  One of the most important re methods that use regular expressions is SUB.
  ----Example----
  re.sub(pattern, repl, string, count=0)
  ---Example----

  this method replaces all occurences of the pattern in string with repl, substituting all occurences, unless count provided. this method returns the modified string. 

  ------example------
  import re

  str = "my name is David. Hi David"
  pattern = r"david"
  newstr = re.sub(pattern, "amy", str)
  print (newstr)

  ## MetaCharecters

  Metacharacters are what make regular expressions more powerful than normal string methods.
They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a literal metacharacter, such as "$". You can do this by escaping the metacharacters by putting a backslash in front of them.
However, this can cause problems, since backslashes also have an escaping function in normal Python strings. This can mean putting three or four backslashes in a row to do all the escaping.


** To avoid this, you can use a raw string, which is a normal string with an "r" in front of it. We saw usage of raw strings in the previous lesson. ** 

The first metacharecter .(dot)

this matches any charecter, other than a new line
  
  ----example----


import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
  print("match 1")

if re.match(pattern, "gray"):
  print("match 2")

if re.match(pattern, "blue"):
  print("match 3")

  ----example----

  A "...." would match any four charecter string with no newlines.

  The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.

----example-----

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
  print("match 1")

if re.match(pattern, "gray"):
  print("match 2")

if re.match(pattern, "stingray"):
  print("match 3")

  ----example-----

The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline, and end with y.


Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.

----example-----

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
  print("match 1")

if re.search(pattern, "qwertyuiop"):
  print("match 2")

if re.match(pattern, "rhythm myths"):
  print("match 3")

  ----example-----

## Charecter Classes

  The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

  [abc][def] would match any letter out of "abc", then any letter out of "def"


  Character classes can also match ranges of characters.
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.

----example-----

import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "ls8"):
  print("match 1")

if re.search(pattern, "e3"):
  print("match 2")

if re.match(pattern, "lab"):
  print("match 3")

  ----example-----

  The pattern in the example above matches strings that contain two alphabetic uppercase letters followed by a digit.

### question 
what would [1-5][0-9] match? 
Any two-digit number from 10 to 59. 

## Invert Charecter classes
Place a ^ at the start of a character class to invert it.
This causes it to match any character other than the ones included.
Other metacharacters such as $ and ., have no meaning within character classes.
The metacharacter ^ has no meaning unless it is the first character in a class.

**The pattern [^A-Z] excludes uppercase strings.
Note, that the ^ should be inside the brackets to invert the character class.**


## More Metacharacters

Some more metacharacters are * + ? { and }.
These specify numbers of repetitions.
The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses.


-------EXAMPLE-------
import re

pattern = r"egg(spam)*"

if re.match(patterm, "egg"):
  print ("match")
else 
  print ("no match")

if re.search(pattern, "eggspamspamegg"):
  print("match")
else
  print("no match")

print(re.findall(pattern, "spam"))
-------EXAMPLE-------

[a^]* would match zero or more repetitions of "a" or "^"


The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".

-------EXAMPLE-------
import re

pattern = r"g+"

if re.match(patterm, "g"):
  print ("match")

if re.match(pattern, "ggggggggg):
  print("match")

if re.match(pattern, "abc"):
  print("match")

-------EXAMPLE-------

To summarize:
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.

The metacharacter ? means "zero or one repetitions".


## Curly Braces


Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something".
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
Example:

import re
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
  print("match 2")

if re.match(pattern, "999"):
  print("match 2")

if re.match(pattern, "9999"):
  print("match 3")

"9{1,3}$" matches string that have 1 to 3 nines.

## Groups
A group can be created by surrounding part of a regular expression with parentheses.
This means that a group can be given as an argument to metacharacters such as * and ?.

The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.

As you can see from the example above, groups can be nested.

What would group(3) be of a match of 1(23)(4(56)78)9(0)?

-- 56

There are several kinds of special groups.
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.


import re pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
  print(match.group("first"))
  print(match.group())



## metacharacter

### | = or
  Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue".

## Special Sequences


There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character.
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.

------example------
import re
pattern =r"(.+) \1"

match = re.match(pattern, "word word")
if match: print ("match 1")

match = re.match(pattern, "?! ?!")
if match:
  print ("match 2")

match = re.match(pattern, "abc cde")
if match: 
  print ("match 3")
------example-------

Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.



More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively.
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.

------example------
import re
pattern =r"(\D+\d)"

match = re.match(pattern, "hi 999!")
if match: print ("match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
  print ("match 2")

match = re.match(pattern, " ! $?")
if match: 
  print ("match 3")
------example-------
(\D+\d) matches one or more non-digits followed by a digit.


Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.

\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.

\AS...\b.\Z would match 'SPAM!' in a search


## Email Extraction 

To demonstrate a sample usage of regular expressions, lets create a program to extract email addresses from a string.
Suppose we have a text that contains an email address:
str = "Please contact info@sololearn.com for assistance"


Our goal is to extract the substring "info@sololearn.com".
A basic email address consists of a word and may include dots or dashes. This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix).

This is the basis for building our regular expression.
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

[\w\.-]+ matches one or more word character, dot or dash.
The regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign, then another similar word, then a dot and another word.
Our regex contains three groups:
1 - first part of the email address.
2 - domain name without the suffix.
3 - the domain suffix.

import re

pattern = r"([\W\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
  print(match.group())

  In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses.


The regex in this example is for demonstration purposes only.
A much more complex regex is required to fully validate an email address.



# The Zen of Python
Writing programs that actually do what they are supposed to do is just one component of being a good Python programmer.
It's also important to write clean code that is easily understood, even weeks after you've written it.

One way of doing this is to follow the Zen of Python, a somewhat tongue-in-cheek set of principles that serves as a guide to programming the Pythoneer way. Use the following code to access the Zen of Python.

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
<!-- Blank space line at the end -->

## PEP


Python Enhancement Proposals (PEP) are suggestions for improvements to the language, made by experienced Python developers.
PEP 8 is a style guide on the subject of writing readable code. It contains a number of guidelines in reference to variable names, which are summarized here:
- modules should have short, all-lowercase names;
- class names should be in the CapWords style;
- most variables and function names should be lowercase_with_underscores;
- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
- names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.

PEP 8 also recommends using spaces around operators and after commas to increase readability.

## PEP 8


Other PEP 8 suggestions include the following:
- lines shouldn't be longer than 80 characters;
- 'from module import *' should be avoided;
- there should only be one statement per line.

It also suggests that you use spaces, rather than tabs, to indent. However, to some extent, this is a matter of personal preference. If you use spaces, only use 4 per line. It's more important to choose one and stick to it.

The most important advice in the PEP is to ignore it when it makes sense to do so. Don't bother with following PEP suggestions when it would cause your code to be less readable; inconsistent with the surrounding code; or not backwards compatible.
However, by and large, following PEP 8 will greatly enhance the quality of your code.
Some other notable PEPs that cover code style:
PEP 20: The Zen of Python
PEP 257: Style Conventions for Docstrings


## Function Arguments


Python allows to have function with varying number of arguments.
Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.
Example:
The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.


## Default Values


Named parameters to a function can be made optional by giving them a default value.
These must come after named parameters without a default value.
Example:
In case the argument is passed in, the default value is ignored.
If the argument is not passed in, the default value is used.


** kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.

def my_func(x, y=7, *args, **kwargs):
  print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

a and b are the names of the arguments that we passed to the function call, The arguments returned by **kwargs are not included in *args.

## Tuple Unpacking


Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.

numbers = (1, 2, 3)
a, b, c =numbers
print(a)
print(b)
print(c)

this can be also used to swap variables by doing a,b = b,a subce b,a on the right hand side forms the tuble (b,a) which is unpacked. 

A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


## Ternary Operator


Conditional expressions provide the functionality of if statements while using less code. They shouldn't be overused, as they can easily reduce readability, but they are often useful when assigning variables.
Conditional expressions are also known as applications of the ternary operator.

a = 7 
b = 1 if a >= 5 else 42
print(b)

The ternary operator checks the condition and returns the corresponding value.
In the example above, as the condition is true, b is assigned 1. If a was less than 5, it would have been assigned 42.

status = 1
msg = "logout" if status == 1 else "login"


The ternary operator is so called because, unlike most operators, it takes three arguments.


## else


The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning.
With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop).

The first for loop executes normally, resulting in the printing of "Unbroken 1".
The second loop exits due to a break, which is why it's else statement is not executed.

The else statement can also be used with try/except statements.
In this case, the code within it is only executed if no error occurs in the try statement.

try: 
  print(1)
except ZeroDivisionError:
  print(2)
else:
  print(3)

try:
  print(1/0)
except ZeroDivisionError:
  print(4)
else:
  print(5)


  ## __main__


Most Python code is either a module to be imported, or a script that does something.
However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
To do this, place script code inside if __name__ == "__main__".
This ensures that it won't be run if the file is imported.


def function():
  print("this is a module function")
if __name__=="__main__":
  print("this is a script")

  When the Python interpreter reads a source file, it executes all of the code it finds in the file. Before executing the code, it defines a few special variables.
For example, if the Python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.

If we save the code from our previous example as a file called sololearn.py, we can then import it to another script as a module, using the name sololearn.
sololearn.py

def function ():
  print("this is a module function")

  if __name__="__main__":
    print("this is a script")

some_script.py

import sololearn
sololearn.function()

result: 
>>> 
this is a module function 
>>>
Basically, we've created a custom module called sololearn, and then used it in another script.


## Major 3rd-Party Libraries


The Python standard library alone contains extensive functionality.
However, some tasks require the use of third-party libraries. Some major third-party libraries:
Django: The most frequently used web framework written in Python, Django powers websites that include Instagram and Disqus. It has many useful features, and whatever features it lacks are covered by extension packages.
CherryPy and Flask are also popular web frameworks.

For scraping data from websites, the library BeautifulSoup is very useful, and leads to better results than building your own scraper with regular expressions.
While Python does offer modules for programmatically accessing websites, such as urllib, they are quite cumbersome to use. Third-party library requests make it much easier to use HTTP requests.

A number of third-party modules are available that make it much easier to carry out scientific and mathematical computing with Python.
The module matplotlib allows you to create graphs based on data in Python.
The module NumPy allows for the use of multidimensional arrays that are much faster than the native Python solution of nested lists. It also contains functions to perform mathematical operations such as matrix transformations on the arrays.
The library SciPy contains numerous extensions to the functionality of NumPy.

Python can also be used for game development.
Usually, it is used as a scripting language for games written in other languages, but it can be used to make games by itself.
For 3D games, the library Panda3D can be used. For 2D games, you can use pygame.

## Packaging


In Python, the term packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease.
This involves use of the modules setuptools and distutils.
The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as an important file called setup.py.
Example directory structure:
SoloLearn/
   LICENSE.txt
   README.txt
   setup.py
   sololearn/
      __init__.py
      sololearn.py
      sololearn2.py
You can place as many script files in the directory as you need.


The next step in packaging is to write the setup.py file.
This contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip (name, version, etc.).
Example of a setup.py file:
from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)
After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution.
Use python setup.py register, followed by python setup.py sdist upload to upload a package.
Finally, install a package with python setup.py install.

The previous lesson covered packaging modules for use by other Python programmers. However, many computer users who are not programmers do not have Python installed. Therefore, it is useful to package scripts as executable files for the relevant platform, such as the Windows or Mac operating systems. This is not necessary for Linux, as most Linux users do have Python installed, and are able to run scripts as they are.

For Windows, many tools are available for converting scripts to executables. For example, py2exe, can be used to package a Python script, along with the libraries it requires, into a single executable.
PyInstaller and cx_Freeze serve the same purpose.
For Macs, use py2app, PyInstaller or cx_Freeze.