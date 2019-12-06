這裡整理了使用github、寫markdown以來所查詢的資料與一點點使用心得。



<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Markdown (.md檔案)](#markdown-md檔案)
  - [目前常用語法:](#目前常用語法)
  - [現在編輯[.md檔案]的方式:](#現在編輯md檔案的方式)
- [關於github使用的大小事:](#關於github使用的大小事)
  - [✍如何確認github上`.ipynb`檔案的情形?](#如何確認github上ipynb檔案的情形)
  - [✍怎麼寫好的read.me](#怎麼寫好的readme)
  - [✍怎麼使用建立目錄頁?](#怎麼使用建立目錄頁)
  - [✍gitignore教學](#gitignore教學)
<!-- TOC END -->



關於github(待更新)
==
需要建立帳號、倉庫、在電腦上裝`git`。
可以用來管理版本。
* [使用圖形化介面操作](https://progressbar.tw/posts/49)

- [ ] [要研究的]什麼是flork.....等功能
- [ ] tag功能是什麼




# Markdown (.md檔案)
### 目前常用語法:
* `>`：通常當作引言使用
      >    嗨~歡迎您來到我的學習筆記! 這邊主要紀錄一些練習的程式碼。
     效果:
     >    嗨~歡迎您來到我的學習筆記! 這邊主要紀錄一些練習的程式碼。

* `*` 點點標記
        * 這是點點的效果

     效果:
    * 這是點點的效果
* 超連結 :`[顯示文字](網址)`
         輸入文字:`[我的github] (https://github.com/evaneversaydie/My_Study_Note)

     效果 :
     [我的github](https://github.com/evaneversaydie/My_Study_Note)

* ``: 框起來的文字
       `這是框起來的字`
     效果:
     `這是框起來的字`
* 套用程式碼風格:
```
 #```Python
 #程式碼
 #```
```
效果:
```Python
這裡是顯示的效果:
def a(code):
     return code
 ```


* 更多語法可以參考:
 * [Hackmd快速入門](https://hackmd.io/s/quick-start-tw)
 * [Hackmd完整功能說明](https://hackmd.io/c/tutorials-tw/%2Fs%2Ffeatures-tw)
 * [或是這邊](https://ithelp.ithome.com.tw/articles/10203758)
 * [markdown語法](https://blog.csdn.net/u012067966/article/details/50736647)


### 現在編輯[.md檔案]的方式:
初使用`markdown`，覺得很需要即時瀏覽的功能，比較能夠知道與嘗試這些語法以及排版的效果。目前找到且有在使用的方法如下:
* 使用Atom:將Atom安裝套件即時預覽所寫的md檔案。
 * [Atom安裝](https://ithelp.ithome.com.tw/articles/10194985)
 * [用ATOM寫MD檔_推薦的套件](https://www.itread01.com/content/1544422359.html)

* 使用[Hackmd](https://hackmd.io/)網站編譯。
##### 關於圖檔使用
* 上傳至github，並使用引用圖片檔的語法
```
![若圖片無法正常顯示時顯示的文字](圖片連結)
```

* [Hackmd](https://hackmd.io/)拖曳圖檔直接把檔案上傳是網路免費空間








# 關於github使用的大小事:
### ✍如何確認github上`.ipynb`檔案的情形?
 * 上傳檔案至github，並複製檔案網址。
 * 使用[nbviewer](https://nbviewer.jupyter.org/')，在網頁內貼上自己的.ipynobook網址，即可快速閱讀自己的檔案預覽情型。
<br> [更多參考:在部落格引用ipynb程式碼](https://medium.com/@kabuto412rock/%E5%B0%87jupyter-notebook%E8%A4%87%E8%A3%BD%E5%88%B0gist%E4%B8%8A-20412d126f07)

### ✍怎麼寫好的read.me


### ✍怎麼使用建立目錄頁?
* 在atom裡，可以安裝TOC相關套件。(如:Markdown TOC Auto:Insert TOC)
* 可以使用`ctrl`+`shft`+`M`，呼叫搜尋列輸入TOC使用。
* 必須使用`#`符號的地方才會在目錄上。

### ✍[gitignore教學](https://www.youtube.com/watch?v=3FRIGBbsuxA)
* 可以指定不想被track的檔案。
* 如`.ipynb_checkpoints`、`.idea`檔。
