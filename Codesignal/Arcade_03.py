
# coding: utf-8

# [題目](https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ)
# 

# Given the string, check if it is a palindrome.
# 
# # Example
# 
# >For inputString = "aabaa", the output should be
# checkPalindrome(inputString) = true;
# For inputString = "abac", the output should be
# checkPalindrome(inputString) = false;
# For inputString = "a", the output should be
# checkPalindrome(inputString) = true.
# Input/Output
# 
# * [execution time limit] 4 seconds (py3)
# 
# * [input] string inputString
#     * A non-empty string consisting of lowercase characters.
#     * Guaranteed constraints:
#         * 1 ≤ inputString.length ≤ 105.
# 
# * [output] boolean
#     *true if inputString is a palindrome, false otherwise.
# 
# # [Python3] Syntax Tips
# 
# #Prints help message to the console
# #Returns a string
# >def helloWorld(name):
#     print("This prints to the console when you Run Tests")
#     return "Hello, " + name
# 

# In[2]:


def checkPalindrome(inputString):
    return inputString[::-1] == inputString

'''字串反轉:
1.使用切片
2.內建reserve()只適用於list。
'''

'''
palindrome:可以回文的字句。
'''

