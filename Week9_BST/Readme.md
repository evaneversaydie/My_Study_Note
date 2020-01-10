# Binary Search Tree
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Binary Search Tree](#binary-search-tree)
- [關於 Binary Search Tree](#關於-binary-search-tree)
 - [尋值](#尋值)
 - [應用:](#應用)
 - [什麼是`pre-order`、`深度優先搜尋`?](#什麼是pre-order深度優先搜尋)
- [示意圖](#示意圖)
- [參考資料](#參考資料)
<!-- TOC END -->


# 關於 Binary Search Tree
* Binary Tree(二元樹)指的是每一個節點最多只有兩個小孩。
* Binary Search Tree(二元搜尋樹)是一個每個節點左小孩都<節點本身，而右小孩都比節點還大。
## 尋值
* BST的最小值位置:從root開始一直往左邊找找找(中間都不可以往右邊找)，找到的節點就是整個BST的最小值。
* BST的最大值位置:從root開始一直往右邊找找找(中間都不可以往左邊找)，找到的節點就是整個BST的最小值。
## 應用:
因為有規則可以搜尋，所以往往應用於資料庫中。其中BST適合「越亂越好」的資料(如果是sort好的資料去建BST的話容易產生worst case=>linked_list)
## 什麼是`pre-order`、`深度優先搜尋`?
<br> `pre-order`是一種遍訪tree的方式，先印出自己(root)再印左邊、右邊。不限於BST使用。
<br> 如圖:

![image](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg?raw=true)
[圖片沒有正常顯示請點此處看原圖>~<](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg)
<br>深度優先搜尋是先往下尋找(每一個節點找到最深的地方再去找其他分支)
<br>圖片中紅筆的方向仕紳度優先。廣度優先搜尋則是綠色的方向。使用哪一種搜尋法，則在這個方向的節點將被優先搜尋到。

# 示意圖
![HW3_BST_flow.jpg](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_BST_flow.jpg?raw=true)
# 實作:
## def說明

### 新增: `insert`(self,root,val)
*  功能: 新增節點至對的位置。
<br>(位置要符合二元搜尋樹的定義——所有的左邊的節點<Node本人
<右邊節點)
*  case:
 * **root 不存在:**
 <br>(例如原本只有一個root的樹在歷經修改等等之後被刪掉了)
 <br>=>新增一個TreeNode在root的位置
 <br>=> return TreeNode(val)
 * **root 存在且root.left/root.right 為None:**
 <br> => 新增一個TreeNode(val)在右邊或左邊
 <br> => return TreeNode(val)
 *  **root 存在但root.left/root.right 為None:**
  <br>=> `遞迴`
  <br>=> 直到符合case2

<font color=red></font>

### 查詢: `search`(self, root, target)
*  功能: 給予想尋找的目標，二元搜尋樹中有沒有這個值，若有找到則回傳那一個被搜尋的節點。
*  case:
 * **找不到目標:**
<br> 代表樹裡面沒有這個值。
 * **找到目標:**
<br> 回傳找到的節點。

<註>
<br>
* root.val==target  => return root
*  target > root.val =>往root.right找=>`遞迴` = > search (self.search(root.right,target))
*  root不存在 => return None
*  root存在但是root.val == None => return None
* root.left、root.right有可能是None，遇到None=>None

### 刪除:`delete`(self, root, target)
當樹可以新增和查詢後，就可以刪除節點了~覺得delete比較複雜。
*  功能: 完全刪掉BST中值跟target一樣的節點。
*  case:
 * **沒有值==Target的節點**: 樹裡面呒有這個值，整棵樹沒有刪除任何節點。

 * **Target存在且為葉子**: 直接刪掉這個節點。
 * **Target存在且有一個小孩**:
 <br>刪掉Node，並重新把小孩的爸爸變成原本Node的爸爸。
 <br>如果Target是整棵樹的根，小孩變成根。
 * **Target存在且有兩個小孩**:
  <br>刪掉Node，原本Node的地方變成predecessor，避免樹的結構被破壞。
  <br>predecessor
  從原本位置換到Node位置 ，所以在原本predecessor的位置也會變成沒有值。
  <br>如果Target是整棵樹的根，也是一樣的:刪掉Node，找到下面predecessor是誰並把predecessor移到root。


### 修改: `modify`(self, root, target, new_val)

*  功能: 把樹中值是target的Node通通改成new_val。並且修改後的樹需要重新排成一個符合BST的樹。

*  case:
 * **沒有值==Target的節點**: 沒有修改任何節點。
 <br>
 * **有值==Target的節點**:
   * Step1:找到所有noed.val==Target的節點。(使用search 遞迴)<br>
   *　Step2:由於修改值可能導致整個BST被破壞。
修改後，需要重新排建立出一個BST，並把新的root回傳。

### 其他小工具
* searchwithparent:功能和搜尋相同。但多記錄了要找的node的parent。用來幫忙delete()。
* pre_order:把樹用pre-order的方式印出來。
* letbst1:回傳一個list，用來提供modify()重建BST
### 程式碼
```Python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def child_count(self):
        count = 0
        if self.right:
            count+=1
        if self.left:
            count+=1
        return count
    #count有0、1、2三種值。

#Node分為:不存在、樹根、節點


class Solution(object):

    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val != None: #改成not root.val
            if val<=root.val :
                if root.left==None:
                    root.left=TreeNode(val)
                    return root.left
                else:
                    # root = root.left
                    return self.insert(root.left, val) #2\3\4
            elif val>root.val:
                if root.right==None:
                    root.right =TreeNode(val)
                    return root.right
                else:
                    #root = root.right
                    return self.insert(root.right,val) #2\3\4
        else:
            root.val = val #非TreeNode
            return root #4
 ####################################################################################

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if not root:
            return None
        if root.val == None: #if not root.val
            return None
        if root.val == target:
            return root ####################非return target
        if target > root.val: #要找的值比root大
            return self.search(root.right,target) #往右邊找
        if target <= root.val:
            return self.search(root.left,target) #往左邊找
 ####################################################################################

    def searchwithparent(self,root,target,parent=None):

        if not root:
            return None,None
        if root.val == None: #if not root.val
            return None,None
        if root.val == target:
            return root,parent #############非return target
        if target > root.val: #要找的值比root大
            return self.searchwithparent(root.right,target,root) #往右邊找，parent變成root
        if target <= root.val:
            return self.searchwithparent(root.left,target,root) #往左邊找，parent變成root

#==================================================================================
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        node,p =self.searchwithparent(root,target)

        if node == None:
            return root

        while node:  
            #node,p =self.searchwithparent(root,target)
            #刪掉根
            if p == None:
                if node.child_count() ==0:
                    node.val = None

                elif node.child_count() ==1:
                    if node.right:
                        new_root = node.right
                    else:
                        new_root = node.left
                    del node
                    root = new_root

                elif node.child_count() ==2:
                    predecessor = node.left
                    predecessor_p = node
                    #這行要先有，否則沒有先宣告不符合進入while loop 條件
                    #會出現'local variable 'predecessor_p' referenced before assignment'
                    while predecessor.right:
                        predecessor_p = predecessor
                        predecessor = predecessor.right

                    if predecessor_p.left == predecessor:
                        node.val = predecessor.val
                        node.left = predecessor.left
                        del predecessor
                    elif predecessor_p.right == predecessor:
                        node.val = predecessor.val
                        #predecessor_p.left = predecessor.right  #left打成lfet
                        predecessor_p.right = predecessor.left
                        del predecessor
                    root = node


           #不是root     
            if p:    
                if node.child_count() == 0: ##不是node.child_count
                    if p.left == node:
                        p.left = None
                        del node
                        #return root
                    elif p.right == node:
                        p.right = None
                        del node
                        #return root

                elif node.child_count() == 1: ##不是node.child_count
                    #找小孩在左邊還是右邊
                    if node.left: #打錯字有改
                        child = node.left
                    else:
                        child = node.right

                    if p.left == node:
                        p.left = child
                        #return root
                    elif p.right ==node:
                        p.right = child
                        #return root
                    del node         

                elif node.child_count() == 2: ##不是node.child_count
                    predecessor = node.left
                    predecessor_p = node
                    while predecessor.right:
                        predecessor_p = predecessor #這一橫要比較早，否則predecssor就不是原本的值了
                        predecessor = predecessor.right
                    #node.val = predecessor.val
                    if predecessor_p.left == predecessor:
                        node.val = predecessor.val
                        predecessor_p.left = predecessor.left
                        del predecessor
                    else:
                        node.val = predecessor.val
                        predecessor_p.right=predecessor.left
                        del predecessor     
            node,p =self.searchwithparent(root,target)
        return root  

  ####################################################################################

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        '''if target == new_val:
            return root
        '''
        node = self.search(root,target)
        if node == None:
            return root
        while node:
            node.val = new_val
            node = self.search(node.left,target)#直接荀子樹以免erro，不是:node = self.search(root.left,target)
            #一值修改直到沒有值== target
        unsort = self.pre_order(root,[])
        sort = sorted(unsort)
        root = TreeNode(self.letbst1(root,sort,[])[0])
        for i in self.letbst1(root,sort,[])[1:]:
            self.insert(root,i)
        return root

    def pre_order(self,root,array):
        array.append(root.val)
        if root.left:
            #self.pre_order(root,array)
            self.pre_order(root.left,array)
        if root.right:
            #self.pre_order(root,array)
            self.pre_order(root.right,array)
        return array

    def letbst1(self,root,array,resl):   
        if len(array)>=1:
            a = len(array)//2
            res = array[a]
            resl.append(res)
            #resl.append(res)
            self.letbst1(root,array[a+1:],resl)
            self.letbst1(root,array[:a],resl)
        return resl

```
# 參考資料
###### tree:

* [演算法圖鑑](https://www.books.com.tw/products/0010771263)
* [What is the worse-case time complexity for a binary search tree for searching?](https://www.quora.com/What-is-the-worse-case-time-complexity-for-a-binary-search-tree-for-searching)
* [二元搜尋樹](https://zh.wikipedia.org/zh-tw/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)
* [Binary Tree](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html)
* [How to Implement a Binary Search Tree in Python
](https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533)
* [BinarySearchTree.py on github](https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py)
* [Binary Search Tree library in Python](https://www.laurentluce.com/posts/binary-search-tree-library-in-python/)
###### python 物件:
* ['物件導向程式設計'](https://kaochenlong.com/2011/10/13/python-oop/)
* [positional argument vs keyword argument](https://blog.csdn.net/lanchunhui/article/details/50039769)
* [Python，你到底是在__底線__什麼啦！](https://aji.tw/python%E4%BD%A0%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8__%E5%BA%95%E7%B7%9A__%E4%BB%80%E9%BA%BC%E5%95%A6/)
###### 印出tree:(最後用pycharm debug)
* ['Python nltk -- Tree'](http://cpmarkchang.logdown.com/posts/184948-python-nltk-tree)
* ['python 按圖形列印二叉樹'](https://www.itread01.com/content/1547977526.html)

###### markdown:
* [如何使用 Markdown 來撰寫 Docs](https://docs.microsoft.com/zh-tw/contribute/how-to-write-use-markdown)

###### 自己的流程圖圖片
* [pre-order、深度優先搜尋](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg)
- [流程圖原圖](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_BST_flow.jpg)-
- [流程圖手繪部分search](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_3.jpg?raw=true)
- [流程圖手繪部分delete](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_5.jpg?raw=true)
- [流程圖手繪部分modify](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_4.jpg?raw=true)
