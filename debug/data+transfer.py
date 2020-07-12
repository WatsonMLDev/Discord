import sqlite3
import functools 
import operator
connection = sqlite3.connect("discordBot") 
crsr = connection.cursor() 

def singleData(tup):
	item = functools.reduce(operator.add,(tup))
	return item


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
    
crsr.execute("SELECT BsLoadout FROM MEMBER")
ans = crsr.fetchall()
bs = []
for i in ans:
    bs.append(singleData(i))
    
crsr.execute("SELECT Support1 FROM MEMBER")
ans = crsr.fetchall()
support1 = []
for i in ans:
    support1.append(singleData(i))
    
crsr.execute("SELECT Support2 FROM MEMBER")
ans = crsr.fetchall()
support2 = []
for i in ans:
    support2.append(singleData(i))
    	
    	
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
    	
    	
print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(name,UserName,bs,support1,support2,corp,ws))    	
print("-----------------------")
  	
crsr.execute("SELECT CorpID FROM CORP")
ans = crsr.fetchall()
CorpID = []
for i in ans:
    CorpID.append(singleData(i))    	

crsr.execute("SELECT CorpName FROM CORP")
ans = crsr.fetchall()
CorpName = []
for i in ans:
    CorpName.append(singleData(i))
    
crsr.execute("SELECT CorpLvl FROM CORP")
ans = crsr.fetchall()
CorpLvl = []
for i in ans:
    CorpLvl.append(singleData(i))

crsr.execute("SELECT WsID1 FROM CORP")
ans = crsr.fetchall()
CorpWS = []
for i in ans:
    CorpWS.append(singleData(i))
    	
print("{}\n{}\n{}\n{}\n{}".format(CorpID,CorpName,CorpLvl,CorpWS,-1))    
print("-----------------------")
crsr.execute("SELECT rowid FROM WS")
ans = crsr.fetchall()
rowid = []
for i in ans:
    rowid.append(singleData(i))    	
    
crsr.execute("SELECT NumInWs1 FROM WS")
ans = crsr.fetchall()
numws1 = []
for i in ans:
    numws1.append(singleData(i))
    
crsr.execute("SELECT WsMSG FROM WS")
ans = crsr.fetchall()
msg = []
for i in ans:
    msg.append(singleData(i))

print("{}\n{}\n{}\n{}".format(rowid,numws1,0,msg))    
	
    	
connection.commit() 

connection.close() 

"""
connection = sqlite3.connect("NEWdiscordBot") 
crsr = connection.cursor()

for i , item in enumerate(numws1):
    crsr.execute('''INSERT INTO WS(rowid,NumInWS1,NumInWS2,WsMSG) VALUES({}, {}, {}, {})'''.format(rowid[i],numws1[i],0,msg[i]))

#for i , item in enumerate(CorpID):
    #crsr.execute('''INSERT INTO CORP(CorpID,CorpName,CorpLvl) VALUES({}, \'{}\',{})'''.format(CorpID[i],CorpName[i],0,))


for i , item in enumerate(CorpID):
    crsr.execute('''INSERT INTO CORP(CorpID,CorpName,CorpLvl,WsID1,WsID2) VALUES({}, \'{}\' , {}, {},{})'''.format(CorpID[i],CorpName[i],0,CorpWS[i],-1))


for i , item in enumerate(name):
    crsr.execute('''INSERT INTO MEMBER VALUES({}, \'{}\', \'{}\', \'{}\', \'{}\', {}, {},{})'''.format(name[i],UserName[i],bs[i],support1[i],support2[i],corp[i], ws[i],0,0))

connection.commit()     


connection.close() 
"""
