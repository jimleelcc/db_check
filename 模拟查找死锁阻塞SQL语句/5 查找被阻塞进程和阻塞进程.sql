select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作
from master..sysprocesses a,master..sysprocesses b
where a.blocked<>0 and a.blocked= b.spid

exec sp_who 'active'--查看系统内所有的活动进程 BLK不为0的为死锁

exec sp_lock 52 --返回某个进程对资源的锁定情况

SELECT object_name(1504685104)--返回对象ID对应的对象名

DBCC INPUTBUFFER (52)--显示从客户端发送到服务器的最后一个语句