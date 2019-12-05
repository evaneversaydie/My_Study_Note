# Codesignal
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Codesignal](#codesignal)
    - [01](#01)
    - [02](#02)
    - [03](#03)
    - [04](#04)
    - [05](#05)
    - [06](#06)
<!-- TOC END -->

#### About this Note:
這裡是我用`python3`解[codesignal](https://app.codesignal.com/)的練習程式碼與學習歷程。

## 01
 Write a function that returns the sum of two numbers.

Example:
For param1 = 1 and param2 = 2,
the output should be add(param1, param2) = 3.

```Python
    def add(param1, param2):
        return param1+param 2
```
* 心得:return 之功能:
return 有【退出函式】的功能，執行到return(後面沒有回傳值再python 是允許的，默認傳回None)

[📔](#Codesignal)

## 02
```Python
def centuryFromYear(year):
    if year%100 != 0:
        n = int(year/100)+1
    if year%100 == 0:
        n = year//100
    return n
                    ```
* 找回python 中，數字運算的語法:
 * % :餘數
 * //:整除的商(一定是int)

[📔](#Codesignal)

## 03
```Python
def checkPalindrome(inputString):
    return inputString[::-1] == inputString
```
* note:
字串反轉:
1.使用切片
2.內建reserve()只適用於list。
palindrome:可以回文的字句。

[📔](#Codesignal)

## 04

回傳list中，相鄰的兩個元素之積的最大值。
```Python
    def adjacentElementsProduct(inputArray):
        res=[]
        for i in range(len(inputArray)-1):
            res.append(inputArray[i]*inputArray[i+1])
        return max(res)

```


## 05
- [ ] 可以使用sort
## 06
