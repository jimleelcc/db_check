SELECT  session_id ,
        text
FROM    sys.dm_exec_connections
        CROSS APPLY sys.dm_exec_sql_text
        (most_recent_sql_handle) AS ST
WHERE   session_id IN (52,59,54)
order by charindex(rtrim(session_id),'%s,%s,%s')% (52)
