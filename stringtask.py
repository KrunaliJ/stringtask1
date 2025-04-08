#Strings
'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function
'''
print("hello")
print('Hello')

#Quotes inside quotes
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991")
print("It is used for 'web development (server-side),software development,mathematics,system scripting'")
print('why python"Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc)"')

#assign string to a variable
#Assigning a string to a variable is done with the variable name followed by an equal sign and the string

a="python"
print (a)

#multiline strings
#You can assign a multiline string to a variable by using three  double quotes three single quotes

b="""Python was designed for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose."""

c='''Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.
'''
print(b,c)

#strings are arrays
'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''
# eg:get the chracter at position 1(remember that the first character has the postion 0)

d="python tutorial"
print(a[1])

#looping through a string
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
#eg:loop through the letters in word "python"

for x in "pyhton":
    print(x)
    
#string length: to get the length of a string ,use the len()function it count the space along with comma and .

y="pyhton is a easy language."
print(len(y))

#check string:To check if a certain phrase or character is present in a string, we can use the keyword in

txt="The best things in life are free!"
print("free" in txt)

#use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#check if not:To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#use if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#python-slicing strings
'''
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
'''
c="python"
print(c[2:4]) #th

#slice from the start:By leaving out the start index, the range will start at the first character

print(c[:5])

#slice from the end:By leaving out the end index, the range will go to the end:

print(c[3:])