
# coding: utf-8

# [題目練習](https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN)

# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
# 
# # Example
# 
# > For year = 1905, the output should be
# centuryFromYear(year) = 20;
# For year = 1700, the output should be
# centuryFromYear(year) = 17.
# Input/Output
# 
# * [execution time limit] 4 seconds (py3)
# 
# * [input] integer year
#     * A positive integer, designating the year.
#     * Guaranteed constraints: 1 ≤ year ≤ 2005.
# 
# * [output] integer
#     * The number of the century the year is in.
# 
# # [Python3] Syntax Tips
# 
# #Prints help message to the console
# #Returns a string
# >def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name

# In[ ]:


def centuryFromYear(year):
    if year%100 != 0:
        n = int(year/100)+1
    if year%100 == 0:
        n = year//100
    return n 
"""
找回python 中，數字運算的語法:
1.%:餘數
2.//:整除的商(一定是int)
"""

