"""
Requirement : Python 3.8.5

This is solution to find the regular expressions with support for '.' and '*' characters. 

I have created a simple GUI tool using tkinter. You can enter the pattern and input string and click on Process.
The program throws exceptions for invalid entries such as '*' at the beginning.

I have also wrote a test file that is not commited to the repository.
Please select the Regex.py and run the program. 
"""
from Console import * 
from RegexEntry import * 

regexEntry = RegexEntry()
getInputs(regexEntry)