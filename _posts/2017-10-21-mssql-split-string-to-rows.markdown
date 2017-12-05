---
layout: post
title:  MSSQL: split string to rows
created: 2017-10-21 15:57:20 +08:00
modified: 2017-10-21 16:31:46 +08:00
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


