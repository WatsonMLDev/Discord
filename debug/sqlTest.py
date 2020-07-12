import sqlite3
import functools
import operator
connection = sqlite3.connect("discordBot")
crsr = connection.cursor()

def singleData(tup):
	item = functools.reduce(operator.add,(tup))
	return item
serverId = 123
user = "104"
name = "myname"
bs = "test"
sup1 = "test"
sup2 = "test"
my = "123456"
corpName = "test"
'''
crsr.execute("UPDATE MEMBER SET WsID = {} WHERE UserName LIKE \'*\'".format(-1))

'''
crsr.execute("SELECT UserID FROM MEMBER")
ans = crsr.fetchall()
name = []
for i in ans:
    name.append(singleData(i))

crsr.execute("SELECT UserName FROM MEMBER")
ans = crsr.fetchall()
UserName = []
for i in ans:
    UserName.append(singleData(i))


crsr.execute("SELECT CorpID FROM MEMBER")
ans = crsr.fetchall()
corp = []
for i in ans:
    corp.append(singleData(i))


crsr.execute("SELECT WsID FROM MEMBER")
ans = crsr.fetchall()
ws = []
for i in ans:
    ws.append(singleData(i))

print("{}\n{}\n{}\n{}".format(name,UserName,corp,ws))

print("-----------------------")
connection.commit()

connection.close()
