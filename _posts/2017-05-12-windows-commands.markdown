---
layout: post
title:  Windows Commands
created: 2017-05-12 09:04:25 +08:00
modified: 2017-05-19 08:59:49 +08:00
tags: [Windows]
---


* 在 windows 中新增虛擬目錄, 方便把不同專案的東西放在一起使用

```
$ mklink /D E:\code\ExtJS\_posts E:\code\summerwxy.github.io\_posts
symbolic link created for E:\code\ExtJS\_posts <<===>> E:\code\summerwxy.github.io\_posts
```

* 找到並刪除某個 port 的 process, 例: 4200 port

```
$ netstat -aon | findstr :4200
  TCP    127.0.0.1:4200         0.0.0.0:0              LISTENING       10268
  TCP    127.0.0.1:4200         127.0.0.1:57073        ESTABLISHED     10268
  TCP    127.0.0.1:57073        127.0.0.1:4200         ESTABLISHED     17372

$ taskkill /pid 17372 /f
SUCCESS: The process with PID 17372 has been terminated.
```