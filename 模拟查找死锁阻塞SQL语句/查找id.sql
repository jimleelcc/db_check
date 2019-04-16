SELECT  request_session_id AS 会话id ,
        resource_type AS 请求锁定的资源类型 ,
        resource_description AS 描述 ,
        request_mode AS 模式 ,
        request_status AS 状态
FROM    sys.dm_tran_locks