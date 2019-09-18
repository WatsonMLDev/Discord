from planetlists import planet_cap,planet_lvl,transfer,temp,credit_per_hour,planet_cost,max_levels_planet
import time
import discord
from discord.ext import commands
import xlwt
import xlrd
from xlutils.copy import copy
from os.path import join

style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on')

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




TOKEN = 'Insert BOT Token'

client = commands.Bot(command_prefix='$')

class AbortWait(Exception):
    pass

@client.event  # event decorator/wrapper
async def on_ready():

    global betauri
    await client.change_presence(activity = discord.Game(name = 'Type ''$commands'' for a list of commands!'))
    print(f"We have logged in as {client.user}")

@client.command()
async def greet(ctx):

    await ctx.send('Hello!!!')

@client.command()
@commands.has_any_role("Discord Admins","First Officer")
async def betauri_logout(ctx):

    await client.close()

@client.command()
@commands.has_any_role("Betauri Members","Director","Member","HA-WSC")
async def wsadd(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    user = str(ctx.message.author.id)
    name = str(ctx.message.author)


    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    user_id_match = []
    user_name_match = []
    for i in range(iterations):
        user_id_match.append(str(ws_sheet.cell(i+1,0).value))
    for i in range(iterations):
        user_name_match.append(str(ws_sheet.cell(i+1,1).value))
    wbo.release_resources()

    if (user in user_id_match):
        await channel.send('Your info is all ready added')
        await channel.send('Would you like to edit your data (y/n):')
        await channel.send("to exit the program at any time, type... stop")
        edit = await get_input_of_type(str)
        edit.lower()
        if edit == 'y':
            await channel.send('type bs mods, example...')
            await channel.send('bs: battery10,delta4,tw1,barrier1')
            bs = await get_input_of_type(str)

            await channel.send('type first support ship mods, example...')
            await channel.send('miner: tw1,genesis1')
            sup1 = await get_input_of_type(str)

            await channel.send('type second support ship mods, example...')
            await channel.send('trans: tw1,dispatch1')
            sup2 = await get_input_of_type(str)

            in_out = 0

            wbo = xlrd.open_workbook('ws.xls')
            ws_sheet = wbo.sheet_by_name('ws')
            iterations  = int(ws_sheet.cell(0,6).value)

            row_id = 0
            for index, item in enumerate(user_id_match):
                if item == user:
                    row_id = index

            wb = copy(wbo)
            wbo.release_resources()
            wsadd = wb.get_sheet('ws')

            wsadd.write(row_id+1, 0, user, style0)
            wsadd.write(row_id+1, 1, name, style0)
            wsadd.write(row_id+1, 2, bs, style0)
            wsadd.write(row_id+1, 3, sup1, style0)
            wsadd.write(row_id+1, 4, sup2, style0)
            wsadd.write(row_id+1, 5, in_out, style0)


            #wsadd.write(0, 6,(iterations+1),style0)
            wb.save('ws.xls')
            await channel.send('Your entry has been recorded!')
        else:
            pass
    elif (name in user-name_match):
        await channel.send('Your info is all ready added')
        await channel.send('Would you like to edit your data (y/n):')
        await channel.send("to exit the program at any time, type... stop")
        edit = await get_input_of_type(str)
        edit.lower()
        if edit == 'y':
            await channel.send('type bs mods, example...')
            await channel.send('bs: battery10,delta4,tw1,barrier1')
            bs = await get_input_of_type(str)

            await channel.send('type first support ship mods, example...')
            await channel.send('miner: tw1,genesis1')
            sup1 = await get_input_of_type(str)

            await channel.send('type second support ship mods, example...')
            await channel.send('trans: tw1,dispatch1')
            sup2 = await get_input_of_type(str)

            in_out = 0

            wbo = xlrd.open_workbook('ws.xls')
            ws_sheet = wbo.sheet_by_name('ws')
            iterations  = int(ws_sheet.cell(0,6).value)

            row_id = 0
            for index, item in enumerate(user_id_match):
                if item == user:
                    row_id = index

            wb = copy(wbo)
            wbo.release_resources()
            wsadd = wb.get_sheet('ws')

            wsadd.write(row_id+1, 0, user, style0)
            wsadd.write(row_id+1, 1, name, style0)
            wsadd.write(row_id+1, 2, bs, style0)
            wsadd.write(row_id+1, 3, sup1, style0)
            wsadd.write(row_id+1, 4, sup2, style0)
            wsadd.write(row_id+1, 5, in_out, style0)


            #wsadd.write(0, 6,(iterations+1),style0)
            wb.save('ws.xls')
            await channel.send('Your entry has been recorded!')
        
    else:
        await channel.send("to exit the program at any time, type... stop")
        await channel.send('type bs mods, example...')
        await channel.send('bs: battery10,delta4,tw1,barrier1')
        bs = await get_input_of_type(str)

        await channel.send('type first support ship mods, example...')
        await channel.send('miner: tw1,genesis1')
        sup1 = await get_input_of_type(str)

        await channel.send('type second support ship mods, example...')
        await channel.send('trans: tw1,dispatch1')
        sup2 = await get_input_of_type(str)

        in_out = 0

        wbo = xlrd.open_workbook('ws.xls')
        ws_sheet = wbo.sheet_by_name('ws')
        iterations  = int(ws_sheet.cell(0,6).value)



        wb = copy(wbo)
        wbo.release_resources()
        wsadd = wb.get_sheet('ws')

        wsadd.write(iterations+1, 0, user, style0)
        wsadd.write(iterations+1, 1, name, style0)
        wsadd.write(iterations+1, 2, bs, style0)
        wsadd.write(iterations+1, 3, sup1, style0)
        wsadd.write(iterations+1, 4, sup2, style0)
        wsadd.write(iterations+1, 5, in_out, style0)

        #temp = name+': |'+bs+'  | '+sup1+'  | '+sup2
        #with open('ws.txt', 'a') as a_writer:
            #a_writer.write("\n```")
            #a_writer.write("\n{}".format(name))
            #a_writer.write("\n{}".format(bs))
            #a_writer.write("\n{}".format(sup1))
            #a_writer.write("\n{}```".format(sup2))
            #a_writer.write("--------------------------------------------------")
        wsadd.write(0, 6,(iterations+1),style0)
        wb.save('ws.xls')
        await channel.send('Your entry has been recorded!')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
@commands.has_any_role("Betauri Members","Director","HA-WSC")
async def wstech(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    with open('ws.txt', 'w') as a_writer:
        pass

    await channel.send('Here is the ws list as of right now...')
    await channel.send('name:          |bs:                          |suport1:                        |suport2           ')
    await channel.send('---------------------------------------------------------------------------------------')

    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    ws_in_out = []
    ws_in = []
    for i in range(iterations):
        ws_in_out.append(int(ws_sheet.cell(i+1,5).value))
    print(ws_in_out)
    for index, value in enumerate(ws_in_out):
        if value == 1:
            ws_in.append(index+1)
    print(ws_in)
    if len(ws_in) == 0:
        await channel.send('No users opted in for ws')
    else:
        for index,items in enumerate(ws_in):
            if index == 0:
                with open('ws.txt', 'w') as a_writer:
                        a_writer.write("\n```")
                        a_writer.write("\n{}".format(str(ws_sheet.cell(ws_in[index],1).value)))
                        a_writer.write("\n{}".format(str(ws_sheet.cell(ws_in[index],2).value)))
                        a_writer.write("\n{}".format(str(ws_sheet.cell(ws_in[index],3).value)))
                        a_writer.write("\n{}```".format(str(ws_sheet.cell(ws_in[index],4).value)))
                        a_writer.write("--------------------------------------------------")
            else:
                with open('ws.txt', 'a') as a_writer:
                        a_writer.write("\n```")
                        a_writer.write("\n{}".format(str(ws_sheet.cell(ws_in[index],1).value)))
                        a_writer.write("\n{}".format(str(ws_sheet.cell(ws_in[index],2).value)))
                        a_writer.write("\n{}".format(str(ws_sheet.cell(ws_in[index],3).value)))
                        a_writer.write("\n{}```".format(str(ws_sheet.cell(ws_in[index],4).value)))
                        a_writer.write("--------------------------------------------------")
        with open('ws.txt', 'r') as reader:
            await channel.send(reader.read())
    wbo.release_resources()


@client.command()
@commands.has_any_role("Betauri Members","Director","Member","HA-WSC")
async def wslist(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    with open('ws.txt', 'w') as a_writer:
        pass

    await channel.send('Here is the ws list as of right now...')


    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    ws_in_out = []
    ammount = []

    for i in range(iterations):
        ws_in_out.append(int(ws_sheet.cell(i+1,5).value))
    print(ws_in_out)

    for index, value in enumerate(ws_in_out):
            ammount.append(index+1)
    print(ammount)
    for index,items in enumerate(ws_in_out):
        if index == 0:
            with open('ws.txt', 'w') as a_writer:
                    a_writer.write("\n")
                    if items == 1:
                        a_writer.write("{}{}".format(str(ws_sheet.cell(ammount[index],1).value),':white_check_mark:' ))
                    elif items == 2:
                        pass
                    else:
                        a_writer.write("{}{}".format(str(ws_sheet.cell(ammount[index],1).value),':x:' ))

        else:
            with open('ws.txt', 'a') as a_writer:
                    a_writer.write("\n")
                    if items == 1:
                        a_writer.write("{}{}".format(str(ws_sheet.cell(ammount[index],1).value),':white_check_mark:' ))
                    elif items == 2:
                        pass
                    else:
                        a_writer.write("{}{}".format(str(ws_sheet.cell(ammount[index],1).value),':x:' ))

    with open('ws.txt', 'r') as reader:
        await channel.send(reader.read())
    wbo.release_resources()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
@commands.has_any_role("Betauri Members","Director","Member","HA-WSC")
async def wsin(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    user = str(ctx.message.author.id)
    name = str(ctx.message.author)


    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    user_name_match = []
    for i in range(iterations):
        user_name_match.append(str(ws_sheet.cell(i+1,1).value))

    wb = copy(wbo)
    wbo.release_resources()
    wsadd = wb.get_sheet('ws')

    for index, value in enumerate(user_name_match):
        if value == name:
            wsadd.write(index+1, 5, 1)
            wb.save('ws.xls')
            await channel.send('Added to the ws roster!')
        else:
            pass

@client.command()
@commands.has_any_role("Betauri Members","Director","Member","HA-WSC")
async def wsout(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    user = str(ctx.message.author.id)
    name = str(ctx.message.author)


    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    user_name_match = []
    for i in range(iterations):
        user_name_match.append(str(ws_sheet.cell(i+1,1).value))

    wb = copy(wbo)
    wbo.release_resources()
    wsadd = wb.get_sheet('ws')

    counter = 0
    for index, value in enumerate(user_name_match):
        if value == name:
            wsadd.write(index+1, 5, 0)
            wb.save('ws.xls')
            await channel.send('Taken off the ws roster!')
        else:
            counter += 1



@client.command()
@commands.has_any_role("Betauri Members","Director","HA-WSC")
async def wswipe(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel


    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    ws_in_out = []
    wb = copy(wbo)
    wbo.release_resources()
    wsadd = wb.get_sheet('ws')
    for i in range(iterations):
        ws_in_out.append(int(ws_sheet.cell(i+1,5).value))

    for index, value in enumerate(ws_in_out):
        wsadd.write(index+1, 5, 0)
    wb.save('ws.xls')
    await channel.send('All current ws participants set to opt-out')

@client.command()
async def wsdelete(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    wbo = xlrd.open_workbook('ws.xls')
    ws_sheet = wbo.sheet_by_name('ws')
    iterations  = int(ws_sheet.cell(0,6).value)
    user_id_match = []
    user_name_match = []
    for i in range(iterations):
        user_id_match.append(str(ws_sheet.cell(i+1,0).value))
    for i in range(iterations):
        user_name_match.append(str(ws_sheet.cell(i+1,1).value))
    wbo.release_resources()

    await channel.send("What username do you wish to delete (type exact username without @ symbol) : ")
    user_name = await get_input_of_type(str)

    in_out = 0
    if user_name in user_name_match:
            wbo = xlrd.open_workbook('ws.xls')
            ws_sheet = wbo.sheet_by_name('ws')
            iterations  = int(ws_sheet.cell(0,6).value)

            row_id = 0
            for index, item in enumerate(user_id_match):
                if item == user_name:
                    row_id = index

            wb = copy(wbo)
            wbo.release_resources()
            wsadd = wb.get_sheet('ws')

            wsadd.write(row_id+1, 0, 'x', style0)
            wsadd.write(row_id+1, 1, 'x', style0)
            wsadd.write(row_id+1, 2, 'x', style0)
            wsadd.write(row_id+1, 3, 'x', style0)
            wsadd.write(row_id+1, 4, 'x', style0)
            wsadd.write(row_id+1, 5, 2, style0)


            #wsadd.write(0, 6,(iterations+1),style0)
            wb.save('ws.xls')
            await channel.send('User has been deleted')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command()
async def planetcap(ctx):

    async def get_input_of_type(func):
        global sentdex_guild
        while True:
            try:
                msg = await client.wait_for('message', check=check)
                return func(msg.content)
            except ValueError:
                return 'bad'
                continue
    def check(m):
        if m.content == 'stop':
            raise AbortWait
        return m.content == m.content and m.channel == channel and m.author == ctx.author
    channel = ctx.channel

    continueser = True
    planet_list = {}
    with open('upgradelist.txt', 'w') as a_writer:
        pass

    tutorial = ' '
    await channel.send("Would you like to go through the tutorial (y/n)")
    tutorial = await get_input_of_type(str)
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
        await channel.send("to exit the program at any time, type... stop")
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
                number = await get_input_of_type(int)
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
                        info = await get_input_of_type(str)
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
            redo = await get_input_of_type(str)
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
        cap_goal = await get_input_of_type(int)
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
async def adminlist(ctx):
    await ctx.send('Here is a list of Betauri commands')
    await ctx.send('----------------------------------')
    await ctx.send('```$greet   -a simple way to see if the bot is working\n$wsadd   -add yourself to the ws roster and builds for next ws\n$wsin   -to opt-in for WS\n$wsout   - to opt-out of WS\n$wslist   -a list of who is ws and who isnt\n$wstech   -lists who is in ws and their builds\n$wswipe   - wipes the ws roster\n$planetcap   -can calculate what planets you need to upgrade to meet a certain credit cap```')
@client.command()
@commands.has_any_role("Betauri Members","Director","Member",)
async def memberlist(ctx):
    await ctx.send('Here is a list of Betauri commands')
    await ctx.send('----------------------------------')
    await ctx.send('```$greet   -a simple way to see if the bot is working\n$wsadd   -add yourself to the ws roster and builds for next ws\n$wsin   -to opt-in for WS\n$wsout   - to opt-out of WS\n$wslist   -a list of who is ws and who isnt\n$planetcap   -can calculate what planets you need to upgrade to meet a certain credit cap```')

@client.command()
async def commands(ctx):
    await ctx.send('Here is a list of Betauri commands')
    await ctx.send('----------------------------------')
    await ctx.send('```$greet   -a simple way to see if the bot is working\n$planetcap   -can calculate what planets you need to upgrade to meet a certain credit cap\n$memberlist   -member only commands\n$adminlist   -Admin only commands\n$wsdelete   -deletes a user form the info sheet```')

client.run(TOKEN)
