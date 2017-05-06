---
layout: post
title:  在 NG2 安裝 echarts
date:   2017-05-06 16:11:00 +08:00
tags: [Angular, echarts]
---

* cmd 輸入, 會在 package.json 的 dependencies 裡面加上一行, "echarts"
```
npm install echarts --save
```
* 到 .angular-cli.json 的 scripts 裡面加上 
```js
"scripts": [
  "../node_modules/echarts/dist/echarts.min.js",
  ...
],
```
* 到 app.component.ts 上面定義, 就可以開始使用了
```ts
declare var echarts: any; 
```
