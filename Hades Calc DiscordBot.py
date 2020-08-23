import functools
import operator
import sqlite3
from planetlists import planet_cap,planet_lvl,transfer,temp,credit_per_hour,planet_cost,max_levels_planet
import time
import datetime
import discord
import discord.utils
from discord.ext.commands import has_permissions
from discord.ext import commands
from os.path import join


class Planet:
    def __init__(self,level = 0,storage = 0,credit_per_hour = 0,cost = 0,types = 'desert',tier = 1):
        self.level = level
        self.storage = storage
        self.credit_per_hour = credit_per_hour
        self.cost = cost
        self.types = types
        self.tier = tier

    def __str__ (self):
        return ('level: '+ self.level + ', storage cap: ' + self.storage + ', credits per hour: ' + self.credit_per_hour + ', cost to upgrade: ' + self.cost + ', Planet type: ' + self.types + ', planet tier: ' + self.tier)

    def set_planet_lvl(self,level):
        self.level = level
    def get_planet_lvl(self):
        return(self.level)
    def set_planet_cost(self,cost):
        self.cost = cost
    def get_planet_cost(self):
        return(self.cost)
    def set_planet_storage(self,storage):
        self.storage = storage
    def get_planet_storage(self):
        return(self.storage)
    def set_planet_credit_per_hour(self,credit_per_hour):
        self.credit_per_hour = credit_per_hour
    def get_planet_credit_per_hour(self):
        return(self.credit_per_hour)
    def get_planet_types(self):
        return(self.types)
    def get_planet_tier(self):
        return(self.tier)

class Enter:
    async def get_input_of_type(func,ctx):
        channel = ctx.channel
        def check(m):
            if (m.content == 'Stop') or (m.content == 'stop') or (m.content == 'STOP'):
                raise AbortWait
            return m.content == m.content and m.channel == channel and m.author == ctx.author

        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue


class Error(Exception):
    pass
class AbortWait(Error):
    pass
class NotFound(Error):
    pass

def singleData(tup):
    item = functools.reduce(operator.add,(tup))
    return item


with open("token.txt", 'r') as token_reader:
    TOKEN = token_reader.readlines()
    TOKEN = TOKEN[0]

client = commands.Bot(command_prefix='$')

client.remove_command('help')





@client.event  # event decorator/wrapper
async def on_ready():

    global betauri
    await client.change_presence(activity = discord.Game(name = 'Type ''$help'' for a list of commands!'))
    print(f"We have logged in as {client.user}")

@client.command()
async def greet(ctx):
    await ctx.send('Hello!!!, {}'.format(round(client.latency, 1)))

@client.command()
@commands.has_any_role("Discord Admins","First Officer")
async def betauri_logout(ctx):

    await client.close()
#---------------------------------------------------------------------------------------------------------
@client.command()
async def playeradd(ctx):
    channel = ctx.channel
    user = str(ctx.message.author.id)
    name ='@' + str(ctx.message.author)
    serverId = ctx.guild.id
    guild= ctx.guild
    member = ctx.message.author
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    '''
    role = discord.utils.get(ctx.guild.roles, name="WS1")
    await member.add_roles(role)
    '''
    crsr.execute("SELECT UserName FROM MEMBER")
    ans = crsr.fetchall()
    exsName = []

    for i in ans:
        exsName.append(singleData(i))

    if name in exsName:
        correct_in = False
        while correct_in == False:
            await channel.send('Your info is all ready added')
            await channel.send('Would you like to edit your data (y/n):')
            await channel.send("to exit the program at any time, type... Stop")
            edit = await Enter.get_input_of_type(str,ctx)
            edit = edit.lower()
            if edit == 'y' or edit == 'Y':
                await channel.send('Here is an example info sheet...')
                await channel.send("```\nCharlie#3890\nBs: dual2,delta4,emp6,barrier2\nminer: enrich, remotemining,boost\ntrans: barrier2```--------------------------------------------------")
                time.sleep(1)
                await channel.send('Now you will fill in the data asked by each prompt, note: modules are not formated in a specfic way...')
                time.sleep(.5)
                await channel.send('type bs mods, example...')
                await channel.send('bs: battery10,delta4,tw1,barrier1')
                bs = await Enter.get_input_of_type(str,ctx)

                await channel.send('type first support ship mods, example...')
                await channel.send('miner: tw1,genesis1')
                sup1 = await Enter.get_input_of_type(str,ctx)

                await channel.send('type second support ship mods, example...')
                await channel.send('trans: tw1,dispatch1')
                sup2 = await Enter.get_input_of_type(str,ctx)

                crsr.execute("UPDATE MEMBER SET UserID = {}, BsLoadout = \'{}\', Support1 = \'{}\', Support2 = \'{}\', CorpID = {} WHERE UserName LIKE \'{}\' ".format(user,bs,sup1,sup2,serverId,name))
                connection.commit()
                connection.close()


                role = discord.utils.get(ctx.guild.roles, name="WSready")
                await member.add_roles(role)


                await channel.send("Your entry has been recorded!")
                correct_in = True
            elif edit == 'n' or edit == 'N':
                break
            else:
                correct_in = False

    else:
        sql_command = ('''INSERT INTO MEMBER(UserID,UserName,CorpID,WsID,Banned) VALUES({}, \'{}\', {}, {}, {})'''.format(user,name,serverId, -1,0))
        crsr.execute(sql_command)
        connection.commit()
        connection.close()


        role = discord.utils.get(ctx.guild.roles, name="WSready")
        await member.add_roles(role)


        await channel.send("Your entry has been recorded!")
        '''await channel.send('Would you like to enter bs, trans,and miner data at this time? (type y or n)')
        simple = await Enter.get_input_of_type(str,ctx)
        simple = simple.lower()
        if simple == 'n':
            sql_command = (INSERT INTO MEMBER(UserID,UserName,CorpID,WsID,Banned) VALUES({}, \'{}\', {}, {}, {}).format(user,name,serverId, -1,0))
            crsr.execute(sql_command)
            connection.commit()
            connection.close()


            role = discord.utils.get(ctx.guild.roles, name="WSready")
            await member.add_roles(role)


            await channel.send("Your entry has been recorded!")
        else:
            await channel.send('Here is an example info sheet...')
            await channel.send("```\nCharlie#3890\nBs: dual2,delta4,emp6,barrier2\nminer: enrich, remotemining,boost\ntrans: barrier2```--------------------------------------------------")
            time.sleep(1)
            await channel.send('Now you will fill in the data asked by each prompt, note: modules are not formated in a specfic way...')
            await channel.send("to exit the program at any time, type... Stop")
            await channel.send('---------------------------------------------------------------------------------------')
            time.sleep(.5)
            await channel.send('type bs mods, example...\nbs: battery10,delta4,tw1,barrier1')
            bs = await Enter.get_input_of_type(str,ctx)

            await channel.send('type first support ship mods, example...')
            await channel.send('miner: tw1,genesis1')
            sup1 = await Enter.get_input_of_type(str,ctx)

            await channel.send('type second support ship mods, example...')
            await channel.send('trans: tw1,dispatch1')
            sup2 = await Enter.get_input_of_type(str,ctx)

            sql_command = (INSERT INTO MEMBER VALUES({}, \'{}\', \'{}\', \'{}\', \'{}\', {}, {}, {}).format(user,name,bs,sup1,sup2,serverId, -1,0))
            crsr.execute(sql_command)
            connection.commit()
            connection.close()


            role = discord.utils.get(ctx.guild.roles, name="WSready")
            await member.add_roles(role)


            await channel.send("Your entry has been recorded!")'''

#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(manage_roles=True)
async def register(ctx):

    channel = ctx.channel
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id
    print(serverId)
    crsr.execute("SELECT CorpID FROM CORP")
    ans = crsr.fetchall()
    exsName = []

    for i in ans:
        exsName.append(singleData(i))

    print(exsName)
    if serverId in exsName:
        await channel.send('Your Corp is already registered with the bot')
        connection.close()
    else:
        await channel.send('What is your Corp\'s name?')
        corpName = await Enter.get_input_of_type(str,ctx)

        sql_command = ('''INSERT INTO CORP VALUES({}, \'{}\', {}, {}, {});'''.format(serverId, corpName, 'null',-1,-1))
        crsr.execute(sql_command)

        connection.commit()
        connection.close()

        guild = ctx.guild
        await guild.create_role(name="WSready")
        await guild.create_role(name="WS1")
        await guild.create_role(name="WS2")


        await channel.send('Your corp is registered with the bot!')

#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(manage_roles=True,ban_members=True)
async def wsstart(ctx):
    channel = ctx.channel
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id
    crsr.execute("SELECT WsID1 FROM CORP WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    wsCheck = singleData(ans[0])
    print(wsCheck)

    user = str(ctx.message.author.id)
    name ='@' + str(ctx.message.author)
    crsr.execute("SELECT UserName FROM MEMBER")
    ans = crsr.fetchall()
    exsName = []

    for i in ans:
        exsName.append(singleData(i))

    if name in exsName:
        if wsCheck == -1:

            crsr.execute('''INSERT INTO WS(NumInWs1,NumInWs2) VALUES({},{});'''.format(0,0))

            crsr.execute("SELECT MAX(rowid) FROM WS")
            ans = crsr.fetchall()
            wsid1 = singleData(ans[0])

            crsr.execute("UPDATE CORP SET WsID1 = {} WHERE CorpID LIKE \'{}\' ".format(wsid1,serverId))

            crsr.execute('''INSERT INTO WS(NumInWs1,NumInWs2) VALUES({},{});'''.format(0,0))

            crsr.execute("SELECT MAX(rowid) FROM WS")
            ans = crsr.fetchall()
            wsid2 = singleData(ans[0])

            crsr.execute("UPDATE CORP SET WsID2 = {} WHERE CorpID LIKE \'{}\' ".format(wsid2,serverId))

            await channel.send('You have started a WS\n-------------------------------------------------\nReact to this msg with 1️⃣ or 2️⃣ to be added to the WS1 or WS2 list(unreact to remove yourself)\n-------------------------------------------------')
            time.sleep(.5)
            msg = await channel.history(limit = 1).flatten()
            msg = msg[0]
            msg = msg.id
            '''print(msg)
            msg = channel.last_message_id
            print(msg)'''
            crsr.execute("UPDATE WS SET WsMSG = {} WHERE rowid LIKE \'{}\' ".format(msg,wsid1))
            crsr.execute("UPDATE WS SET WsMSG = {} WHERE rowid LIKE \'{}\' ".format(msg,wsid2))
        else:
            await channel.send('You still have an ongoing ws, please use $wsover and re-do this commmand')
    else:
        await channel.send('You are not registered with the bot, please do $playeradd and then start a ws')

    connection.commit()
    connection.close()

#---------------------------------------------------------------------------------------------------------------------------

@client.event

async def on_raw_reaction_add(payload):

    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()

    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    message_id = payload.message_id
    serverId = payload.guild_id
    user = payload.user_id
    name ='@' + str(discord.utils.find(lambda m: m.id == payload.user_id, guild.members))
    channel = client.get_channel(payload.channel_id)
    msg = 0
    ans = [0]

    crsr.execute("SELECT WsMSG FROM WS as w, CORP as c WHERE w.rowid = c.WsID1 and c.CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    for i in ans:
        msg = singleData(i)
    print(msg)
    print(message_id)
    if message_id == msg:
        if payload.emoji.name == '1️⃣':
            crsr.execute("SELECT WsID1 FROM CORP WHERE CorpID = {} ".format(serverId))
            ans = crsr.fetchall()
            for i in ans:
                currentWS = singleData(i)
            print(currentWS)

            userCheck = ""
            crsr.execute("SELECT WsID FROM MEMBER WHERE UserID = {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                userCheck = singleData(i)

            crsr.execute("SELECT Banned FROM MEMBER WHERE UserID= {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                banned = singleData(i)

            crsr.execute("SELECT w.NumInWs1 FROM WS as w, CORP as c WHERE w.rowid = c.WsID1 and c.CorpID = {} ".format(serverId))
            ans = crsr.fetchall()
            for i in ans:
                numIn = singleData(i)

            msg = await channel.fetch_message(message_id)
            member = guild.get_member(user)
            if userCheck == currentWS:
                await channel.send("{} is already entered into your corp's WS list, un-react to exit your corp's ws".format(name))
                connection.commit()
                connection.close()
            elif userCheck == "":
                await msg.remove_reaction(payload.emoji.name, member)
                await channel.send("You are not entered into the data base, please do $playeradd")
                connection.commit()
                connection.close()
            elif numIn > 15:
                await msg.remove_reaction(payload.emoji.name, member)
                await channel.send("Too many in WS1")
                connection.commit()
                connection.close()
            elif banned == 1:
                await msg.remove_reaction(payload.emoji.name, member)
                await channel.send("{} is banned from your corp's WS list".format(name))
                connection.commit()
                connection.close()

            else:
                crsr.execute("UPDATE MEMBER SET WsID = {} WHERE UserID = {}".format(currentWS, user ))

                crsr.execute("SELECT w.NumInWs1 FROM CORP as c, WS as w WHERE c.WsID1 = w.rowid AND c.CorpID = {} ".format(serverId))
                ans = crsr.fetchall()
                for i in ans:
                    num = singleData(i)
                num+=1

                crsr.execute("UPDATE WS SET NumInWs1 = {} WHERE rowid = {}".format(num, currentWS ))
                role = discord.utils.get(guild.roles, name="WS1")
                await member.add_roles(role)

                await channel.send("{} is entered into your corp's WS list".format(name))
                connection.commit()
                connection.close()
        elif payload.emoji.name == '2️⃣':
            crsr.execute("SELECT WsID2 FROM CORP WHERE CorpID = {} ".format(serverId))
            ans = crsr.fetchall()
            for i in ans:
                currentWS = singleData(i)
            print(currentWS)

            crsr.execute("SELECT WsID1 FROM CORP WHERE CorpID = {} ".format(serverId))
            ans = crsr.fetchall()
            for i in ans:
                otherList = singleData(i)

            userCheck = ""
            crsr.execute("SELECT WsID FROM MEMBER WHERE UserID = {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                userCheck = singleData(i)

            crsr.execute("SELECT Banned FROM MEMBER WHERE UserID= {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                banned = singleData(i)

            msg = await channel.fetch_message(message_id)
            member = guild.get_member(user)

            if userCheck == currentWS:
                await channel.send("{} is already entered into your corp's WS list, un-react to exit your corp's ws".format(name))
                connection.commit()
                connection.close()
            elif userCheck == "":
                await msg.remove_reaction(payload.emoji.name, member)
                await channel.send("You are not entered into the data base, please do $playeradd")
                connection.commit()
                connection.close()
            elif userCheck == otherList:
                await msg.remove_reaction(payload.emoji.name, member)
                await channel.send("{} is already in WS1 list".format(name))
                connection.commit()
                connection.close()
            elif banned == 1:
                await msg.remove_reaction(payload.emoji.name, member)
                await channel.send("{} is banned from your corp's WS list".format(name))
                connection.commit()
                connection.close()


            else:
                crsr.execute("UPDATE MEMBER SET WsID = {} WHERE UserID = {}".format(currentWS, user ))

                crsr.execute("SELECT w.NumInWs2 FROM CORP as c, WS as w WHERE c.WsID2 = w.rowid AND c.CorpID = {} ".format(serverId))
                ans = crsr.fetchall()
                for i in ans:
                    num = singleData(i)
                num+=1

                print(num)
                crsr.execute("UPDATE WS SET NumInWs2 = {} WHERE rowid = {}".format(num, currentWS ))

                role = discord.utils.get(guild.roles, name="WS2")
                await member.add_roles(role)

                await channel.send("{} is entered into your corp's WS list".format(name))

                connection.commit()
                connection.close()
        else:
            connection.commit()
            connection.close()
    else:
        connection.commit()
        connection.close()
#---------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_raw_reaction_remove(payload):
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()

    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    message_id = payload.message_id
    serverId = payload.guild_id
    user = payload.user_id
    name ='@' + str(discord.utils.find(lambda m: m.id == payload.user_id, guild.members))
    channel = client.get_channel(payload.channel_id)
    msg = 0
    ans = [0]
    banned = 0

    crsr.execute("SELECT WsMSG FROM WS as w, CORP as c WHERE w.rowid = c.WsID1 and c.CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    for i in ans:
        msg = singleData(i)

    if message_id == msg:
        if payload.emoji.name == '1️⃣':
            userCheck = ""
            crsr.execute("SELECT WsID FROM MEMBER WHERE UserID= {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                userCheck = singleData(i)

            crsr.execute("SELECT WsID1 FROM CORP WHERE CorpID = {} ".format(serverId))
            ans = crsr.fetchall()
            for i in ans:
                currentWS = singleData(i)
            print(currentWS)

            crsr.execute("SELECT Banned FROM MEMBER WHERE UserID= {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                banned = singleData(i)
                print(banned)

            if banned == 1:
                pass

            elif userCheck == "":
                pass

            elif userCheck == -1:
               await channel.send("{} is already removed from your corp's WS list, react to enter your corp's WS".format(name))

            else:
                crsr.execute("UPDATE MEMBER SET WsID = {} WHERE UserID = {}".format(-1, user ))

                crsr.execute("SELECT w.NumInWs1 FROM CORP as c, WS as w WHERE c.WsID1 = w.rowid AND c.CorpID = {} ".format(serverId))
                ans = crsr.fetchall()
                for i in ans:
                    num = singleData(i)
                num-=1

                crsr.execute("UPDATE WS SET NumInWs1 = {} WHERE rowid = {}".format(num, currentWS ))
                member = guild.get_member(user)
                role = discord.utils.get(guild.roles, name="WS1")
                await member.remove_roles(role)
                await channel.send("{} is removed from your corp's WS list".format(name))
        elif payload.emoji.name == '2️⃣':
            userCheck = ""
            crsr.execute("SELECT WsID FROM MEMBER WHERE UserID= {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                userCheck = singleData(i)

            crsr.execute("SELECT WsID2 FROM CORP WHERE CorpID = {} ".format(serverId))
            ans = crsr.fetchall()
            for i in ans:
                currentWS = singleData(i)
            print(currentWS)

            crsr.execute("SELECT Banned FROM MEMBER WHERE UserID= {} ".format(user))
            ans = crsr.fetchall()
            for i in ans:
                banned = singleData(i)
                print(banned)

            if banned == 1:
                pass

            elif userCheck == "":
                pass

            elif userCheck == -1:
               await channel.send("{} is already removed from your corp's WS list, react to enter your corp's WS".format(name))

            else:
                crsr.execute("UPDATE MEMBER SET WsID = {} WHERE UserID = {}".format(-1, user ))

                crsr.execute("SELECT w.NumInWs2 FROM CORP as c, WS as w WHERE c.WsID2 = w.rowid AND c.CorpID = {} ".format(serverId))
                ans = crsr.fetchall()
                for i in ans:
                    num = singleData(i)
                num-=1
                print(num)
                crsr.execute("UPDATE WS SET NumInWs2 = {} WHERE rowid = {}".format(num, currentWS ))
                member = guild.get_member(user)
                role = discord.utils.get(guild.roles, name="WS2")
                await member.remove_roles(role)
                await channel.send("{} is removed from your corp's WS list".format(name))
        connection.commit()
        connection.close()



#---------------------------------------------------------------------------------------------------------------------------
@client.command()
@has_permissions(manage_roles=True,ban_members=True)
async def wsover(ctx, WS):
    WS = int(WS)

    guild= ctx.guild
    '''
    role = discord.utils.get(guild.roles, name="WS1")
    await member.remove_roles(role)
    '''

    channel = ctx.channel
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id

    crsr.execute("SELECT WsID1 FROM CORP WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    wsCheck1 = singleData(ans[0])

    crsr.execute("SELECT WsID2 FROM CORP WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    wsCheck2 = singleData(ans[0])

    crsr.execute("SELECT UserID FROM MEMBER as m ,WS as w WHERE w.rowid = m.WsID and w.rowid = {}".format(wsCheck1))
    ans = crsr.fetchall()
    member = []
    for i in ans:
        member.append(singleData(i))

    member1 = []
    print(member)
    for i in member:
        member1.append(guild.get_member(i))


    crsr.execute("SELECT WsMSG FROM WS as w, CORP as c WHERE w.rowid = c.WsID1 and c.CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    message = singleData(ans[0])

    crsr.execute("SELECT UserID FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    wsCheck1 = singleData(ans[0])


    if wsCheck1 != -1 and WS == 1:
        crsr.execute("UPDATE CORP SET WsID1 = {} WHERE CorpID = {}".format(-1,serverId))
        crsr.execute("UPDATE MEMBER SET WsID = {} WHERE CorpID = {} AND WsID == {}".format(-1,serverId,wsCheck1))
        try:
            msg = await channel.fetch_message(message)
            await msg.delete()
        except NotFound:
            print("error")
        except discord.errors.NotFound:
            print("cannont find msg")
        finally:
            await channel.send("Your WS1 is terminated")
            for i in member1:
                await i.remove_roles("WS1")
            connection.commit()
            connection.close()

    elif wsCheck2 != -1 and WS == 2:
        crsr.execute("UPDATE CORP SET WsID2 = {} WHERE CorpID = {}".format(-1,serverId))
        crsr.execute("UPDATE MEMBER SET WsID = {} WHERE CorpID = {} AND WsID == {}".format(-1,serverId,wsCheck1))
        try:
            msg = await channel.fetch_message(message)
            await msg.delete()
        except NotFound:
            print("error")
        except discord.errors.NotFound:
            print("cannont find msg")
        finally:
            for i in member1:
                await i.remove_roles("WS1")
            await channel.send("Your WS2 is terminated")
            connection.commit()
            connection.close()
    elif WS == 0 or WS == None :
        crsr.execute("UPDATE CORP SET WsID1 = {} WHERE CorpID = {}".format(-1,serverId))
        crsr.execute("UPDATE CORP SET WsID2 = {} WHERE CorpID = {}".format(-1,serverId))
        crsr.execute("UPDATE MEMBER SET WsID = {} WHERE CorpID = {} AND (WsID = {} OR WsID = {})".format(-1,serverId,wsCheck1,wsCheck2))
        try:
            msg = await channel.fetch_message(message)
            await msg.delete()
        except NotFound:
            print("error")
        except discord.errors.NotFound:
            print("cannont find msg")
        finally:
            for i in member1:
                await i.remove_roles("WS1")
            await channel.send("Your WS is terminated")
            connection.commit()
            connection.close()
    else:
        print(wsCheck1)
        await channel.send("Your corp dosen't have an active ws on file, do $wsstart to start one")
        connection.commit()
        connection.close()


#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(manage_roles=True)
async def wslist1(ctx):
    channel = ctx.channel

    with open('ws.txt', 'w') as a_writer:
        pass
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id

    crsr.execute("SELECT UserName FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userIds= []
    for i in ans:
        userIds.append(singleData(i))
    print(userIds)
    crsr.execute("SELECT WsID1 FROM CORP WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    for i in ans:
        currentWS = singleData(i)
    print(currentWS)
    print("------")
    crsr.execute("SELECT WsID FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userInOut= []
    for i in ans:
        userInOut.append(singleData(i))
    print(userInOut)

    check = 0
    crsr.execute("SELECT count(UserName) FROM MEMBER WHERE CorpID = {} AND WsID != -1".format(serverId))
    ans = crsr.fetchall()
    for i in ans:
        check = singleData(i)

    if check == 0:
        await channel.send('There is no one signed up...')
    else:
        await channel.send('Here is the ws1 list as of right now...')

        inWs = 0

        for i, item in enumerate(userIds):
            if i == 0:
               with open('ws.txt', 'w') as a_writer:
                    a_writer.write("\n")
                    if userInOut[i] == currentWS  :
                        a_writer.write("{}{}".format(userIds[i], ':white_check_mark:' ))
                        inWs+=1
                        print('hit')
            else:
                with open('ws.txt', 'a') as a_writer:
                    if userInOut[i] == currentWS  :
                        a_writer.write("\n")
                        a_writer.write("{}{}".format(userIds[i], ':white_check_mark:' ))
                        inWs += 1

        with open('ws.txt', 'r') as reader:
            await channel.send(reader.read())

        crsr.execute("SELECT w.NumInWs1 FROM CORP as c, WS as w WHERE c.WsID1 = w.rowid AND c.CorpID = {} ".format(serverId))
        ans = crsr.fetchall()
        for i in ans:
            num = singleData(i)

        if num == 4:
            await channel.send('You are {} person away from a 5v5'.format(5-num))
        elif num < 5:
            await channel.send('You are {} people away from a 5v5'.format(5-num))
        elif 5 <= num <10:
            await channel.send('You are {} people away from a 10v10'.format(10-num))
        elif 10 <= num < 15:
            await channel.send('You are {} people away from a 15v15'.format(15-num))
        else:
            await channel.send('You have {} members signed up'.format(num))
    connection.commit()
    connection.close()

#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(manage_roles=True)
async def wslist2(ctx):
    channel = ctx.channel

    with open('ws.txt', 'w') as a_writer:
        pass
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id

    crsr.execute("SELECT UserName FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userIds= []
    for i in ans:
        userIds.append(singleData(i))
    print(userIds)
    crsr.execute("SELECT WsID2 FROM CORP WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    for i in ans:
        currentWS = singleData(i)
    print(currentWS)
    print("------")
    crsr.execute("SELECT WsID FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userInOut= []
    for i in ans:
        userInOut.append(singleData(i))
    print(userInOut)

    check = 0
    crsr.execute("SELECT count(UserName) FROM MEMBER WHERE CorpID = {} AND WsID != -1".format(serverId))
    ans = crsr.fetchall()
    for i in ans:
        check = singleData(i)

    if check == 0:
        await channel.send('There is no one signed up...')
    else:
        await channel.send('Here is the ws2 list as of right now...')

        inWs = 0

        for i, item in enumerate(userIds):
            if i == 0:
               with open('ws.txt', 'w') as a_writer:
                    a_writer.write("\n")
                    if userInOut[i] == currentWS  :
                        a_writer.write("{}{}".format(userIds[i], ':white_check_mark:' ))
                        inWs+=1
                        print('hit')
            else:
                with open('ws.txt', 'a') as a_writer:
                    if userInOut[i] == currentWS  :
                        a_writer.write("\n")
                        a_writer.write("{}{}".format(userIds[i], ':white_check_mark:' ))
                        inWs += 1

        with open('ws.txt', 'r') as reader:
            await channel.send(reader.read())

        crsr.execute("SELECT w.NumInWs2 FROM CORP as c, WS as w WHERE c.WsID2 = w.rowid AND c.CorpID = {} ".format(serverId))
        ans = crsr.fetchall()
        for i in ans:
            num = singleData(i)

        if num < 5:
            await channel.send('You are {} people away from a 5v5'.format(5-num))
        elif 5 <= num <10:
            await channel.send('You are {} people away from a 10v10'.format(10-num))
        elif 10 <= num < 15:
            await channel.send('You are {} people away from a 15v15'.format(15-num))
        else:
            await channel.send('You have {} members signed up'.format(num))
    connection.commit()
    connection.close()

#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(manage_roles=True,ban_members = True)
async def players(ctx):
    channel = ctx.channel
    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id

    crsr.execute("SELECT UserName FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userIds= []
    for i in ans:
    	userIds.append(singleData(i))

    crsr.execute("SELECT BsLoadout FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    bs = []
    for i in ans:
    	bs.append(singleData(i))

    crsr.execute("SELECT Support1 FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    sup1= []
    for i in ans:
    	sup1.append(singleData(i))

    crsr.execute("SELECT Support2 FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    sup2= []
    for i in ans:
    	sup2.append(singleData(i))

    await channel.send('Here is the corp members list as of right now...')
    await channel.send('name:          |bs:                          |suport1:                        |suport2           ')
    await channel.send('---------------------------------------------------------------------------------------')

    if len(userIds) == 0:
        await channel.send('No users registered')
    else:
        for index,items in enumerate(userIds):
            if index == 0:
                with open('ws.txt', 'w') as a_writer:
                        a_writer.write("\n```")
                        a_writer.write("\n{}".format(userIds[index]))
                        a_writer.write("\n{}".format(bs[index]))
                        a_writer.write("\n{}".format(sup1[index]))
                        a_writer.write("\n{}```".format(sup2[index]))
                        a_writer.write("--------------------------------------------------")
            else:
                with open('ws.txt', 'a') as a_writer:
                        a_writer.write("\n```")
                        a_writer.write("\n{}".format(userIds[index]))
                        a_writer.write("\n{}".format(bs[index]))
                        a_writer.write("\n{}".format(sup1[index]))
                        a_writer.write("\n{}```".format(sup2[index]))
                        a_writer.write("--------------------------------------------------")
        with open('ws.txt', 'r') as reader:
            await channel.send(reader.read())
    connection.commit()
    connection.close()

#----------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(administrator = True)
async def delete(ctx):
    channel = ctx.channel

    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id

    crsr.execute("SELECT UserID FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userIds= []
    for i in ans:
    	userIds.append(singleData(i))

    print(userIds)
    crsr.execute("SELECT UserName FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userName= []
    for i in ans:
    	userName.append(singleData(i))

    await channel.send("If the user is still in the discord server type y, if not type n")
    answer = await Enter.get_input_of_type(str,ctx)
    answer = answer.lower()

    if answer == 'y':
        await channel.send("What username do you wish to delete (ping the person to get correct name) : ")
        user_name = await Enter.get_input_of_type(str,ctx)
        print(user_name)
        user_name = user_name.replace("<@!","")
        user_name = user_name.replace("<@","")
        user_name = user_name.replace(">","")
        user_name = int(user_name)
        if user_name in userIds:

            crsr.execute("DELETE FROM MEMBER WHERE UserID = {}".format(user_name))
            connection.commit()
            await channel.send('User has been deleted')

        else:
            await channel.send("The bot failed to find a user, their id might have changed. try again but go down the ""n"" path")
    else:
        await channel.send("What username do you wish to delete (type username without the ""@"" symbol) : ")
        user_name = singleData(await Enter.get_input_of_type(str,ctx))
        print(user_name)
        user_name = "@" + user_name
        if user_name in userName:

                crsr.execute("DELETE FROM MEMBER WHERE UserName = \'{}\'".format(user_name))
                await channel.send('User has been deleted')

        else:
                await channel.send("The bot failed to find a user, their id might have changed or there is a bug...")
    connection.commit()
    connection.close()

#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, user_name):
    channel = ctx.channel

    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id
    user_name = user_name.replace("<@!","")
    user_name = user_name.replace("<@","")
    user_name = user_name.replace(">","")
    user_name = int(user_name)

    print(user_name)

    crsr.execute("SELECT UserID FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userIds= []
    for i in ans:
    	userIds.append(singleData(i))

    if user_name in userIds:
        crsr.execute("UPDATE MEMBER SET Banned = {} WHERE UserID = {}".format(1,user_name))
        await channel.send("User banned from entering a WS roster")
    else:
        await channel.send("You pinged the wrong person or they are not registered under your server")
    connection.commit()
    connection.close()

#---------------------------------------------------------------------------------------------------------------------------

@client.command()
@has_permissions(ban_members=True)
async def unban(ctx, user_name):
    channel = ctx.channel

    connection = sqlite3.connect("discordBot")
    crsr = connection.cursor()
    serverId = ctx.guild.id
    user_name = user_name.replace("<@!","")
    user_name = user_name.replace("<@","")
    user_name = user_name.replace(">","")
    user_name = int(user_name)

    print(user_name)

    crsr.execute("SELECT UserID FROM MEMBER WHERE CorpID = {}".format(serverId))
    ans = crsr.fetchall()
    userIds= []
    for i in ans:
    	userIds.append(singleData(i))

    if user_name in userIds:
        crsr.execute("UPDATE MEMBER SET Banned = {} WHERE UserID = {}".format(0,user_name))
        await channel.send("User un-banned from entering a WS roster")
    else:
        await channel.send("You pinged the wrong person or they are not registered under your server")
    connection.commit()
    connection.close()

#---------------------------------------------------------------------------------------------------------------------------
@client.command()
@has_permissions(ban_members=True)
async def wssaveplan(ctx):
    channel = ctx.channel
    await channel.send("awaitng WS plan, please send image in chat")
    msg = await client.wait_for('message')
    url = msg.attachments[0].url
    user = str(ctx.message.author.id)
    name ='@' + str(ctx.message.author)
    now = datetime.datetime.now()
    with open("battleplan.txt", "w") as f:
        f.write(url + "\n")
        f.write(name+ "\n")
        f.write(str(now.strftime("%Y-%m-%d %H:%M")))

#---------------------------------------------------------------------------------------------------------------------------
@client.command()
@has_permissions(ban_members=True)
async def wsplan(ctx):
    channel = ctx.channel

    with open("battleplan.txt", "r") as f:
        data = f.readlines()
    data[1] = data[1].strip("\n")
    await channel.send("{} added this plan at {}\n{}".format(data[1],data[2],data[0]))


#---------------------------------------------------------------------------------------------------------------------------
@client.command()
async def planetcap(ctx):
    channel = ctx.channel

    continueser = True
    planet_list = {}
    with open('upgradelist.txt', 'w') as a_writer:
        pass

    tutorial = ' '
    await channel.send("Would you like to go through the tutorial (y/n)")
    tutorial = await Enter.get_input_of_type(str,ctx)
    tutorial = tutorial.lower()

    if tutorial == 'y':
        await channel.send("Welcome to the credit cap calculator!")
        await channel.send("-----")
        time.sleep(.5)
        await channel.send("This program will take your planet information, ask you what credit cap you want to reach, and will tell you what you need to upgrade! ")
        await channel.send("-----")
        time.sleep(3.5)
        await channel.send("the program will prompt you to enter every planets level,type, and tier")
        await channel.send("-----")
        time.sleep(3.5)
        await channel.send("tiers are based on how many times it can be upgraded, this information is found in the planets info tab, the tiers go as folows...")
        time.sleep(3.75)
        await channel.send("tier 1 = 15 upgrades")
        time.sleep(.5)
        await channel.send("tier 2 = 20 upgrades")
        time.sleep(.5)
        await channel.send("tier 3 = 30 upgrades")
        time.sleep(.5)
        await channel.send("tier 4 = 40 upgrades")
        await channel.send("-----")
        time.sleep(2.25)
        await channel.send("when entering data, it should look like this...")
        time.sleep(2)
        await channel.send("lvl,type,tier..... so:")
        time.sleep(1)
        await channel.send("1,desert,3")
        await channel.send("-----")
        time.sleep(2.25)
        await channel.send("to exit the program at any time, type... Stop")
        await channel.send("wait for the bot to ask you a question before typing or the bot will malfunction becuase it thinks you are trying to answer again.")
        await channel.send("-----")
        time.sleep(2.25)
        await channel.send("time to begin!!!")
        await channel.send("-----")
    else:
        pass

    redo = 'n'
    continues = False
    while redo == 'n':
        while continues == False:
            await channel.send("how many planets do you have?")
            t = time.process_time()
            continuser = True
            while continuser == True:
                number = await Enter.get_input_of_type(int,ctx)
                if (time.process_time() - t) >=45 :
                    continuser = False
                    await channel.send("Timed out")
                    raise AbortWait
                else:
                    if number == 'bad':
                        continues = False
                        continuser = False
                        t = time.process_time()
                    else:
                        continues = True
                        continuser = False

        for i in range(number):
            good = False
            while good == False:
                continues3 = False
                while continues3 == False:
                    try:
                        await channel.send("what is your {} planet lvl, {} planets type, {} planets tier?".format(i+1,i+1,i+1))
                        info = await Enter.get_input_of_type(str,ctx)
                        info = info.lower()
                        levels,planet_type,teirlvl = info.split(',')
                        continues3 = True
                    except ValueError:
                        await channel.send("please enter valid data, refer to tutorial for format")
                        continues3 = False
                levels = levels.replace(" ","")
                planet_type = planet_type.replace(" ","")
                teirlvl = teirlvl.replace(" ","")
                print(levels,planet_type,teirlvl)
                try:
                    credit_cap = planet_cap(levels)
                    credits_per_hour = credit_per_hour(planet_type,levels,teirlvl)
                    cost = planet_cost(levels)
                    good = True
                except:
                    await channel.send("please enter valid data, refer to tutorial for format")
                    good = False


            doc_stats = ('planet#: {}, level: {}, Storage: {}, planet_type: {}, tier: {}, credits: {}, cost to upgrade: {}'.format((i+1),levels,credit_cap,planet_type,teirlvl,credits_per_hour,cost))
            with open('upgradelist.txt', 'a') as a_writer:
                a_writer.write("\n{}".format(doc_stats))
                print('done {}'.format(i+1))

            planet_list[i] = (Planet(levels,credit_cap,credits_per_hour,cost,planet_type,teirlvl))
        orig_planet_lvl = []
        for i in planet_list:
            orig_planet_lvl.append(planet_list[i].get_planet_lvl())

        cost_list = []
        increase_in_cap = []
        increase_in_income = []
        decider = []
        temp_planets = planet_list.copy()

        current_storage = 0


        for i in temp_planets:
            storage = int(temp_planets[i].get_planet_storage())
            current_storage += storage
        await channel.send("Your starting storage is: {}".format(current_storage))
        cont = 'n'
        while cont == 'n':
            await channel.send('is this correct? (y/n)')
            redo = await Enter.get_input_of_type(str,ctx)
            print(redo)
            redo = redo.lower()
            if redo == 'y':
                cont = 'y'
            elif redo == 'n':
                with open('upgradelist.txt', 'w') as a_writer:
                    pass
                cont = 'y'
            else:
                await channel.send('please enter either y or n')
                cont = 'n'

    continues2 = False
    while continues2 == False:
        await channel.send('what is your desired credit cap goal?')
        cap_goal = await Enter.get_input_of_type(int,ctx)
        if cap_goal == 'bad':
            continues2 = False
        else:
            continues2 = True
    with open('upgradelist.txt', 'a') as a_writer:
                a_writer.write("\n--------------------------------------------------")
                a_writer.write("\nYour current cap: {}".format(current_storage))
                a_writer.write("\n--------------------------------------------------")
                a_writer.write("\nYour desired cap: {}".format(cap_goal))
                a_writer.write("\n--------------------------------------------------")


    max_levels = []

    for i in planet_list:
        max_levels.append(max_levels_planet(temp_planets[i].get_planet_types(),temp_planets[i].get_planet_tier()))



    while cap_goal > current_storage:

        for i in temp_planets:

            planet_storage = temp_planets[i].get_planet_storage()
            # print('storage is: ', planet_storage)
            planet_lvl = temp_planets[i].get_planet_lvl()
            #print('level is: ', planet_lvl)
            credit_per_hours = temp_planets[i].get_planet_credit_per_hour()
            #print('credit_per_hours is: ', credit_per_hours)
            planet_type = temp_planets[i].get_planet_types()
            #print('planet type is: ', planet_type)
            planet_tier = temp_planets[i].get_planet_tier()
            #print('planet tier is: ', planet_tier)
            new_lvl = str((int(planet_lvl) + 1))
            #print('next level should be: ', new_lvl)
            planet_cost_to_upgrade = int(planet_cost(planet_lvl))




            if planet_lvl == max_levels[i]:
                #print('test max')
                cost_list.append(temp_planets[i].get_planet_cost())
                increase_in_cap.append(99999)
                increase_in_income.append(999999)
                decider.append(999999)


            elif planet_cost_to_upgrade > current_storage:
                #print('test over')
                #print('cost to upgrade is: ',planet_cost_to_upgrade)
                cost_list.append(temp_planets[i].get_planet_cost())
                increase_in_cap.append(99999)
                increase_in_income.append(999999)
                decider.append(999999)

            else:
                #print('test normal')
                #print('cost to upgrade is: ',planet_cost_to_upgrade)
                if planet_cost_to_upgrade == 0:
                    planet_cost_to_upgrade = 1
                cost_list.append(planet_cost_to_upgrade)


                #print('its next planet cap if upgraded: ', new_planet_cap)
                new_planet_cap = int(planet_cap(new_lvl))
                increase_cap = new_planet_cap - int(planet_storage)
                #print('increase in cap is: ', increase_cap)
                if increase_cap == 0:
                    increase_cap = 1
                increase_in_cap.append(increase_cap)

                new_credits_per_hour = int(credit_per_hour(planet_type,new_lvl,planet_tier))
                #print('new creadis per our if upgraded: ' , new_credits_per_hour)
                increase_in_incomees = new_credits_per_hour - int(credit_per_hours)
                #print('increase in income is: ', increase_in_incomees)
                #print('')
                if increase_in_incomees == 0:
                    increase_in_incomees = 1
                increase_in_income.append(increase_in_incomees)



                decider.append((cost_list[i]/increase_in_cap[i]/increase_in_income[i]))
            #print(decider)


        value = min(decider)
        first = 'y'
        for index,item in enumerate(decider):
            if item == value:
                if first == 'y':
                    if item == 999999:
                        continue
                        first = 'n'
                    else:
                        sending = ('planet',(index +1), '--->', (int(temp_planets[index].get_planet_lvl())+1))
                        #await channel.send(sending)
                        with open('upgradelist.txt', 'a') as a_writer:
                            a_writer.write("\n{}".format(sending))

                        new_planet_cost = planet_cost(str(int(temp_planets[index].get_planet_lvl())+1))
                        temp_planets[index].set_planet_cost(new_planet_cost)

                        new_planet_storage = planet_cap(str(int(temp_planets[index].get_planet_lvl())+1))
                        #print('new planet storage = ', new_planet_storage)
                        temp_planets[index].set_planet_storage(new_planet_storage)

                        new_planet_credits = credit_per_hour(temp_planets[index].get_planet_types(),str(int(temp_planets[index].get_planet_lvl())+1),temp_planets[index].get_planet_tier())
                        temp_planets[index].set_planet_credit_per_hour(new_planet_credits)

                        new_planet_lvl = str(int(temp_planets[index].get_planet_lvl())+1)
                        temp_planets[index].set_planet_lvl(new_planet_lvl)

                        current_storage += increase_in_cap[index]
                        #await channel.send('Your storage went up to: {}'.format(current_storage))


                        first = 'n'

        cost_list = []
        increase_in_cap = []
        increase_in_income = []
        decider = []

    await channel.send('Your final storage is: {}'.format(current_storage))
    with open('upgradelist.txt', 'a') as a_writer:
        a_writer.write("\n--------------------------------------------------")
        a_writer.write("\n'Your final storage is: {}".format(current_storage))
        a_writer.write("\n--------------------------------------------------")
    for index,item in enumerate(planet_list):
        if temp_planets[index].get_planet_lvl() != orig_planet_lvl[index]:
            #sent = '{} planet whent from lvl'.format(index+1),orig_planet_lvl[index], 'to lvl',temp_planets[index].get_planet_lvl()
            await channel.send('the {} planet was upgrade to lvl {}'.format((index+1),temp_planets[index].get_planet_lvl()))
            with open('upgradelist.txt', 'a') as a_writer:
                a_writer.write('\nThe {} planet was upgrade to lvl {}'.format((index+1),temp_planets[index].get_planet_lvl()))
    txtfile = 'upgradelist.txt'
    await channel.send('Here is a file of this calculation to keep!')
    await channel.send(file=discord.File('upgradelist.txt'))

@client.command()
@commands.has_any_role("Betauri Members","Director",)
async def help(ctx):
    await ctx.send('Here is a list of Betauri commands')
    await ctx.send('----------------------------------')
    await ctx.send('```$register   -registers your corp/server with the bot\n$playeradd   -add yourself to your corp and enter your builds for next ws\n$delete   -removes a player from the bot\n$wslist1 & $wslis2   -a list of who is ws and who isnt\n$players   -lists who is in ws and their builds\n$wsstart   -starts a new ws for your server\n$wsover (1 or 2)   - wipes the ws roster and stops the active ws on your server\n$ban   - bans a player from entering a WS roster\n$unban   - un-bans a player from entering a WS roster\nwssaveplan   -saves image for wsplans\nwsplan   -shows ws plan that is saved\n-----------------------------------------------------\n$greet   -a simple way to see if the bot is working\n$planetcap   -can calculate what planets you need to upgrade to meet a certain credit cap```')
    await ctx.send("-----------------------------------------------")
    await ctx.send("```Starting a WS...\nMake sure your corp is registered with $register and players are registerd with $playeradd\nThen do $wsstart to start a ws\nyour players should now be able to react to the msg to enter or exit ws\nWhen the WS is over, do $wsover (1 or 2) to stop the bots current ws for your server and repeat the proccess```")


client.run(TOKEN)
