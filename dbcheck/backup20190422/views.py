from django.shortcuts import render, redirect
from django.db import connections
from functools import reduce
from django.http import HttpResponse
import xlwt


# Create your views here.
# Ctrl+Shift+[ 折叠代码
# Ctrl+Shift+] 展开代码
# Ctrl+KT 折叠属性
# Ctrl+K0 展开所有


def checkpage(request):
    curs_find_text = connections['db_mssql_162009'].cursor()
    curs_find_text.execute("select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作 \
        from master..sysprocesses a,master..sysprocesses b \
        where a.blocked<>0 and a.blocked= b.spid")
    curs_find_text_content = curs_find_text.fetchall()

    if curs_find_text_content:
            curs_find = connections['db_mssql_162009'].cursor()
            curs_find.execute("select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作 \
                from master..sysprocesses a,master..sysprocesses b \
                where a.blocked<>0 and a.blocked= b.spid")

            curs_find_content = curs_find.fetchall()

            # 将被阻塞ID和阻塞进程的id循环取值组成列表
            sid_wait = [x[0] for x in curs_find_content]
            sid_X = [x[2] for x in curs_find_content]

            # 查找被阻塞进程正在进行的sql语句
            curs_wait_sid_text = connections['db_mssql_162009'].cursor()
            str1 = 'SELECT  session_id , text  \
            FROM sys.dm_exec_connections CROSS APPLY sys.dm_exec_sql_text (most_recent_sql_handle) AS ST  \
            WHERE session_id in (%s)' % ','.join(['%s'] * len(sid_wait))
            str_order1 = '     order by charindex(rtrim(session_id),' + '\'' + str(sid_wait) + '\'' + ')'
            str_wait_sid_text = curs_wait_sid_text.execute(str1 + str_order1, sid_wait)

            # 查找和阻塞进程正在进行的sql语句
            curs_X_sid_text = connections['db_mssql_162009'].cursor()
            str2 = 'SELECT  session_id , text  \
            FROM sys.dm_exec_connections CROSS APPLY sys.dm_exec_sql_text (most_recent_sql_handle) AS ST  \
            WHERE session_id in (%s)' % ','.join(['%s'] * len(sid_X))
            str_order2 = '     order by charindex(rtrim(session_id),' + '\'' + str(sid_X) + '\'' + ')'
            str_X_sid_text = curs_X_sid_text.execute(str2 + str_order2, sid_X)

            result_wait = str_wait_sid_text.fetchall()
            result_X = str_X_sid_text.fetchall()
            result_zip = list(zip(result_wait, result_X))

            content = {'t1': result_wait, 't2': result_X, 't3': result_zip}
            # test = curs.fetchone()
            # return render(request, 'dbcheck/home.html', curs1_spid, curs2_spid)
            return render(request, 'dbcheck/checkpage.html', content)
    else:
            return render(request, 'dbcheck/checkpage.html')


def kill(request, foo_1_0):
    if request.method == "POST":
        # a = Todo.objects.get(id=每一件事_id)
        spid_kill = foo_1_0
        curs_kill = connections['db_mssql_162009'].cursor()
        curs_kill.execute("kill %s" % spid_kill)
        return redirect('dbcheck:检查页面')
    else:
        return redirect('dbcheck:检查页面')


def checkpage146245(request):
    curs_find_text = connections['db_mssql_146245'].cursor()
    curs_find_text.execute("select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作 \
        from master..sysprocesses a,master..sysprocesses b \
        where a.blocked<>0 and a.blocked= b.spid")
    curs_find_text_content = curs_find_text.fetchall()

    if curs_find_text_content:

        curs_find = connections['db_mssql_146245'].cursor()
        curs_find.execute("select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作 \
            from master..sysprocesses a,master..sysprocesses b \
            where a.blocked<>0 and a.blocked= b.spid")

        curs_find_content = curs_find.fetchall()

        sid_wait = [x[0] for x in curs_find_content]
        sid_X = [x[2] for x in curs_find_content]

        curs_wait_sid_text = connections['db_mssql_146245'].cursor()
        str1 = 'SELECT  session_id , text  \
        FROM sys.dm_exec_connections CROSS APPLY sys.dm_exec_sql_text (most_recent_sql_handle) AS ST  \
        WHERE session_id in (%s)' % ','.join(['%s'] * len(sid_wait))
        str_order1 = '     order by charindex(rtrim(session_id),' + '\'' + str(sid_wait) + '\'' + ')'
        str_wait_sid_text = curs_wait_sid_text.execute(str1 + str_order1, sid_wait)

        curs_X_sid_text = connections['db_mssql_146245'].cursor()
        str2 = 'SELECT  session_id , text  \
        FROM sys.dm_exec_connections CROSS APPLY sys.dm_exec_sql_text (most_recent_sql_handle) AS ST  \
        WHERE session_id in (%s)' % ','.join(['%s'] * len(sid_X))
        str_order2 = '     order by charindex(rtrim(session_id),' + '\'' + str(sid_X) + '\'' + ')'
        str_X_sid_text = curs_X_sid_text.execute(str2 + str_order2, sid_X)

        result_wait = str_wait_sid_text.fetchall()
        result_X = str_X_sid_text.fetchall()
        result_zip = list(zip(result_wait, result_X))

        content = {'t1': result_wait, 't2': result_X, 't3': result_zip}
        # test = curs.fetchone()
        # return render(request, 'dbcheck/home.html', curs1_spid, curs2_spid)
        return render(request, 'dbcheck/checkpage146245.html', content)
    else:
        return render(request, 'dbcheck/checkpage146245.html')


def home(request):
    return render(request, 'dbcheck/home.html')


def export(request):
    return render(request, 'dbcheck/home.html')


def checkpageclass(request):
    curs_find_text = connections['db_mssql_162009'].cursor()
    curs_find_text.execute("select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作 \
        from master..sysprocesses a,master..sysprocesses b \
        where a.blocked<>0 and a.blocked= b.spid")
    curs_find_text_content = curs_find_text.fetchall()

    if curs_find_text_content:
            curs_find = connections['db_mssql_162009'].cursor()
            curs_find.execute("select A.SPID as 被阻塞进程,a.CMD AS 正在执行的操作,b.spid AS 阻塞进程号,b.cmd AS 阻塞进程正在执行的操作 \
                from master..sysprocesses a,master..sysprocesses b \
                where a.blocked<>0 and a.blocked= b.spid")

            curs_find_content = curs_find.fetchall()

            sid_wait = [x[0] for x in curs_find_content]
            sid_X = [x[2] for x in curs_find_content]

            curs_wait_sid_text = connections['db_mssql_162009'].cursor()
            str1 = 'SELECT  session_id , text  \
            FROM sys.dm_exec_connections CROSS APPLY sys.dm_exec_sql_text (most_recent_sql_handle) AS ST  \
            WHERE session_id in (%s)' % ','.join(['%s'] * len(sid_wait))
            str_order1 = '     order by charindex(rtrim(session_id),' + '\'' + str(sid_wait) + '\'' + ')'
            str_wait_sid_text = curs_wait_sid_text.execute(str1 + str_order1, sid_wait)

            curs_X_sid_text = connections['db_mssql_162009'].cursor()
            str2 = 'SELECT  session_id , text  \
            FROM sys.dm_exec_connections CROSS APPLY sys.dm_exec_sql_text (most_recent_sql_handle) AS ST  \
            WHERE session_id in (%s)' % ','.join(['%s'] * len(sid_X))
            str_order2 = '     order by charindex(rtrim(session_id),' + '\'' + str(sid_X) + '\'' + ')'
            str_X_sid_text = curs_X_sid_text.execute(str2 + str_order2, sid_X)

            result_wait = str_wait_sid_text.fetchall()
            result_X = str_X_sid_text.fetchall()
            result_zip = list(zip(result_wait, result_X))

            content = {'t1': result_wait, 't2': result_X, 't3': result_zip}
            # test = curs.fetchone()
            # return render(request, 'dbcheck/home.html', curs1_spid, curs2_spid)
            return render(request, 'dbcheck/checkpage_class.html', content)
    else:
            return render(request, 'ddbcheck/checkpage_class.html')
