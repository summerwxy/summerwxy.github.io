---
layout: post
title:  Node.js and NPM
created:
modified:
tags: [Node.js]
---

## commands

```
檢查版本
$ node -v
$ npm -v 
---------------------------------
幫助
$ npm help
$ npm install -h
$ npm help-search update   // 找出跟update相關的指令
$ npm help update // 顯示詳細操作的網頁
----------------------------------
在空白資料夾裡面初始化
$ npm init
$ npm init --yes
--------------------------------
設定 init 裡面的預設參數
$ npm config set init-author-name “wxy”
$ npm set init-license “MIT”
$ npm config get init-author-name
$ npm get init-license
$ npm config delete init-author-name
$ npm config delete init-license
--------------------------------
安裝
$ npm install moment   // 純安裝
$ npm install monment --save // 安裝+寫到package.json
$ npm install lodash --save-dev // 安裝+寫到 package.json for DEV
```

