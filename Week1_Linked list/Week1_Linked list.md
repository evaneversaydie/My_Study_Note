Linked list
===
什麼是liked list?
--
linked list(單向鏈結)是一種一元樹。
使用`node`來紀錄資料，每個`node`包含:
 * `Data`:可以是任何型態的資料，練習中以整數為例。
 * `pointer`:下一個`node`在哪裡。

藉由`pointer`，我們可以將`node`連接起來。這樣的特點使linked list在存取時，可以使用不連續的記憶體空間。使用linked list 可以使我們更能善用電腦的記憶體。也適用於需要頻繁修改順序的資料。



我們可以想像linked list像一個簡單的RPG遊戲。遊戲中，關主四散在遊戲範圍(記憶體)中。我們拿著入場卷(header)去找第一個關主存不存在。而遊戲中，只有前一關主知道下一關主的位置。也就是說，唯有遇到第N個關主，才可以知道有沒有N+1關、有的話N+1關的關卡地點又在哪裡、是什麼。



#linked list 應用
* 區塊鍊(無法得知上一個節點的資料)


# 設計linked list的想法:
1.linked list 的一開始(或是變數名稱)我們可以稱為`header`.next()是下一個位置,.value()是值。
2.預設header是pointer和value是null，一遇到null linked list就結束。

- [ ] 程式碼還有沒有想明白的地方。



練習題目:[leetcode_707]('https://github.com/evaneversaydie/My_Study_Note/blob/master/leetcode/707_Design%20Linked%20List.ipynb')(程式碼)
參考資料與其他學習資源:
--
* [蔡芸琤老師_資料結構與演算法課堂簡報](https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.p)
*  李根逸老師_簡報

* 影片:
[Introduction to Linked Lists (Data Structures & Algorithms #5)](https://www.youtube.com/watch?v=WwfhLC16bis)

* 文章:
[What’s a Linked List, Anyway?](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
什麼是QUICKSORT
想法
測試流程
流程圖
sample code 怎麼用他的packae
補充說明
代辦事項
把軌跡留清楚
釐清你怎麼學習的
每天做一點事
外務(安排)
