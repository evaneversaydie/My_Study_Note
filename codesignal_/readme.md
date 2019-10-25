# Codesignal
[toc]


這裡是我用`python3`解[codesignal](https://app.codesignal.com/)的練習程式碼與學習歷程。


## 01
 Write a function that returns the sum of two numbers.

Example:
For param1 = 1 and param2 = 2,
the output should be add(param1, param2) = 3.


    def add(param1, param2):
        return param1+param2

* 心得:return 之功能:
return 有【退出函式】的功能，執行到return(後面沒有回傳值再python 是允許的，默認傳回None)

[📔](#目錄)

## 02
                def centuryFromYear(year):
                    if year%100 != 0:
                        n = int(year/100)+1
                    if year%100 == 0:
                        n = year//100
                    return n
* 找回python 中，數字運算的語法:
 * % :餘數
 * //:整除的商(一定是int)

[📔](#目錄)

## 03
                def checkPalindrome(inputString):
                    return inputString[::-1] == inputString

* note:
字串反轉:
1.使用切片
2.內建reserve()只適用於list。
palindrome:可以回文的字句。

[📔](#目錄)

## 04
                def adjacentElementsProduct(inputArray):
                    res=[]
                    for i in range(len(inputArray)-1):
                        res.append(inputArray[i]*inputArray[i+1])
                        return max(res)


## 05

## 06
