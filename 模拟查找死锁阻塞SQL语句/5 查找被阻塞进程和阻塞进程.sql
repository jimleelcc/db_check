select A.SPID as ����������,a.CMD AS ����ִ�еĲ���,b.spid AS �������̺�,b.cmd AS ������������ִ�еĲ���
from master..sysprocesses a,master..sysprocesses b
where a.blocked<>0 and a.blocked= b.spid

exec sp_who 'active'--�鿴ϵͳ�����еĻ���� BLK��Ϊ0��Ϊ����

exec sp_lock 52 --����ĳ�����̶���Դ���������

SELECT object_name(1504685104)--���ض���ID��Ӧ�Ķ�����

DBCC INPUTBUFFER (52)--��ʾ�ӿͻ��˷��͵������������һ�����