---
layout: post
title:  ExtJS getting started
created: 2017-05-11 12:37:02 +08:00
modified: 2017-05-12 14:44:35 +08:00
tags: [ExtJS]
---


## 準備

* 在[Sencha Cmd 下載畫面](https://www.sencha.com/products/extjs/cmd-download/)下載 Sencha Cmd 並安裝
* 在[ExtJS GPL 下載畫面](https://www.sencha.com/legal/GPL/)下載 GPL 版本的 ExtJS, 這個畫面在官網藏的很深不是很好找, 下載後解壓縮就好
* 接下來就可以開始新建專案了

```
>> sencha -sdk /path/to/ext6 generate app MyApp /path/to/my-app
   ====== ================== ============ ===== ===============
   exe    指定SDK位置         生成app專案   專案名 路徑

>> sencha app build
   打包起來, 會在 build 資料夾裡面

>> sencha app watch
   開發模式, 打開後訪問 [http://localhost:1841](), 瀏覽器按 F5 可以隨時看到修改情況
```

# 指令
```
>> sencha generate model User id:int,name,email
   生成 model, 路徑 app/model 下, 注意最後面的屬性部分, 不可以有空白, 要連在一起, 沒指定類型, 預設 auto

>> sencha generate view foo.Thing
   生成 view, 路徑在 app/view/foo 下, 有 Thing.js / ThingModel.js / ThingController.js

>> sencha generate controller Central
   Ext JS 5+ 之後, 生成 view 的時候, 會順便有 controller 所以不需要特別生成 global controller
   
>> sencha app upgrade path-to-new-framework
   升級 app 的 framework 版本
```

# 基本的修改
```
>> sencha -sdk /path/to/ext6 generate app MyApp /path/to/my-app
>> cd /path/to/my-app
>> sencha app watch
>> sencha generate view main.Home
```
* 修改根目錄底下 app.js MyApp.view.main.Main 相關的部分, 把預設的畫面, 改成自己產生的 main.Home
* 替換 app.json 裡面的 theme name: theme-triton, 我喜歡 theme-neptune 顏色