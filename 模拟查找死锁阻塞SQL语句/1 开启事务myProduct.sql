BEGIN TRAN t1
UPDATE dbtest.dbo.myProduct SET price = price + 1 WHERE id=1

BEGIN TRAN t2
UPDATE dbtest.dbo.myBook SET price = price + 1 WHERE id=1

BEGIN TRAN t3
UPDATE dbtest.dbo.myToy SET price = price + 1 WHERE id=1