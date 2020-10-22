#!/usr/bin/env python
# -*- coding:utf-8 -*-

import happybase
#默认自动与hbase建立socket连接
#conn=happybase.Connection('127.0.0.1')
#手动进行连接
conn=happybase.Connection('127.0.0.1',autoconnect=False)
conn.open()
print (conn.tables())
# conn.create_table(
#     'lrx_test',
#     {
#     'date':dict()
#     }
# )
table0=conn.table('lrx_test')
print(table0)
table=happybase.Table('lrx_test',conn)
print (table)

for i in  range(5):
    table.put('row%s' % i, {'date:%s' % i: '%s' % i})
table.put('row5', {"date:5": 'value1'})
content=table.cells('row1', 'date:1')
print (content)

scanner=table.scan()
for k,v in scanner:
    print (k,v)
