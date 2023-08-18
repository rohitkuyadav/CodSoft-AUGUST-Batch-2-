import random
"""
random module provide the random digit between the numbers
"""
import string
"""
String module provides various string-related constants, functions, and classes.
It includes a set of string constants, such as ASCII letters, digits, 
"""

print("----- || Random Password Generator || ----- \n")
size = int(input("Enter password length: "))  

lower_chr = string.ascii_lowercase
upper_chr = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower_chr + upper_chr + num + symbols

password = "".join(random.sample(all,size)) 

print(f"Generated Password is: {password} \n")