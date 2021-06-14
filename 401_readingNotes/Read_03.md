# What Is a File?

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

## Files on most modern file systems are composed of three main parts:

Header: metadata about the contents of the file (file name, size, type, and so on)
Data: contents of the file as written by the creator or editor
End of file (EOF): special character that indicates the end of the file

## File Paths

When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

Folder Path: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)
File Name: the actual name of the file
Extension: the end of the file path pre-pended with a period (.) used to indicate the file type


## Line Endings

Windows uses the CR+LF characters to indicate a new line, while Unix and the newer Mac versions use just the LF character. 


# Opening and Closing a File in Python

This is done by invoking the open() built-in function. open() has a single required argument that is the path to the file. open() has a single return, the file object:

 <!-- file = open('dog_breeds.txt') -->

After you open a file, the next thing to learn is how to close it.

Warning: You should always make sure that an open file is properly closed.
<!-- 
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close() -->


    Character	Meaning
'r'	Open for reading (default)
'w'	Open for writing, truncating (overwriting) the file first
'rb' or 'wb'	Open in binary mode (read/write using byte data)

# Reading and Writing Opened Files

Once you’ve opened up a file, you’ll want to read or write to the file. First off, let’s cover reading a file. There are multiple methods that can be called on a file object to help you out:

## Method	What It Does

.read(size=-1)	This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
.readline(size=-1)	This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
.readlines()	This reads the remaining lines from the file object and returns them as a list.


Method	What It Does
.write(string)	This writes the string to the file.
.writelines(seq)	This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).

Python Exceptions: An Introduction


## Exceptions versus Syntax Errors

Syntax errors occur when the parser detects an incorrect statement. Observe the following example:

The arrow indicates where the parser ran into the syntax error. In this example, there was one bracket too many. Remove it and run your code again:

## Raising an Exception
We can use raise to throw an exception if a condition occurs. The statement can be complemented with a custom exception.


## The AssertionError Exception
Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. We assert that a certain condition is met. If this condition turns out to be True, then that is excellent! The program can continue. If the condition turns out to be False, you can have the program throw an AssertionError exception.

## The try and except Block: Handling Exceptions
The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.

## The else Clause
In Python, using the else statement, you can instruct a program to execute a certain block of code only in the absence of exceptions.

## Cleaning Up After Using finally
Imagine that you always had to implement some sort of action to clean up after executing your code. Python enables you to do so using the finally clause.

