---
layout: post
title:  MSSQL: clear SQL log files
created: 2017-10-21 15:57:20 +08:00
modified: 2017-10-21 16:31:46 +08:00
tags: [SQL]
---

#### sp_tablespace



```
DUMP TRANSACTION 数据库名 WITH NO_LOG
BACKUP LOG 数据库名 WITH NO_LOG
DBCC SHRINKDATABASE(数据库名)
EXEC sp_dboption '数据库名', 'autoshrink', 'TRUE' 
```
