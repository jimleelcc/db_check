SELECT  session_id ,
        connect_time ,
        last_read ,
        last_write ,
        most_recent_sql_handle
FROM    sys.dm_exec_connections
 
WHERE   session_id IN ( 60, 67 )