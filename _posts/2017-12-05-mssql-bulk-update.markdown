---
layout: post
title:  MSSQL: bulk update
created: 2017-12-05 09:54:49 +08:00
modified: 2017-12-05 09:55:40 +08:00
tags: [SQL]
---

#### bulk update



```
UPDATE TableA SET TableA.A1 = TableB.B1, TableA.A2 = TableB.B2  FROM TableB  WHERE TableA.A3 = TableA.B3

update table 1 set 價格=b.價格 from table 1 a,table b where a.代號=b.代號
```
