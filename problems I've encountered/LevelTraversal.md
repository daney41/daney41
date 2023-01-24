# 二元搜尋樹 - 層序走訪(Python)

#### 雖然裡面遇到的問題犯的錯可能都很基本，但也不妨作為一個程式小白的犯錯紀錄:)。

在看**二元搜尋樹**的文章時，裡面寫到了前序、中序及後序三種走訪。  
**【Day16】[資料結構]-二元搜尋樹Binary Search Tree-實作：** https://ithelp.ithome.com.tw/articles/10272982  
前面介紹時有提到層序走訪但實作並沒有寫到，因此想說自己試著來練習寫寫看。

雖然知道其走法就是從左到右一層一層往下走訪，但照邏輯並參考實作的寫法來寫的話就會變成前序的方法。  

因此去找看有沒有文章介紹到層序的寫法，很幸運地有找到下面這一篇。  
https://sites.google.com/site/zsgititit/home/python-cheng-shi-she-ji/shu-zhuang-jie-gou-python  

裡面的方法是創建一個空list，先讀取第一層的數字，並將`list[0]` print出來，再分別將`list[0]`的左右子節點的數字加進list內，之後將`list[0]`刪除，如此重複循環，直到list內為空。如下：

```python
qu = []
def levelorder(now):
    qu.append(now)
    while (len(qu)>0):
        print(qu[0].val, sep=' ', end = '')
        if qu[0].left != None:
            qu.append(qu[0].left)
        if qu[0].right != None:
            qu.append(qu[0].right)
        del qu[0]
levelorder(root)
print()
```

我以此為範本試寫了一段：
```python
def levelTraversal(self, root):
	res = []
	res.append(root)
	while len(res) > 0:
        print(res[0])
		if res[0].left:
			res.append(res[0].left)
		if res[0].right:
			res.append(res[0].right)
		del res[0]
	return res 
```
這樣得到的結果會是一個一個print出來的物件位置以及一個empty list。  
如下：
```
<__main__.BinarySearchTree object at 0x7f6e610b7b70>
<__main__.BinarySearchTree object at 0x7f6e68cabeb8>
<__main__.BinarySearchTree object at 0x7f6e610b7748>
<__main__.BinarySearchTree object at 0x7f6e5db57780>
<__main__.BinarySearchTree object at 0x7f6e68d88a58>
<__main__.BinarySearchTree object at 0x7f6e5d8f1c50>
```

但我希望能夠得到的結果是：
```
[11, 7, 15, 5, 9, 3]
```

我試著將`print(res[0])`刪掉
```python
def levelTraversal(self, root):
	res = []
	res.append(root)
	while len(res) > 0:
		if res[0].left:
			res.append(res[0].left)
		if res[0].right:
			res.append(res[0].right)
		del res[0]
	return res 
```
最後得到的結果就是empty list。  
這是因為在while迴圈內的`del res[0]`把list的內容都給刪光了。  
因此最後`return res`才會得到empty list。

發現方法不行後，我想到之前有看到一個作法是創建一個list，然後在迴圈內copy這個list,結束時再將新的list return出來。
在這個想法上，我嘗試創建兩個空list，然後將迴圈內list的內容copy到另一個list內。
因此得到下方的程式碼：

```python
def levelTraversal(self, root):
	qu = []
    res = []
	res.append(root)
	while len(res) > 0:
		qu.append(res[0])
		if res[0].left:
			res.append(res[0].left)
		if res[0].right:
			res.append(res[0].right)
		del res[0]
	return qu 
```

到這邊後感覺都差不多了，但其實這樣後得到的結果會是：
```
[<__main__.BinarySearchTree object at 0x1089a4ad0>, <__main__.BinarySearchTree object at 0x1089a5510>, 
<__main__.BinarySearchTree object at 0x1089a5850>, <__main__.BinarySearchTree object at 0x1089a5c50>, 
<__main__.BinarySearchTree object at 0x1089a5cd0>, <__main__.BinarySearchTree object at 0x1089a5c90>]
```
物件的位置的list。

但我希望得到的會是一個具可讀性的list。  
後來想到之前也有遇過一樣的問題，再加上`__str__`及`__repr__`的定義便可正常讀到內容，因此再加上`__str__`及`__repr__`的定義。  
如下：

```python
def levelTraversal(self, root):
    qu = []
    res = []
    res.append(root)
    while len(res) > 0:
        qu.append(res[0])
        if res[0].left:
            res.append(res[0].left)
        if res[0].right:
            res.append(res[0].right)
        del res[0]
    return qu

def __str__(self):
    return str(self.data)

def __repr__(self):
    return str(self)
```

這樣便可以得到完整的層序走訪數據結果：
```
[11, 7, 15, 5, 9, 3]
```

