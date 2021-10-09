Read 42 to spare confusion

# What Are Dunder Methods?
In Python, special methods are a set of predefined methods you can use to enrich your classes. They are easy to recognize because they start and end with double underscores, for example __init__ or __str__.

As it quickly became tiresome to say under-under-method-under-under Pythonistas adopted the term “dunder methods”, a short form of “double under.”

These “dunders” or “special methods” in Python are also sometimes called “magic methods.” But using this terminology can make them seem more complicated than they really are—at the end of the day there’s nothing “magical” about them. You should treat these methods like a normal language feature.

Dunder methods let you emulate the behavior of built-in types. For example, to get the length of a string you can call len('string'). But an empty class definition doesn’t support this behavior out of the box:

class NoLenSupport:
    pass

>>> obj = NoLenSupport()
>>> len(obj)
TypeError: "object of type 'NoLenSupport' has no len()"
To fix this, you can add a __len__ dunder method to your class:

class LenSupport:
    def __len__(self):
        return 42

>>> obj = LenSupport()
>>> len(obj)
42
Another example is slicing. You can implement a __getitem__ method which allows you to use Python’s list slicing syntax: obj[start:stop].

Special Methods and the Python Data Model
This elegant design is known as the Python data model and lets developers tap into rich language features like sequences, iteration, operator overloading, attribute access, etc.

You can see Python’s data model as a powerful API you can interface with by implementing one or more dunder methods. If you want to write more Pythonic code, knowing how and when to use dunder methods is an important step.

For a beginner this might be slightly overwhelming at first though. No worries, in this article I will guide you through the use of dunder methods using a simple Account class as an example.

Enriching a Simple Account Class
Throughout this article I will enrich a simple Python class with various dunder methods to unlock the following language features:

Initialization of new objects
Object representation
Enable iteration
Operator overloading (comparison)
Operator overloading (addition)
Method invocation
Context manager support (with statement)
You can find the final code example here. I’ve also put together a Jupyter notebook so you can more easily play with the examples.

Object Initialization: __init__
Right upon starting my class I already need a special method. To construct account objects from the Account class I need a constructor which in Python is the __init__ dunder:

class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []
The constructor takes care of setting up the object. In this case it receives the owner name, an optional start amount and defines an internal transactions list to keep track of deposits and withdrawals.

This allows us to create new accounts like this:

>>> acc = Account('bob')  # default amount = 0
>>> acc = Account('bob', 10)
Object Representation: __str__, __repr__
It’s common practice in Python to provide a string representation of your object for the consumer of your class (a bit like API documentation.) There are two ways to do this using dunder methods:

__repr__: The “official” string representation of an object. This is how you would make an object of the class. The goal of __repr__ is to be unambiguous.

__str__: The “informal” or nicely printable string representation of an object. This is for the enduser.

Let’s implement these two methods on the Account class:

class Account:
    # ... (see above)

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)
If you don’t want to hardcode "Account" as the name for the class you can also use self.__class__.__name__ to access it programmatically.

If you wanted to implement just one of these to-string methods on a Python class, make sure it’s __repr__.

Now I can query the object in various ways and always get a nice string representation:

>>> str(acc)
'Account of bob with starting amount: 10'

>>> print(acc)
"Account of bob with starting amount: 10"

>>> repr(acc)
"Account('bob', 10)"
Iteration: __len__, __getitem__, __reversed__
In order to iterate over our account object I need to add some transactions. So first, I’ll define a simple method to add transactions. I’ll keep it simple because this is just setup code to explain dunder methods, and not a production-ready accounting system:

def add_transaction(self, amount):
    if not isinstance(amount, int):
        raise ValueError('please use int for amount')
    self._transactions.append(amount)
I also defined a property to calculate the balance on the account so I can conveniently access it with account.balance. This method takes the start amount and adds a sum of all the transactions:

@property
def balance(self):
    return self.amount + sum(self._transactions)
Let’s do some deposits and withdrawals on the account:

>>> acc = Account('bob', 10)

>>> acc.add_transaction(20)
>>> acc.add_transaction(-10)
>>> acc.add_transaction(50)
>>> acc.add_transaction(-20)
>>> acc.add_transaction(30)

>>> acc.balance
80
Now I have some data and I want to know:

How many transactions were there?

Index the account object to get transaction number …

Loop over the transactions

With the class definition I have this is currently not possible. All of the following statements raise TypeError exceptions:

>>> len(acc)
TypeError

>>> for t in acc:
...    print(t)
TypeError

>>> acc[1]
TypeError
Dunder methods to the rescue! It only takes a little bit of code to make the class iterable:

class Account:
    # ... (see above)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]
Now the previous statements work:

>>> len(acc)
5

>>> for t in acc:
...    print(t)
20
-10
50
-20
30

>>> acc[1]
-10
To iterate over transactions in reversed order you can implement the __reversed__ special method:

def __reversed__(self):
    return self[::-1]

>>> list(reversed(acc))
[30, -20, 50, -10, 20]
To reverse the list of transactions I used Python’s reverse list slice syntax. I also had to wrapp the result of reversed(acc) in a list() call because reversed() returns a a reverse iterator, not a list object we can print nicely in the REPL. Check out this tutorial on iterators in Python if you’d like to learn more about how this approach works in detail.

All in all, this account class is starting to look quite Pythonic to me now.

Operator Overloading for Comparing Accounts: __eq__, __lt__
We all write dozens of statements daily to compare Python objects:

>>> 2 > 1
True

>>> 'a' > 'b'
False
This feels completely natural, but it’s actually quite amazing what happens behind the scenes here. Why does > work equally well on integers, strings and other objects (as long as they are the same type)? This polymorphic behavior is possible because these objects implement one or more comparison dunder methods.

An easy way to verify this is to use the dir() builtin:

>>> dir('a')
['__add__',
...
'__eq__',    <---------------
'__format__',
'__ge__',    <---------------
'__getattribute__',
'__getitem__',
'__getnewargs__',
'__gt__',    <---------------
...]
Let’s build a second account object and compare it to the first one (I am adding a couple of transactions for later use):

>>> acc2 = Account('tim', 100)
>>> acc2.add_transaction(20)
>>> acc2.add_transaction(40)
>>> acc2.balance
160

>>> acc2 > acc
TypeError:
"'>' not supported between instances of 'Account' and 'Account'"
What happened here? We got a TypeError because I have not implemented any comparison dunders nor inherited them from a parent class.

Let’s add them. To not have to implement all of the comparison dunder methods, I use the functools.total_ordering decorator which allows me to take a shortcut, only implementing __eq__ and __lt__:

from functools import total_ordering

@total_ordering
class Account:
    # ... (see above)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance
And now I can compare Account instances no problem:

>>> acc2 > acc
True

>>> acc2 < acc
False

>>> acc == acc2
False
Operator Overloading for Merging Accounts: __add__
In Python, everything is an object. We are completely fine adding two integers or two strings with the + (plus) operator, it behaves in expected ways:

>>> 1 + 2
3

>>> 'hello' + ' world'
'hello world'
Again, we see polymorphism at play: Did you notice how + behaves different depending the type of the object? For integers it sums, for strings it concatenates. Again doing a quick dir() on the object reveals the corresponding “dunder” interface into the data model:

>>> dir(1)
[...
'__add__',
...
'__radd__',
...]
Our Account object does not support addition yet, so when you try to add two instances of it there’s a TypeError:

>>> acc + acc2
TypeError: "unsupported operand type(s) for +: 'Account' and 'Account'"
Let’s implement __add__ to be able to merge two accounts. The expected behavior would be to merge all attributes together: the owner name, as well as starting amounts and transactions. To do this we can benefit from the iteration support we implemented earlier:

def __add__(self, other):
    owner = '{}&{}'.format(self.owner, other.owner)
    start_amount = self.amount + other.amount
    acc = Account(owner, start_amount)
    for t in list(self) + list(other):
        acc.add_transaction(t)
    return acc
Yes, it is a bit more involved than the other dunder implementations so far. It should show you though that you are in the driver’s seat. You can implement addition however you please. If we wanted to ignore historic transactions—fine, you can also implement it like this:

def __add__(self, other):
    owner = self.owner + other.owner
    start_amount = self.balance + other.balance
    return Account(owner, start_amount)
I think the former implementation would be more realistic though, in terms of what a consumer of this class would expect to happen.

Now we have a new merged account with starting amount $110 (10 + 100) and balance of $240 (80 + 160):

>>> acc3 = acc2 + acc
>>> acc3
Account('tim&bob', 110)

>>> acc3.amount
110
>>> acc3.balance
240
>>> acc3._transactions
[20, 40, 20, -10, 50, -20, 30]
Note this works in both directions because we’re adding objects of the same type. In general, if you would add your object to a builtin (int, str, …) the __add__ method of the builtin wouldn’t know anything about your object. In that case you need to implement the reverse add method (__radd__) as well. You can see an example for that here.

Callable Python Objects: __call__
You can make an object callable like a regular function by adding the __call__ dunder method. For our account class we could print a nice report of all the transactions that make up its balance:

class Account:
    # ... (see above)

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))
Now when I call the object with the double-parentheses acc() syntax, I get a nice account statement with an overview of all transactions and the current balance:

>>> acc = Account('bob', 10)
>>> acc.add_transaction(20)
>>> acc.add_transaction(-10)
>>> acc.add_transaction(50)
>>> acc.add_transaction(-20)
>>> acc.add_transaction(30)

>>> acc()
Start amount: 10
Transactions:
20
-10
50
-20
30
Balance: 80
Please keep in mind that this is just a toy example. A “real” account class probably wouldn’t print to the console when you use the function call syntax on one of its instances. In general, the downside of having a __call__ method on your objects is that it can be hard to see what the purpose of calling the object is.

Most of the time it’s therefore better to add an explicit method to the class. In this case it probably would’ve been more transparent to have a separate Account.print_statement() method.

Context Manager Support and the With Statement: __enter__, __exit__
My final example in this tutorial is about a slightly more advanced concept in Python: Context managers and adding support for the with statement.

Now, what is a “context manager” in Python? Here’s a quick overview:

A context manager is a simple “protocol” (or interface) that your object needs to follow so it can be used with the with statement. Basically all you need to do is add __enter__ and __exit__ methods to an object if you want it to function as a context manager.

Let’s use context manager support to add a rollback mechanism to our Account class. If the balance goes negative upon adding another transaction we rollback to the previous state.

We can leverage the Pythonic with statement by adding two more dunder methods. I’m also adding some print calls to make the example clearer when we demo it:

class Account:
    # ... (see above)

    def __enter__(self):
        print('ENTER WITH: Making backup of transactions for rollback')
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print('Rolling back to previous transactions')
            print('Transaction resulted in {} ({})'.format(
                exc_type.__name__, exc_val))
        else:
            print('Transaction OK')
As an exception has to be raised to trigger a rollback, I define a quick helper method to validate the transactions in an account:

def validate_transaction(acc, amount_to_add):
    with acc as a:
        print('Adding {} to account'.format(amount_to_add))
        a.add_transaction(amount_to_add)
        print('New balance would be: {}'.format(a.balance))
        if a.balance < 0:
            raise ValueError('sorry cannot go in debt!')
Now I can use an Account object with the with statement. When I make a transaction to add a positive amount, all is good:

acc4 = Account('sue', 10)

print('\nBalance start: {}'.format(acc4.balance))
validate_transaction(acc4, 20)

print('\nBalance end: {}'.format(acc4.balance))
Executing the above Python snippet produces the following printout:

Balance start: 10
ENTER WITH: Making backup of transactions for rollback
Adding 20 to account
New balance would be: 30
EXIT WITH: Transaction OK
Balance end: 30
However when I try to withdraw too much money, the code in __exit__ kicks in and rolls back the transaction:

acc4 = Account('sue', 10)

print('\nBalance start: {}'.format(acc4.balance))
try:
    validate_transaction(acc4, -50)
except ValueError as exc:
    print(exc)

print('\nBalance end: {}'.format(acc4.balance))
In this case we get a different result:

Balance start: 10
ENTER WITH: Making backup of transactions for rollback
Adding -50 to account
New balance would be: -40
EXIT WITH: Rolling back to previous transactions
ValueError: sorry cannot go in debt!
Balance end: 10


Notes taken directly from https://dbader.org/blog/python-dunder-methods


# Python Iterators: A Step-By-Step Introduction

Let’s take the humble for-in loop, for example. It speaks for Python’s beauty that you can read a Pythonic loop like this as if it was an English sentence:

numbers = [1, 2, 3]
for n in numbers:
    print(n)
But how do Python’s elegant loop constructs work behind the scenes? How does the loop fetch individual elements from the object it is looping over? And how can you support the same programming style in your own Python objects?

You’ll find the answer to these questions in Python’s iterator protocol:

Objects that support the __iter__ and __next__ dunder methods automatically work with for-in loops.

But let’s take things step by step. Just like decorators, iterators and their related techniques can appear quite arcane and complicated on first glance. So we’ll ease into it.

In this tutorial you’ll see how to write several Python classes that support the iterator protocol. They’ll serve as “non-magical” examples and test implementations you can build upon and deepen your understanding with.

We’ll focus on the core mechanics of iterators in Python 3 first and leave out any unnecessary complications, so you can see clearly how iterators behave at the fundamental level.

I’ll tie each example back to the for-in loop question we started out with. And at the end of this tutorial we’ll go over some differences that exist between Python 2 and 3 when it comes to iterators.

Ready? Let’s jump right in!

Python Iterators That Iterate Forever
We’ll begin by writing a class that demonstrates the bare-bones iterator protocol in Python. The example I’m using here might look different from the examples you’ve seen in other iterator tutorials, but bear with me. I think doing it this way gives you a more applicable understanding of how iterators work in Python.

Over the next few paragraphs we’re going to implement a class called Repeater that can be iterated over with a for-in loop, like so:

repeater = Repeater('Hello')
for item in repeater:
    print(item)
Like its name suggests, instances of this Repeater class will repeatedly return a single value when iterated over. So the above example code would print the string Hello to the console forever.

To start with the implementation we’ll define and flesh out the Repeater class first:

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)
On first inspection, Repeater looks like a bog-standard Python class. But notice how it also includes the __iter__ dunder method.

What’s the RepeaterIterator object we’re creating and returning from __iter__? It’s a helper class we also need to define for our for-in iteration example to work:

class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value
Again, RepeaterIterator looks like a straightforward Python class, but you might want to take note of the following two things:

In the __init__ method we link each RepeaterIterator instance to the Repeater object that created it. That way we can hold on to the “source” object that’s being iterated over.

In RepeaterIterator.__next__, we reach back into the “source” Repeater instance and return the value associated with it.

In this code example, Repeater and RepeaterIterator are working together to support Python’s iterator protocol. The two dunder methods we defined, __iter__ and __next__, are the key to making a Python object iterable.

We’ll take a closer look at these two methods and how they work together after some hands-on experimentation with the code we’ve got so far.

Let’s confirm that this two-class setup really made Repeater objects compatible with for-in loop iteration. To do that we’ll first create an instance of Repeater that would return the string 'Hello' indefinitely:

>>> repeater = Repeater('Hello')
And now we’re going to try iterating over this repeater object with a for-in loop. What’s going to happen when you run the following code snippet?

>>> for item in repeater:
...     print(item)
Right on! You’ll see 'Hello' printed to the screen…a lot. Repeater keeps on returning the same string value, and so, this loop will never complete. Our little program is doomed to print 'Hello' to the console forever:

Hello
Hello
Hello
Hello
Hello
...
But congratulations—you just wrote a working iterator in Python and used it with a for-in loop. The loop may not terminate yet…but so far, so good!

Next up we’ll tease this example apart to understand how the __iter__ and __next__ methods work together to make a Python object iterable.

Pro tip: If you ran the last example inside a Python REPL session or from the terminal and you want to stop it, hit Ctrl + C a few times to break out of the infinite loop.

How do for-in loops work in Python?
At this point we’ve got our Repeater class that apparently supports the iterator protocol, and we just ran a for-in loop to prove it:

repeater = Repeater('Hello')
for item in repeater:
    print(item)
Now, what does this for-in loop really do behind the scenes? How does it communicate with the repeater object to fetch new elements from it?

To dispel some of that “magic” we can expand this loop into a slightly longer code snippet that gives the same result:

repeater = Repeater('Hello')
iterator = repeater.__iter__()
while True:
    item = iterator.__next__()
    print(item)
As you can see, the for-in was just syntactic sugar for a simple while loop:

It first prepared the repeater object for iteration by calling its __iter__ method. This returned the actual iterator object.
After that, the loop repeatedly calls the iterator object’s __next__ method to retrieve values from it.
If you’ve ever worked with database cursors, this mental model will seem familiar: We first initialize the cursor and prepare it for reading, and then we can fetch data into local variables as needed from it, one element at a time.

Because there’s never more than one element “in flight”, this approach is highly memory-efficient. Our Repeater class provides an infinite sequence of elements and we can iterate over it just fine. Emulating the same with a Python list would be impossible—there’s no way we could create a list with an infinite number of elements in the first place. This makes iterators a very powerful concept.

On more abstract terms, iterators provide a common interface that allows you to process every element of a container while being completely isolated from the container’s internal structure.

Whether you’re dealing with a list of elements, a dictionary, an infinite sequence like the one provided by our Repeater class, or another sequence type—all of that is just an implementation detail. Every single one of these objects can be traversed in the same way by the power of iterators.

And as you’ve seen, there’s nothing special about for-in loops in Python. If you peek behind the curtain, it all comes down to calling the right dunder methods at the right time.

In fact, you can manually “emulate” how the loop used the iterator protocol in a Python interpreter session:

>>> repeater = Repeater('Hello')
>>> iterator = iter(repeater)
>>> next(iterator)
'Hello'
>>> next(iterator)
'Hello'
>>> next(iterator)
'Hello'
...
This gives the same result: An infinite stream of hellos. Every time you call next() the iterator hands out the same greeting again.

By the way, I took the opportunity here to replace the calls to __iter__ and __next__ with calls to Python’s built-in functions iter() and next().

Internally these built-ins invoke the same dunder methods, but they make this code a little prettier and easier to read by providing a clean “facade” to the iterator protocol.

Python offers these facades for other functionality as well. For example, len(x) is a shortcut for calling x.__len__. Similarly, calling iter(x) invokes x.__iter__ and calling next(x) invokes x.__next__.

Generally it’s a good idea to use the built-in facade functions rather than directly accessing the dunder methods implementing a protocol. It just makes the code a little easier to read.

A Simpler Iterator Class
Up until now our iterator example consisted of two separate classes, Repeater and RepeaterIterator. They corresponded directly to the two phases used by Python’s iterator protocol:

First setting up and retrieving the iterator object with an iter() call, and then repeatedly fetching values from it via next().

Many times both of these responsibilities can be shouldered by a single class. Doing this allows you to reduce the amount of code necessary to write a class-based iterator.

I chose not to do this with the first example in this tutorial, because it mixes up the cleanliness of the mental model behind the iterator protocol. But now that you’ve seen how to write a class-based iterator the longer and more complicated way, let’s take a minute to simplify what we’ve got so far.

Remember why we needed the RepeaterIterator class again? We needed it to host the __next__ method for fetching new values from the iterator. But it doesn’t really matter where __next__ is defined. In the iterator protocol, all that matters is that __iter__ returns any object with a __next__ method on it.

So here’s an idea: RepeaterIterator returns the same value over and over, and it doesn’t have to keep track of any internal state. What if we added the __next__ method directly to the Repeater class instead?

That way we could get rid of RepeaterIterator altogether and implement an iterable object with a single Python class. Let’s try it out! Our new and simplified iterator example looks as follows:

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value
We just went from two separate classes and 10 lines of code to to just one class and 7 lines of code. Our simplified implementation still supports the iterator protocol just fine:

>>> repeater = Repeater('Hello')
>>> for item in repeater:
...    print(item)

Hello
Hello
Hello
...
Streamlining a class-based iterator like that often makes sense. In fact, most Python iterator tutorials start out that way. But I always felt that explaining iterators with a single class from the get-go hides the underlying principles of the iterator protocol—and thus makes it more difficult to understand.

Who Wants to Iterate Forever
At this point you’ll have a pretty good understanding of how iterators work in Python. But so far we’ve only implemented iterators that kept on iterating forever.

Clearly, infinite repetition isn’t the main use case for iterators in Python. In fact, when you look back all the way to the beginning of this tutorial, I used the following snippet as a motivating example:

numbers = [1, 2, 3]
for n in numbers:
    print(n)
You’ll rightfully expect this code to print the numbers 1, 2, and 3 and then stop. And you probably don’t expect it to go on spamming your terminal window by printing threes forever until you mash Ctrl+C a few times in a wild panic…

And so, it’s time to find out how to write an iterator that eventually stops generating new values instead of iterating forever. Because that’s what Python objects typically do when we use them in a for-in loop.

We’ll now write another iterator class that we’ll call BoundedRepeater. It’ll be similar to our previous Repeater example, but this time we’ll want it to stop after a predefined number of repetitions.

Let’s think about this for a bit. How do we do this? How does an iterator signal that it’s exhausted and out of elements to iterate over? Maybe you’re thinking, “Hmm, we could just return None from the __next__ method.”

And that’s not a bad idea—but the trouble is, what are we going to do if we want some iterators to be able to return None as an acceptable value?

Let’s see what other Python iterators do to solve this problem. I’m going to construct a simple container, a list with a few elements, and then I’ll iterate over it until it runs out of elements to see what happens:

>>> my_list = [1, 2, 3]
>>> iterator = iter(my_list)

>>> next(iterator)
1
>>> next(iterator)
2
>>> next(iterator)
3
Careful now! We’ve consumed all of the three available elements in the list. Watch what happens if I call next on the iterator again:

>>> next(iterator)
StopIteration
Aha! It raises a StopIteration exception to signal we’ve exhausted all of the available values in the iterator.

That’s right: Iterators use exceptions to structure control flow. To signal the end of iteration, a Python iterator simply raises the built-in StopIteration exception.

If I keep requesting more values from the iterator it’ll keep raising StopIteration exceptions to signal that there are no more values available to iterate over:

>>> next(iterator)
StopIteration
>>> next(iterator)
StopIteration
...
Python iterators normally can’t be “reset”—once they’re exhausted they’re supposed to raise StopIteration every time next() is called on them. To iterate anew you’ll need to request a fresh iterator object with the iter() function.

Now we know everything we need to write our BoundedRepeater class that stops iterating after a set number of repetitions:

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value
This gives us the desired result. Iteration stops after the number of repetitions defined in the max_repeats parameter:

>>> repeater = BoundedRepeater('Hello', 3)
>>> for item in repeater:
        print(item)
Hello
Hello
Hello
If we rewrite this last for-in loop example to take away some of the syntactic sugar, we end up with the following expanded code snippet:

repeater = BoundedRepeater('Hello', 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item)
Every time next() is called in this loop we check for a StopIteration exception and break the while loop if necessary.

Being able to write a three-line for-in loop instead of an eight lines long while loop is quite a nice improvement. It makes the code easier to read and more maintainable. And this is another reason why iterators in Python are such a powerful tool.

Python 2.x Compatible Iterators
All the code examples I showed here were written in Python 3. There’s a small but important difference between Python 2 and 3 when it comes to implementing class-based iterators:

In Python 3, the method that retrieves the next value from an iterator is called __next__.
In Python 2, the same method is called next (no underscores).
This naming difference can lead to some trouble if you’re trying to write class-based iterators that should work on both versions of Python. Luckily there’s a simple approach you can take to work around this difference.

Here’s an updated version of the InfiniteRepeater class that will work on both Python 2 and Python 3:

class InfiniteRepeater(object):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

    # Python 2 compatibility:
    def next(self):
        return self.__next__()
To make this iterator class compatible with Python 2 I’ve made two small changes to it:

First, I added a next method that simply calls the original __next__ and forwards its return value. This essentially creates an alias for the existing __next__ implementation so that Python 2 finds it. That way we can support both versions of Python while still keeping all of the actual implementation details in one place.

And second, I modified the class definition to inherit from object in order to ensure we’re creating a new-style class on Python 2. This has nothing to do with iterators specifically, but it’s a good practice nonetheless.

Notes taken directly from https://dbader.org/blog/python-iterators

# What Are Python Generators?

Python Generators 101 – The Basics
Let’s start by looking again at the Repeater example that I previously used to introduce the idea of iterators. It implemented a class-based iterator cycling through an infinite sequence of values.

This is what the class looked like in its second (simplified) version:

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value
If you’re thinking, “that’s quite a lot of code for such a simple iterator,” you’re absolutely right. Parts of this class seem rather formulaic, as if they would be written in exactly the same way from one class-based iterator to the next.

This is where Python’s generators enter the scene. If I rewrite this iterator class as a generator, it looks like this:

def repeater(value):
    while True:
        yield value
We just went from seven lines of code to three.

Not bad, eh? As you can see, generators look like regular functions but instead of using the return statement, they use yield to pass data back to the caller.

Will this new generator implementation still work the same way as our class-based iterator did? Let’s bust out the for-in loop test to find out:

>>> for x in repeater('Hi'):
...    print(x)
'Hi'
'Hi'
'Hi'
'Hi'
'Hi'
...
Yep! We’re still looping through our greetings forever. This much shorter generator implementation seems to perform the same way that the Repeater class did.

(Remember to hit Ctrl+C if you want out of the infinite loop in an interpreter session.)

Now, how do these generators work? They look like normal functions, but their behavior is quite different. For starters, calling a generator function doesn’t even run the function. It merely creates and returns a generator object:

>>> repeater('Hey')
<generator object repeater at 0x107bcdbf8>
The code in the generator function only executes when next() is called on the generator object:

>>> generator_obj = repeater('Hey')
>>> next(generator_obj)
'Hey'
If you read the code of the repeater function again, it looks like the yield keyword in there somehow stops this generator function in mid-execution and then resumes it at a later point in time:

def repeater(value):
    while True:
        yield value
And that’s quite a fitting mental model for what happens here. You see, when a return statement is invoked inside a function, it permanently passes control back to the caller of the function. When a yield is invoked, it also passes control back to the caller of the function—but it only does so temporarily.

Whereas a return statement disposes of a function’s local state, a yield statement suspends the function and retains its local state.

In practical terms, this means local variables and the execution state of the generator function are only stashed away temporarily and not thrown out completely.

Execution can be resumed at any time by calling next() on the generator:

>>> iterator = repeater('Hi')
>>> next(iterator)
'Hi'
>>> next(iterator)
'Hi'
>>> next(iterator)
'Hi'
This makes generators fully compatible with the iterator protocol. For this reason, I like to think of them primarily as syntactic sugar for implementing iterators.

You’ll find that for most types of iterators, writing a generator function will be easier and more readable than defining a long-winded class-based iterator.

Python Generators That Stop Generating
In this tutorial we started out by writing an infinite generator once again. By now you’re probably wondering how to write a generator that stops producing values after a while, instead of going on and on forever.

Remember, in our class-based iterator we were able to signal the end of iteration by manually raising a StopIteration exception. Because generators are fully compatible with class-based iterators, that’s still what happens behind the scenes.

Thankfully, as programmers we get to work with a nicer interface this time around. Generators stop generating values as soon as control flow returns from the generator function by any means other than a yield statement. This means you no longer have to worry about raising StopIteration at all!

Here’s an example:

def repeat_three_times(value):
    yield value
    yield value
    yield value
Notice how this generator function doesn’t include any kind of loop. In fact it’s dead simple and only consists of three yield statements. If a yield temporarily suspends execution of the function and passes back a value to the caller, what will happen when we reach the end of this generator?

Let’s find out:

>>> for x in repeat_three_times('Hey there'):
...     print(x)
'Hey there'
'Hey there'
'Hey there'
As you may have expected, this generator stopped producing new values after three iterations. We can assume that it did so by raising a StopIteration exception when execution reached the end of the function.

But to be sure, let’s confirm that with another experiment:

>>> iterator = repeat_three_times('Hey there')
>>> next(iterator)
'Hey there'
>>> next(iterator)
'Hey there'
>>> next(iterator)
'Hey there'
>>> next(iterator)
StopIteration
>>> next(iterator)
StopIteration
This iterator behaved just like we expected. As soon as we reach the end of the generator function, it keeps raising StopIteration to signal that it has no more values to provide.

Let’s come back to another example from my Python iterators tutorials. The BoundedIterator class implemented an iterator that would only repeat a value a set number of times:

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value
Why don’t we try to re-implement this BoundedRepeater class as a generator function. Here’s my first take on it:

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value
I intentionally made the while loop in this function a little unwieldy. I wanted to demonstrate how invoking a return statement from a generator causes iteration to stop with a StopIteration exception. We’ll soon clean up and simplify this generator function some more, but first let’s try out what we’ve got so far:

>>> for x in bounded_repeater('Hi', 4):
...     print(x)
'Hi'
'Hi'
'Hi'
'Hi'
Great! Now we have a generator that stops producing values after a configurable number of repetitions. It uses the yield statement to pass back values until it finally hits the return statement and iteration stops.

Like I promised you, we can further simplify this generator. We’ll take advantage of the fact that Python adds an implicit return None statement to the end of every function. This is what our final implementation looks like:

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
Feel free to confirm that this simplified generator still works the same way. All things considered, we went from a 12-line iterator in the BoundedRepeater class to a three-line generator-based implementation providing the same functionality.

That’s a 75% reduction in the number of lines of code—not too shabby!

Generator functions are a great feature in Python, and you shouldn’t hesitate to use them in your own programs.

As you just saw, generators help you “abstract away” most of the boilerplate code otherwise needed when writing class-based iterators. Generators can make your life as a Pythonista much easier and allow you to write cleaner, shorter, and more maintainable iterators.

Notes taken directly from https://dbader.org/blog/python-generators
