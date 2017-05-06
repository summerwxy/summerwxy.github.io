---
layout: post
title:  關於 Github Pages + Jekyll
date:   2017-05-06 11:30:00 +08:00
tags: [Jekyll]
---

### 安裝本地運行環境

* 到 [Ruby Downloads 頁面](http://rubyinstaller.org/downloads/) 下載安裝 RubyInstaller + Development Kit
* Development Kit 安裝方式, 解壓縮目錄, 然後 cmd 畫面中輸入
```
dk init
dk install
```

* 安裝 Jekyll
```
gem install jekyll bundler
jekyll new my-awesome-site
cd my-awesome-site
bundle update # 如果有狀況用這兩行, 更新 lib
bundle install # 重新安裝 lib
bundle exec jekyll serve # 訪問 http://localhost:4000/
```

* 預設使用 Minima theme

### 上傳到 Github

* 建新的 [Repository: summerwxy.github.io](https://github.com/summerwxy/summerwxy.github.io)
* 到 Settings / Options / GitHub Pages 設定, 個人的 Pages 不能改 branch
* 把上個步驟生成的檔案放上去, github 會自動在主機上產生

### 其他有用的網頁

* [Highlight 支援的清單](https://haisum.github.io/2014/11/07/jekyll-pygments-supported-highlighters/)
* [Jekyll 內建變數](https://jekyllrb.com/docs/variables/)


