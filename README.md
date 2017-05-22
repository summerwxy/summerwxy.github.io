# 0_o's Pages


## memo



## local run

執行後, 訪問 http://localhost:4000
```
bundle exec jekyll serve
```


## hooks

新增檔案 .git/hooks/pre-commit 就可以自動執行 foo.py 做一些檢查工作
```
#!/bin/sh

python foo.py
```
