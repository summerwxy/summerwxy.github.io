---
layout: post
title:  MSSQL code snipplets
created: 2017-05-20 10:09:15 +08:00
modified: 2017-05-20 10:12:43 +08:00
tags: [SQL]
---


#### split string to rows
```

CREATE FUNCTION [udf_SplitByXml] (@Data NVARCHAR(MAX), @Delimiter NVARCHAR(5))
RETURNS @Table TABLE ( Data NVARCHAR(MAX), SequentialOrder INT IDENTITY(1, 1))
AS
BEGIN

    DECLARE @TextXml XML;
    SELECT @TextXml = CAST('<d>' + REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(@Data, '&', '&amp;'), '<', '&lt;'), '>', '&gt;'), '"', '&quot;'), '''', '&apos;'), @Delimiter, '</d><d>') + '</d>' AS XML);

    INSERT INTO @Table (Data)
    SELECT Data = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(RTRIM(LTRIM(T.split.value('.', 'nvarchar(max)'))), '&amp;', '&'), '&lt;', '<'), '&gt;', '>'), '&quot;', '"'), '&apos;', '''')
    FROM @TextXml.nodes('/d') T(Split)

    RETURN
END

SELECT * FROM udf_SplitByXml('yes, no, maybe, so', ',');
SELECT * FROM udf_SplitByXml('who|what|where|when|why|how|Uh, I don''t know!', '|');
SELECT * FROM udf_SplitByXml('Government, Education, Non-profit|Energy & Power|Yes|No', '|');
SELECT * FROM udf_SplitByXml('Energy & Power|Some<Thing>Wicked''This"Way Comes', '|');
```


#### sp_tablespace



```
--名字：    sp_tablespace
--功能：    列出當前數據庫所有表的行數、大小、數據及索引佔用的空間等
--使用說明：
--          1、創建sp_tablespace
--             在查詢分析器裡,選擇master數據庫,將所有語句複製進去並
--             運行，即在master數據庫中生成sp_tablespace。
--          2、選擇您需要分析的的數據庫，鍵入sp_tablespace並運行。
--             （以後再次運行時,因sp_tablespace已創建,請跳過第一步）   
--創建時間：2005/07/19 Add by DCMS

create procedure sp_tablespace 

as  
  
create table #spt_space  
(
 id int null,
 type char(10) null,
 name sysname null, 
 rows  int null,  
 reserved dec(15) null,  
 used dec(15) null,
 data  dec(15) null,  
 indexp  dec(15) null,  
 unused  dec(15) null  
)  

 create table #spt_space2  
(
 id int null,
 type char(10) null,
 name sysname null, 
 rows  int null,  
 reserved dec(15) null,
 used dec(15) null,  
 data  dec(15) null,  
 indexp  dec(15) null,  
 unused  dec(15) null  
)  

 insert into #spt_space (id,type,name)
 select id,xtype,name
  from sysobjects  
  
 insert into #spt_space2 (id,type,name)
 select id,xtype,name
  from sysobjects  
   
set nocount on  
 
DBCC UPDATEUSAGE (0) WITH NO_INFOMSGS 

 insert into #spt_space2 (id,reserved)
  select B.id,sum(sysindexes.reserved)  
   from sysindexes,#spt_space B 
    where indid in (0, 1, 255)  
     and sysindexes.id = B.id group by B.id
  
  insert into #spt_space2 (id,data) 
   select B.id,sum(sysindexes.dpages)  
   from sysindexes,#spt_space B  
    where indid < 2  
     and sysindexes.id =  B.id  group by B.id 
     
 insert into  #spt_space2 (id,data)
   select B.id,isnull(sum(sysindexes.used), 0)  
  from sysindexes,#spt_space B  
   where indid = 255  
    and sysindexes.id =  B.id  group by B.id 
  
  insert into  #spt_space2 (id,used)
     select B.id,sum(sysindexes.used)  
    from sysindexes,#spt_space B  
     where indid in (0, 1, 255)  
      and sysindexes.id =  B.id  group by B.id         
  
 delete from #spt_space
 
 insert into #spt_space select id,max(type),max(name),sum(rows),
     sum(reserved),sum(used),sum(data),sum(indexp),sum(unused) from #spt_space2 group by id
  
 update #spt_space  
  set unused =reserved - used  
 
update #spt_space  
  set indexp =used - data   
         
 update #spt_space set rows = i.rows  
   from sysindexes i,#spt_space B
    where i.indid < 2  
     and i.id =  B.id  
 
 delete from #spt_space where isnull(reserved,0)=0
  
 update #spt_space set type='系統表' where type='S'
 
 update #spt_space set type='用戶表' where type='U'
  
 select  #spt_space.id,'類型'=#spt_space.type,'名字'=#spt_space.name,
  '行數' = convert(char(11), rows),  
  '分配空間' = ltrim(str(reserved * d.low / 1024.,15,0) +  
    ' ' + 'KB'),  
  '已使用空間' = ltrim(str(used * d.low / 1024.,15,0) +  
    ' ' + 'KB'),
  '未使用空間' = ltrim(str(unused * d.low / 1024.,15,0) +  
    ' ' + 'KB'),  
  '數據使用' = ltrim(str(data * d.low / 1024.,15,0) +  
    ' ' + 'KB'),  
  '索引使用' = ltrim(str(indexp * d.low / 1024.,15,0) +  
    ' ' + 'KB')
 from #spt_space, master.dbo.spt_values d  
  where d.number = 1  
   and d.type = 'E' order by reserved DESC     
  
return (0) -- sp_tablespace

```