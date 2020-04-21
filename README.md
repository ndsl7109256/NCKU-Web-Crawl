# NCKU-Web-Crawl
Use python selenium to get the course


## 找到目標課程並查詢餘額
![](https://i.imgur.com/EABcxlT.png)
檢查選課人數是否額滿，如果額滿則用 while 卡著，直到有餘額進行下一步。

## 輸入帳號密碼並辨識驗證碼
![](https://i.imgur.com/7HuNqN1.png)

原本想直接拿到圖片 src 再用 urllib 直接獲取圖片做驗證，但似乎有做另外的保護，使得想要 access 驗證碼圖片就會換成另一張驗證碼。
所以我就對畫面做截圖，裁切適當後，利用 pytesseract 做文字辨識，值得一提的是因為圖片有些 noise 可能會多辨識成 ' , . 等符號進去，要檢查每個char是否為 digit。

## 選課
由於選課時，server 忙碌造成擁塞，會讓 selenium 無法取得物件產生 exception ，需要做 try catch 的動作，讓網頁可以等到正常時再動作。
