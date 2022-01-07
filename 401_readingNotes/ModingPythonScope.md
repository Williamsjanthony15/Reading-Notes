# Modifying the Behavior of a Python Scope
So far, you’ve learned how a Python scope works and how they restrict the visibility of variables, functions, classes, and other Python objects to certain portions of your code. You now know that you can access or reference global names from any place in your code, but they can be modified or updated from within the global Python scope.

You also know that you can access local names only from inside the local Python scope they were created in or from inside a nested function, but you can’t access them from the global Python scope or from other local scopes. Additionally, you’ve learned that nonlocal names can be accessed from inside nested functions, but they can’t be modified or updated from there.

Even though Python scopes follow these general rules by default, there are ways to modify this standard behavior. Python provides two keywords that allow you to modify the content of global and nonlocal names. These two keywords are:

global
nonlocal
In the next two sections, you’ll cover how to use these Python keywords to modify the standard behavior of Python scopes.

The global Statement
You already know that when you try to assign a value to a global name inside a function, you create a new local name in the function scope. To modify this behavior, you can use a global statement. With this statement, you can define a list of names that are going to be treated as global names.

The statement consists of the global keyword followed by one or more names separated by commas. You can also use multiple global statements with a name (or a list of names). All the names that you list in a global statement will be mapped to the global or module scope in which you define them.

Here’s an example where you try to update a global variable from within a function:

>>> counter = 0  # A global name
>>> def update_counter():
...     counter = counter + 1  # Fail trying to update counter
...
>>> update_counter()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in update_counter
UnboundLocalError: local variable 'counter' referenced before assignment
When you try to assign counter inside update_counter(), Python assumes that counter is local to update_counter() and raises an UnboundLocalError because you’re trying to access a name that isn’t defined yet.

If you want this code to work the way you expect here, then you can use a global statement as follows:

>>> counter = 0  # A global name
>>> def update_counter():
...     global counter  # Declare counter as global
...     counter = counter + 1  # Successfully update the counter
...
>>> update_counter()
>>> counter
1
>>> update_counter()
>>> counter
2
>>> update_counter()
>>> counter
3
In this new version of update_counter(), you add the statement global counter to the body of the function right before you try to change counter. With this tiny change, you’re mapping the name counter in the function scope to the same name in the global or module scope. From this point on, you can freely modify counter inside update_counter(). All the changes will reflect in the global variable.

With the statement global counter, you’re telling Python to look in the global scope for the name counter. This way, the expression counter = counter + 1 doesn’t create a new name in the function scope, but updates it in the global scope.

Note: The use of global is considered bad practice in general. If you find yourself using global to fix problems like the one above, then stop and think if there is a better way to write your code.

For example, you can try to write a self-contained function that relies on local names rather than on global names as follows:

>>> global_counter = 0  # A global name
>>> def update_counter(counter):
...     return counter + 1  # Rely on a local name
...
>>> global_counter = update_counter(global_counter)
>>> global_counter
1
>>> global_counter = update_counter(global_counter)
>>> global_counter
2
>>> global_counter = update_counter(global_counter)
>>> global_counter
3
This implementation of update_counter() defines counter as a parameter and returns its value augmented by 1 unit every time the function is called. This way, the result of update_counter() depends on the counter you use as an input and not on the changes that other functions (or pieces of code) can perform on the global variable, global_counter.

You can also use a global statement to create lazy global names by declaring them inside a function. Take a look at the following code:

>>> def create_lazy_name():
...     global lazy  # Create a global name, lazy
...     lazy = 100
...     return lazy
...
>>> create_lazy_name()
100
>>> lazy  # The name is now available in the global scope
100
>>> dir()
['__annotations__', '__builtins__',..., 'create_lazy_name', 'lazy']
When you call create_lazy_name(), you’re also creating a global variable called lazy. Notice that after calling the function, the name lazy is available in the global Python scope. If you inspect the global namespace using dir(), then you’ll see that lazy appears last in the list.

Note: Even though you can use a global statement to create lazy global names, this can be a dangerous practice that can lead to buggy code. So, it’s best to avoid things like this in your code.

For example, suppose you’re trying to get access to one of those lazy names and, for some reason, your code hasn’t called the function that creates that name yet. In this case, you’ll get a NameError and your program will crash.

Finally, it’s worth noting that you can use global from inside any function or nested function and the names listed will always be mapped to names in the global Python scope.

Also notice that, even though using a global statement at the top level of a module is legal, it doesn’t make much sense because any name assigned in the global scope is already a global name by definition. Take a look at the following code:

>>> name = 100
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'name']
>>> global name
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'name']
The use of a global statement like global name doesn’t change anything in your current global scope, as you can see in the output of dir(). The variable name is a global variable whether you use global or not.

^^^^^^^^^^^ These notes were take directly out of https://realpython.com/python-scope-legb-rule/#modifying-the-behavior-of-a-python-scope. I chose to copy directly so i can have all the tips and tricks and full description of it for locally gathered notes for later use. ^^^^^^^^^


# The nonlocal Statement
Similarly to global names, nonlocal names can be accessed from inner functions, but not assigned or updated. If you want to modify them, then you need to use a nonlocal statement. With a nonlocal statement, you can define a list of names that are going to be treated as nonlocal.

The nonlocal statement consists of the nonlocal keyword followed by one or more names separated by commas. These names will refer to the same names in the enclosing Python scope. The following example shows how you can use nonlocal to modify a variable defined in the enclosing or nonlocal scope:

>>> def func():
...     var = 100  # A nonlocal variable
...     def nested():
...         nonlocal var  # Declare var as nonlocal
...         var += 100
...
...     nested()
...     print(var)
...
>>> func()
200
With the statement nonlocal var, you tell Python that you’ll be modifying var inside nested(). Then, you increment var using an augmented assignment operation. This change is reflected in the nonlocal name var, which now has a value of 200.

Unlike global, you can’t use nonlocal outside of a nested or enclosed function. To be more precise, you can’t use a nonlocal statement in either the global scope or in a local scope. Here’s an example:

>>> nonlocal my_var  # Try to use nonlocal in the global scope
  File "<stdin>", line 1
SyntaxError: nonlocal declaration not allowed at module level
>>> def func():
...     nonlocal var  # Try to use nonlocal in a local scope
...     print(var)
...
  File "<stdin>", line 2
SyntaxError: no binding for nonlocal 'var' found
Here, you first try to use a nonlocal statement in the global Python scope. Since nonlocal only works inside an inner or nested function, you get a SyntaxError telling you that you can’t use nonlocal in a module scope. Notice that nonlocal doesn’t work inside a local scope either.

Note: For more detailed information on the nonlocal statement, check out PEP 3104 — Access to Names in Outer Scopes.

In contrast to global, you can’t use nonlocal to create lazy nonlocal names. Names must already exist in the enclosing Python scope if you want to use them as nonlocal names. This means that you can’t create nonlocal names by declaring them in a nonlocal statement in a nested function. Take a look at the following code example:

>>> def func():
...     def nested():
...         nonlocal lazy_var  # Try to create a nonlocal lazy name
...
  File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'lazy_var' found
In this example, when you try to define a nonlocal name using nonlocal lazy_var, Python immediately raises a SyntaxError because lazy_var doesn’t exist in the enclosing scope of nested().

^^^^^^^^^^^ These notes were take directly out of https://realpython.com/python-scope-legb-rule/#modifying-the-behavior-of-a-python-scope. I chose to copy directly so i can have all the tips and tricks and full description of it for locally gathered notes for later use. ^^^^^^^^^





