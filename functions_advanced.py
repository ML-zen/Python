# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 00:26:43 2018

@author: JohnK
"""

# Basic function with 
"""
args and **kwargs in function to pass a variable number of arguments to a function. 
The single asterisk form (*args) is used to pass a non-keyworded
variable-length argument list, and the double asterisk (**kwargs form is used to pass a keyworded, variable-length argument list. Here is an example of how to use the non-keyworded form. This example passes one formal
"""

# Basic function without arguments
line_sep="##############################################"
def greet(name, msg, *args):
   print("** Basic verions of a function  with No Arguments passed **")
   print("Hello Mister/Miss, Good Morning")
   print(line_sep)
greet()
