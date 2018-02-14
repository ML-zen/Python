# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:05:02 2018

@author: JohnK
"""

"""
The below example will use Fraudulent Email Corpus from Kaggle . It contains thousands of phising mails
"""

import re


text1 = "This is a beautiful day"
m = re.search('is',text1)
print(m.group())
# Print the position of the position(zero index) and end of the search string (exclusvie)
print(m.start(), m.end())
print()
print(type(m), m)