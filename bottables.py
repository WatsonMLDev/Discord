import sqlite3 

connection = sqlite3.connect("NEWdiscordBot") 

# cursor 
crsr = connection.cursor() 

sql_command ="""CREATE TABLE WS (
NumInWs1 Int NOT NULL,
NumInWs2 Int NOT NULL,
WsMSG Int NULL);"""
crsr.execute(sql_command) 
connection.commit() 

sql_command ="""CREATE TABLE CORP (
CorpID Int NOT NULL PRIMARY KEY,
CorpName VarChar(100) NOT NULL,
CorpLvl Int NULL,
WsID1 Int NOT NULL,
WsID2 Int NOT NULL,

CONSTRAINT CORP_WS_FK FOREIGN KEY(WsID1)
REFERENCES WS(rowid)
ON UPDATE CASCADE

CONSTRAINT CORP_WS_FK FOREIGN KEY(WsID2)
REFERENCES WS(rowid)
ON UPDATE CASCADE
);"""
crsr.execute(sql_command) 
connection.commit() 

sql_command ="""CREATE TABLE MEMBER (
UserID Int NOT NULL PRIMARY KEY,
UserName VarChar(40) NOT NULL,
BsLoadout VarChar(200) NULL,
Support1 VarChar(200) NULL,
Support2 VarChar(200) NULL,
CorpID Int NOT NULL,
WsID Int NOT NULL,
Banned Int NOT NULL,

CONSTRAINT MEMBER_WS_FK FOREIGN KEY(WsID)
REFERENCES WS(rowid)
ON UPDATE CASCADE
CONSTRAINT MEMBER_CORP_FK FOREIGN KEY(CorpID)
REFERENCES CORP(CorpID)
ON UPDATE CASCADE
);"""
crsr.execute(sql_command) 

connection.commit() 

connection.close() 