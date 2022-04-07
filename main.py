import os
import nextcord
import random
import asyncio
from nextcord import Interaction
from nextcord import Intents
from nextcord.ext import commands

intents = Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='-', intents=intents, case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game('-help'))
    print('bot is ready')
  
@bot.listen('on_message')
async def ninde_achan(message):
  if message.author == bot.user:
    return

  if "alla ninde achan poda" in message.content:
    await message.reply(f"{message.author.mention} Athu ninde achan annu. Ninde achan mathramalla ninde achande achannum. Poi odu thendi")

     
  

for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} Can not be loaded")
            raise e



@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)} ms")


@bot.slash_command(name = "rickroll", description="Rickrolls you", guild_ids=[808704986485620736, 910811019608223754, 947151111037526096])
async def rickroll(interaction: Interaction):
    await interaction.response.send_message("https://tenor.com/view/rick-astly-rick-rolled-gif-22755440"
                   )


@bot.command()
async def poll(ctx, title, optionone=None, optiontwo=None):
    embed = nextcord.Embed(title=title)
    embed.add_field(name="Option",
                    value=":one:" + " " + optionone,
                    inline=True)
    embed.add_field(name="Option",
                    value=":two:" + " " + optiontwo,
                    inline=True)
    message = await ctx.send(embed=embed)
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")


@bot.slash_command(name = "dhillan", description= "gives dhillan dialogues", guild_ids= [ 808704986485620736,910811019608223754,947151111037526096])
async def dhillan(interaction: Interaction):
    dhillan = [
        "all hates me anyways",
        "think what u want",
        "tell what u want",
        "roast what u want",
        "frick u mate",
        "poi chavada",
        "REVIVE REVIVE REVIVE TUUUUUUUUUUUUUU",
        "ok",
        "the shiddy never sleeps tonight DADADADA DADADA DADADADADAADA",
        "go frick yourself mate",
        "la la lae",
        "we are homies.  we eat together, we play together, we sleep together",
        "gud for you",
        "i tried so far and got so far. BUT IN THE END IT DOSENT EVEN MAAAAAAAATTTAR",
        "bye motherfathers",
        "bish",
        "this makes my butt feel good",
        "GOOGLE SEND 100 GUNDAAS TO MAAM'S HOUSE",
        "tududududdududud",
    ]
    dhillan = random.choice(dhillan)
    await interaction.response.send_message(dhillan)


@bot.slash_command(name = "hecker", description= "Gives hecker dialogues" , guild_ids= [ 808704986485620736,910811019608223754,947151111037526096])
async def hecker(interaction: Interaction):
    damn = [
        "kulukulukuluku wassup guys", "djal fdlskjafkldjas;fd",
        "YO JOGINDER THARA BHAI JOGINDER",
        "Its jonathan its jonathan who gave the code",
        "Ende pattiku keree oru merry christmas ..... parayan marannu poi oru happy new year",
        "ACHAN AVIDE UNDOOOOO", "MINNAL MURALIIIIIIIIIIIIIIIIIIIIIIIIIII",
        "DES       PA CITOO I ATE MY LAST BURITTO",
        "pls dont remove me pls :(", "shut up man"
    ]
    damn = random.choice(damn)
    await interaction.response.send_message(damn)


@bot.slash_command(name = "emil", description= "Gives emil dialogues", guild_ids= [808704986485620736,910811019608223754,94715111103752609] )
async def emil(interaction:Interaction):
      emil = [
        "ninde achan pavam for having an idiot like you", "jk.....ROWLING",
        "ok man", "wishing the same to you and your family",
        "banjo depresso kazooie"
    ]
      emil = random.choice(emil)
      await interaction.response.send_message(emil)



@bot.slash_command(name = "toss", description = "give heads or tails",  guild_ids= [808704986485620736,910811019608223754,94715111103752609])
async def toss(interaction:Interaction):
     coin = ["heads", "tails"]
     coin = random.choice(coin)
     await interaction.response.send_message(coin)


@bot.command(name="8ball")
async def _8ball(ctx, *,Title = None):
    reply = [
        "HELL YEA. WHY ARE YOU EVEN ASKING MAN", "Most probably yes",
        "Very likely yea", "Maybe", "Tough question but probably no",
        "Most probably no", "OF COURSE NEVER.", "Frick off dont ask me that"
    ]
    reply = random.choice(reply)
    if Title is None:
      await ctx.send("Give a question you dummie")
    else:
      embed = nextcord.Embed(title = Title, description = reply)
      await ctx.send(embed=embed)
    
    
    


@bot.command()
async def timedpoll(ctx, title,time, optionone=None, optiontwo=None):
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    time_period = int(time[0]) * time_convert[time[-1]]
    embed = nextcord.Embed(title=title)
    embed.add_field(name="Option",
                    value=":one:" + " " + optionone,
                    inline=True)
    embed.add_field(name="Option",
                    value=":two:" + " " + optiontwo,
                    inline=True)
    message = await ctx.send(embed=embed)
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await asyncio.sleep(time_period)
    await message.delete()
    await ctx.send("The poll is done")










bot.run("OTI3Nzk5NTA0Mjg2MTIyMDI0.YdPenw.v6_Ch5iPpUTohay-eJQ412PJSn8")