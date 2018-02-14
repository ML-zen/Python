# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 23:53:59 2018

@author: JohnK
"""
# Basic function without arguments
line_sep="##############################################"
def greet():
   print("** Basic verion of a function  with No Arguments passed **")
   print("Hello Mister/Miss, Good Morning")
   print(line_sep)
greet()

# Basic function with arguments . Arguments are taken in the same order passwd by calling function
# Exaple name->"Shahrukh, msg->"Good Morning"
def greet(name,msg):
   print("** function  with two Arguments are passed **")   
   print("Hello",name + ', ' + msg)
   print(line_sep)

greet("Sachin","Good morning!")

## Changing the order of string messages passed to the function gives unexpected results
# Example : Below line will print "Hello, Good Moring", Deepika"
greet("Good morning!", "Sachin")
# Below line will print correct "Hello, Deepika Good Morning"
greet(name = "Sachin", msg = "Good morning!")

# This will return an error, as the defined function required two arguments, but calling function passed only one argument  
#greet("Salman")

# Below function with two arguments, one argument has a default value.
def greet(name,msg="Good Morning"):
   print("** function  with two Arguments passed, one argument has a default value **")   
   print("Hello", name + ', ' + msg)
   print(line_sep)

# This will work fine although only one argument is passed   
greet("Dhoni")
# This will work fine as default msg in the function "Good Morning" is replaced with "Good Evening"  
greet("Dhoni", "Good Evening")

"""
Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values.
"""
"""
def greet(name,msg="Good Morning", addl_msg):
   print("** function  with two Arguments passed **")   
   print("Hello", name + ', ' + msg)
   print(line_sep)

"""


# Below function with two arguments, one argument has a default value.
def greet(name,msg, *args):
   print("** function  with two Arguments passed, and additional list of values **")   
   output_msg = name + " " + msg
   for msg1 in args:
       output_msg = output_msg + ". " + msg1 
   print(output_msg)
   print(line_sep)

greet("Yuvraj !!", "Good Morning", "Welcome", "How are you doing", "Have a nice day")

def greet(name,msg="Good morning", *args):
   print("** function  with two Arguments passed, and additional list of values **")   
   output_msg = name + " " + msg
   for msg1 in args:
       output_msg = output_msg + ". " + msg1 
   print(output_msg)
   print(line_sep)

greet("Yuvraj !!", "Welcome", "How are you doing", "Have a nice day")

# Below function will display a different output than above one. Please try
def greet(name, *args, msg="Good morning"):
   print("** function  with two Arguments passed, and additional list of values **")   
   output_msg = name + " " + msg
   for msg1 in args:
       output_msg = output_msg + ". " + msg1 
   print(output_msg)
   print(line_sep)

greet("Virat !!", "Welcome", "How are you doing", "Have a nice day")

# Below function will display a different output than above one. Please try
def greet(name, msg, **kwargs ):
   print("** function  with two Arguments passed, and additional list of values **")   
   output_msg = name + " " + msg + "\n"
   for key in kwargs:
       output_msg = output_msg + "%s = %s" % (key, kwargs[key]) + "\n"
       
   print(output_msg)
   print(line_sep)

greet("Amir", "Welcome", film_1="Secret Superstar", film_2="Dangal", film_3="PK", film_4="Dhoom3")



# Below function will uses both list and dictionaries as input 
def greet(name, msg, *args, **kwargs ):
   print("** function  with two Arguments passed, and additional list of values **")   
   output_msg = name + " " + msg 
   for msg1 in args:
       output_msg = output_msg + ". " + msg1  
   output_msg = output_msg + " ########### Film List ########" + "\n"
   for key in kwargs:
       output_msg = output_msg + "%s = %s" % (key, kwargs[key]) + "\n"
       
   print(output_msg)
   print(line_sep)
greet("Amir !!", "Welcome", "How are you doing", "Have a nice day", film_1="Secret Superstar", film_2="Dangal", film_3="PK", film_4="Dhoom3")


def greet(name,  *args, msg="Good Evening", **kwargs  ):
   print("** function  with two Arguments passed, and additional list of values **")   
   output_msg = name + " " + msg 
   for msg1 in args:
       output_msg = output_msg + ". " + msg1  
   output_msg = output_msg + " ########### Film List ########" + "\n"
   for key in kwargs:
       output_msg = output_msg + "%s = %s" % (key, kwargs[key]) + "\n"
       
   print(output_msg)
   print(line_sep)
greet("Amir !!", "Welcome", "How are you doing", "Have a nice day", film_1="Secret Superstar", film_2="Dangal", film_3="PK", film_4="Dhoom3")
