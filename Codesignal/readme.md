# 📔Codesignal
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [📔Codesignal](#codesignal)
- [About this Note:](#about-this-note)
- [Arcade:結果與心得](#arcade結果與心得)
    - [01](#01)
    - [02](#02)
    - [03](#03)
    - [04](#04)
    - [05](#05)
- [Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)
    - [1.](#1)
    - [2.](#2)
    - [3.](#3)
    - [4.](#4)
    - [5.](#5)
    - [6](#6)
    - [7](#7)
    - [8](#8)
<!-- TOC END -->



# About this Note:
這裡是我用`python3`解[codesignal](https://app.codesignal.com/)的練習程式碼與學習歷程。

#### 練習題目
所有`筆記`與`程式碼`在[Readme](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/readme.md)中:

|章節|題號|
|--|--|
|Arcade|01|
|Arcade|02|
|Arcade|03|
|Arcade|04|
|Python|01|
|Python|02|
|Python|03|
|Python|04|
|Python|05|
|Python|06|
|Python|07|
|Python|08|

#### 資料夾中的檔案們
* 一開始寫Arcade01到04，都有另外打在`.ipnb`並打包成`py檔`。已經將他們與之後寫的題目直接紀錄在此筆記中，但仍保留學習的軌跡，留下以下檔案。可以點擊來找到它們😀:
|題號|ipnb|程式碼py|
|--|--|--|
|01|[ipnb](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_01.ipynb)|[py](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_01.py)|
|02|[ipnb](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_02.ipynb)|[py](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_02.py)|
|03|[ipnb](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_03.ipynb)|[py](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_03.py)|
|04|[ipnb](https://github.com/evaneversaydie/My_Study_Note/blob/master/Codesignal/Arcade_04.ipynb)|code直接寫在筆記囉|


# Arcade:結果與心得
- [01](#01)
- [02](#02)
- [03](#03)
- [04](#04)
- [05](#05)

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

* [返回📔-Arcade:結果與心得](#arcade結果與心得)

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

* [返回📔-Arcade:結果與心得](#arcade結果與心得)

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


* [返回📔-Arcade:結果與心得](#arcade結果與心得)


## 04

回傳list中，相鄰的兩個元素之積的最大值。
```Python
    def adjacentElementsProduct(inputArray):
        res=[]
        for i in range(len(inputArray)-1):
            res.append(inputArray[i]*inputArray[i+1])
        return max(res)

```

* [返回📔-Arcade:結果與心得](#arcade結果與心得)


## 05
- [ ] 可以使用sort看看。


* [返回📔-Arcade:結果與心得](#arcade結果與心得)


# Code_Signal:Python刷題紀錄與筆記
- [1.](#1)
- [2.](#2)
- [3.](#3)
- [4.](#4)
- [5.](#5)
- [6](#6)
- [7](#7)
- [8](#8)
##1.
[題目網址](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/CodeSignalpython01.jpg)
> ![https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/CodeSignalpython01.jpg?raw=true)
來源:[題目網址](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/CodeSignalpython01.jpg)

list中，存在元素。答案[True,False]

* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)


## 2.
[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/NWtSkp4Gd8ZeKc5R5/comments)
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/CodeSignalpython02.jpg?raw=true)
> .[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/NWtSkp4Gd8ZeKc5R5/comments)
https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/CodeSignalpython02.jpg?raw=true

這題爭議取決於對校譽的定義，如果是時間==>2;程式碼長短=>1。

* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)

## 3.
[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/2iE97RD5zdYLek4cy)
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/CodeSignalpython03.jpg?raw=true)
> [題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/2iE97RD5zdYLek4cy)

java:/中的整數除法僅返回整數，而//會到下一個“最小”整數15 / -4 = -3，15 //- 4 = -4


* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)

## 4.
[https://app.codesignal.com/arcade/python-arcade/meet-python/7bGkfoFf65CiqbX3s/solutions]()
轉成二近位。也可以用bin()
```Python
def countBits(n):
    return n.bit_length()
```
* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)

## 5.
[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/mygD2J9yDbRmtKW8T/)
```Py
def modulus(n):
    if type(n)==int:
        return n % 2
    else:
        return -1
```
* isinstance(n, int)
* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)

## 6
[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/MEgcxkQyYqFDdySnH)
```Py
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            j += 1
    return arr
```
* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)

## 7
[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/u7FW6fpp8Mqxe6sjt)!!
```Py
def baseConversion(n, x):
    return hex(int(str(n),x))[2:]
```
* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)

## 8
[題目網址](https://app.codesignal.com/arcade/python-arcade/meet-python/pLsMG462nzEh3axHN/solutions)
```Py
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found
```
* [返回📔-Code_Signal:Python刷題紀錄與筆記](#code_signalpython刷題紀錄與筆記)
