import keep_alive
import os
import time
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = 'Boi ')
spamflag = 1

@bot.event
async def on_ready():
    print('i am ready')

@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
         await ctx.send("You need to add all the arguments, Use the help command for finding all requirements. ")


@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound):
         await ctx.send("That command doesn't even exist, Use the help command for seeing all commands i can do. ")


@bot.command()
async def clear(ctx, amount):
   if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
     await ctx.channel.purge(limit =  int(amount) + 1)
   else:
     await ctx.send('You are not permitted to use this command')

@bot.command()
async def nuke_channel(ctx, amount = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
   if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
       await ctx.channel.purge(limit =  amount)
       await ctx.send('https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831')
       await ctx.send('This channel has been nuked')
   else:
        await ctx.send('You are not permitted to use this command')

@bot.command()
async def ghostping(ctx, user, amount = None):
    i = int(amount)
    if i < 11 and user !="@LoneWolF#7895" and user != "@LoneWolF" and user != "<@583909790460411904>":
       for i in range(0, i):
          await ctx.send(user)
       await ctx.send("ghostpinging done")
       time.sleep(2)
       await ctx.channel.purge(limit = i + 3)
    elif user == "@LoneWolF#7895" or user == "<@583909790460411904":
        await ctx.send("Can't ghostping this user") 
    elif i >= 11:
       await ctx.send("Sorry, 10 is the limit")

@bot.command()
async def spam(ctx, spam, amount = None):
     x = int(amount)
     if x < 11 and spam != "@LoneWolF#7895" and spam!="@LoneWolF" and spam != "<@583909790460411904" :
       for i in range(0, x):
        await ctx.send(spam)
     elif spam == "@LoneWolF#7895" or spam == "@LoneWolF" or spam == "<@583909790460411904":
        await ctx.send("Bhag Bhosdike")    
     if x > 11:
        await ctx.send("Sorry, the limit is upto 10")


@bot.command() 
async def codmap(ctx,map = None, mode = None):
    if map == "FiringRange" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Firing Range - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/FiringRangeDom.png')
         await ctx.send(embed = embed)

    if map == "Summit" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Summit - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/SummitDom.png')
         await ctx.send(embed = embed)

    if map == "Nuketown" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Nuketown - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/NuketownDom.png')
         await ctx.send(embed = embed)

    if map == "Crossfire" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crossfire - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/plugins/widgetkit/cache/CrossfireDom-4d12761816f9d9467e1e74f2d314de68.png')
         await ctx.send(embed = embed)

    if map == "Raid" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Raid - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/RaidDom.png')
         await ctx.send(embed = embed)

    if map == "Standoff" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Standoff - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/StandoffDom.png')
         await ctx.send(embed = embed)

    if map == "Crash" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crash - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/CrashDom.png')
         await ctx.send(embed = embed)

    if map == "Meltdown" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Meltdown - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/MeltdownDom.png')
         await ctx.send(embed = embed)

    if map == "Rust" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Rust - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/RustDom.png')
         await ctx.send(embed = embed)

    if map == "Scrapyard" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Scrapyard - Domination", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/ScrapyardDom.png')
         await ctx.send(embed = embed)

    if map == "Takeoff" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Takeoff - Domination ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/TakeoffDom.png')
         await ctx.send(embed = embed)

    if map == "HeckneyYard" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "HeckneyYard - Domination ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://i.ibb.co/5vyBRks/Heckney-Yard-Dom.jpg')
         await ctx.send(embed = embed)

    if map == "Highrise" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Highrise - Domination ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://i.ibb.co/26DyC39/20201129-100142.png')
         await ctx.send(embed = embed)

    if map == "Terminal" and mode == "domination":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Terminal - Domination ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://i.ibb.co/KyWw4j7/20201129-215006.png')
         await ctx.send(embed = embed)


#---------------------------------------------------------------------------------------------------------------------------------------


    if map == "FiringRange" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Firing Range - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/FiringRangeHP.png')
         await ctx.send(embed = embed)

    if map == "Summit" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Summit - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/SummiTHP.png')
         await ctx.send(embed = embed)

    if map == "Nuketown" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Nuketown - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/NukeTownHP.png')
         await ctx.send(embed = embed)

    if map == "Crossfire" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crossfire - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/plugins/widgetkit/cache/CrossfireHP-cb81677a6d6f6794e5fbc31ef430e4b0.png')
         await ctx.send(embed = embed)

    if map == "Raid" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Raid - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/RaidHP.png')
         await ctx.send(embed = embed)

    if map == "Standoff" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Standoff - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/StandoffHP.png')
         await ctx.send(embed = embed)

    if map == "Crash" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crash - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/CrashHP.png')
         await ctx.send(embed = embed)

    if map == "Rust" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Rust - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/RustHP.png')
         await ctx.send(embed = embed)

    if map == "Scrapyard" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Scrapyard - Hardpoint", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/ScrapyardHP.png')
         await ctx.send(embed = embed)

    if map == "Takeoff" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Takeoff - Hardpoint ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/TakeoffHP.png')
         await ctx.send(embed = embed)

    if map == "Terminal" and mode == "hardpoint":
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Terminal - Hardpoint ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://i.ibb.co/YdtPXVV/Terminal-HP.jpg')
         await ctx.send(embed = embed)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if map == "Cage" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Cage", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Cage.png')
         await ctx.send(embed = embed)

    if map == "Crash" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crash", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Crash.png')
         await ctx.send(embed = embed)

    if map == "Crossfire" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crash", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/plugins/widgetkit/cache/crossfire-fc1d16ce3fe1af6b5afed94673ad3afc.png')
         await ctx.send(embed = embed)

    if map == "FiringRange" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "FiringRange", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/FiringRange.png')
         await ctx.send(embed = embed)

    if map == "Hijacked" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Hijacked", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Hijacked.png')
         await ctx.send(embed = embed)

    if map == "Killhouse" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Killhouse", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/KillHouse.png')
         await ctx.send(embed = embed)

    if map == "Meltdown" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Meltdown", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Meltdown.png')
         await ctx.send(embed = embed)

    if map == "Nuketown" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Nuketown", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Nuketown.png')
         await ctx.send(embed = embed)

    if map == "Raid" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Raid", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Raid.png')
         await ctx.send(embed = embed)

    if map == "Rust" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Rust", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Rust.png')
         await ctx.send(embed = embed)

    if map == "Scrapyard" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Scrapyard", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Scrapyard.png')
         await ctx.send(embed = embed)

    if map == "Standoff" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Standoff", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Standoff.png')
         await ctx.send(embed = embed)

    if map == "Summit" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Summit", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Summit.png')
         await ctx.send(embed = embed)

    if map == "Takeoff" and mode == None :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Takeoff", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/Takeoff.png')
         await ctx.send(embed = embed)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if map == "Takeoff" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Takeoff - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/TakeoffSnD.png')
         await ctx.send(embed = embed)

    if map == "Summit" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Summit - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/SummitSnD.png')
         await ctx.send(embed = embed)

    if map == "Standoff" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Standoff - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/StandoffSnD.png')
         await ctx.send(embed = embed)

    if map == "Scrapyard" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Scrapyard - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/ScrapyardSnD.png')
         await ctx.send(embed = embed)

    if map == "Raid" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Raid - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/RaidSnD.png')
         await ctx.send(embed = embed)

    if map == "Meltdown" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Meltdown - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/MeltdownSnD.png')
         await ctx.send(embed = embed)

    if map == "FiringRange" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "FiringRange - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/FiringRangeSnD.png')
         await ctx.send(embed = embed)

    if map == "Crossfire" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crossfire - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/CrossfireSnD.png?v=2')
         await ctx.send(embed = embed)

    if map == "Crash" and mode == "SnD" :
         embed = discord.Embed(
              title = 'CODM MAP',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Crash - SnD ", value = "Hello Soldier,for your mission I have asked my intel to get a satellite scan of the map and it's objectives so here it is, Best of Luck. ")
         embed.set_image(url = 'https://hawksnest.gg/wp-content/uploads/CrashSnD.png')
         await ctx.send(embed = embed)

    if map == None and mode == None :
         embed = discord.Embed(
              title = 'CODM MAPS',
              colour = discord.Colour.blue()
         )
         embed.add_field(name = "Info", value = "This feature is used to display a map according to given details, Type Boi codmap <map name> <mode>")
         await ctx.send(embed = embed)

token = os.getenv("SECRET_KEY")
keep_alive.keep_alive()
bot.run(token)