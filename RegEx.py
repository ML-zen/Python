# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:05:02 2018

@author: JohnK
"""


import re


text1 = "This is a beautiful day"
m = re.search('is',text1)
print(m.group())
# Print the position of the position(zero index) and end of the search string (exclusvie)
print(m.start(), m.end())
print()
print(type(m), m)


"""
The below example will use Fraudulent Email Corpus from Kaggle . It contains thousands of phising mails
"""

fh = open(r"DataSets/fradulent_emails.txt", "r").read()
# Example 1 : prints all lines with the word "From:"  
for line in re.findall("From:.*", fh):
    print(line)
    
# Example 2: prints all all names after the word "From:"
match = re.findall("From:.*", fh)
for line in match:
     print(re.findall("\".*\"", line))
     
match = re.findall("From:.*", fh)
# Example 3: prints all all email addresses after the word "From:"
for line in match:
     print(re.findall("\w\S*@.*\w", line))
     
     


