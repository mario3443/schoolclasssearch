# schoolclasssearch - 成大課程 CLI 查詢工具

## 學習背景

這個專案一開始是想練習Python的爬蟲工具（像是requests和BeautifulSoup），原本的構想是想從成大的課程系統爬資料。不過實作到一半發現網站架構比較複雜，在網站導向的部分我找不到思路，爬蟲不太好做，就改成先用整理好的json檔來練習CLI搜尋工具。

## 功能介紹

- 使用CLI介面查詢課程資訊

- 支援輸入課程關鍵字（課號 / 課名 / 上課時間）

- 輸入後會出現相關資料供查看

![image](https://github.com/user-attachments/assets/f08f413e-b5e6-4399-afca-7eac0fc3532c)

![image](https://github.com/user-attachments/assets/1a933ff4-c910-4b2a-a061-4f9e535fc393)

## 如何使用

先clone此專案到你的資料夾中

接著直接進行主程式

``` python ncku_cli.py ```

就可以進行查詢

## 學習或利用到的資訊

### Python的requests和BeautifulSoup（雖然最後沒用上爬蟲，但在嘗試過程中學到不少）

### Selenium（簡單測試爬取學校網站，但最後失敗）

### 網頁架構觀察和json整理

### CLI 工具撰寫（初步練習用純文字互動的方式設計使用者介面）

## 注意事項

因為是使用靜態的json做紀錄，所以我只有拿化工系的mhtml去做，若要其他系所的還要重新製作json檔案
