from django.shortcuts import render, redirect
from django.db import connections


# Create your views here.


def home(request):
    # curs = connections['db_mssql_126'].cursor()
    # curs.execute("SELECT TOP 10 * FROM [aws].[dbo].[StationPar] order by StationID asc")

    # 查找阻塞进程
    curs_wait = connections['db_mssql_162009'].cursor()
    curs_wait.execute("SELECT  request_session_id AS 会话id , \
        resource_type AS 请求锁定的资源类型 , \
        resource_description AS 描述 , \
        request_mode AS 模式 , \
        request_status AS 状态 \
    FROM    sys.dm_tran_locks \
    where request_status = 'WAIT' order by resource_description desc")

    # 查找因锁定导致wait的运行中的事务
    curs_X = connections['db_mssql_162009'].cursor()
    curs_X.execute("SELECT  request_session_id AS 会话id , \
        resource_type AS 请求锁定的资源类型 , \
        resource_description AS 描述 , \
        request_mode AS 模式 , \
        request_status AS 状态 \
    FROM    sys.dm_tran_locks \
    where request_mode = 'X' order by resource_description desc")

    curs_wait_spid = int(curs_wait.fetchall()[1][0])
    curs_X_spid = int(curs_X.fetchall()[1][0])
    # curs1_spid_int = int(curs1_spid)
    # curs2_spid_int = int(curs2_spid)

    # 查找堵塞进程
    curs_wait_sql = connections['db_mssql_162009'].cursor()
    curs_wait_sql.execute("SELECT  session_id , \
        text \
    FROM    sys.dm_exec_connections \
        CROSS APPLY sys.dm_exec_sql_text \
        (most_recent_sql_handle) AS ST \
    WHERE   session_id IN ('%s')" % (curs_wait_spid))

    # 查找导致锁定的事务
    curs_X_sql = connections['db_mssql_162009'].cursor()
    curs_X_sql.execute("SELECT  session_id , \
        text \
    FROM    sys.dm_exec_connections \
        CROSS APPLY sys.dm_exec_sql_text \
        (most_recent_sql_handle) AS ST \
    WHERE   session_id IN ('%s')" % (curs_X_spid))

    # curs1_spid = {'spid1': curs1.fetchone()[0]}
    # curs2_spid = {'spid2': curs2.fetchone()[0]}

    # 取得SQL语句
    curs_wait_sqltext = curs_wait_sql.fetchall()[0][1]
    curs_X_sqltext = curs_X_sql.fetchall()[0][1]

    content = {'t1': curs_wait_spid, 't2': curs_X_spid, 't3': curs_wait_sqltext, 't4': curs_X_sqltext}
    # test = curs.fetchone()
    # return render(request, 'dbcheck/home.html', curs1_spid, curs2_spid)
    return render(request, 'dbcheck/home.html', content)
