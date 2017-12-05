---
layout: post
title:  Screenshot as a service
created: 2017-11-25 09:10:37 +08:00
modified: 2017-11-25 09:17:22 +08:00
tags: [Node.js, Heroku]
---


#### Step 1: install utl-to-image

```
$ npm install --save url-to-image
```

利用 Phantomjs 抓網頁截圖

#### Step 2: Heroku 中文字型

因為 Heroku 系統是沒有中文的, 所以放上 Heroku 之後, 遇到中文字都會是空白的, 所以要自己提供字型

```
// 建立新資料夾
$ mkdir .fonts

// 將 ttf 格式的中文字型放進去
```

這樣操作過後, 就能正確顯示中文了


參考網頁: [基于nodejs与phantomjs在heroku搭建网页截图服务](http://bookshadow.com/weblog/2014/05/07/nodejs-phantomjs-heroku-screenshot-service/)
