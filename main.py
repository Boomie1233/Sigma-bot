import os
import nextcord
import random
import asyncio
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


@bot.command()
async def rickroll(ctx):
    await ctx.send("https://tenor.com/view/rick-astly-rick-rolled-gif-22755440"
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


@bot.command()
async def dhillan(ctx):
    dialogues = [
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
    dialogues = random.choice(dialogues)
    await ctx.send(dialogues)


@bot.command()
async def hecker(ctx):
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
    await ctx.send(damn)


@bot.command()
async def emil(ctx):
    emil = [
        "ninde achan pavam for having an idiot like you", "jk.....ROWLING",
        "ok man", "wishing the same to you and your family",
        "banjo depresso kazooie"
    ]
    emil = random.choice(emil)
    await ctx.send(emil)


@bot.command()
async def toss(ctx):
    coin = ["heads", "tails"]
    coin = random.choice(coin)
    await ctx.send(f"{ctx.author.mention} {coin}")


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


@bot.command()
async def amna(ctx):
  replies = ["404 Not found error. Please try again", 
            "Sigma bot jumped off a cliff  after seeing how ugly amna looked like", "Amna is soo casual that putin will spare ukraine and send troops to her house instead", "Sigma bot systems got overloaded with cringe", "Amna's stupidity is more fatter than a Sumo Wrestler's weight", "Amna sucks like the dog i see enjoying in the dranaige"]
  replies = random.choice(replies)
  await ctx.send(replies)





bot.run("OTI3Nzk5NTA0Mjg2MTIyMDI0.YdPenw.v6_Ch5iPpUTohay-eJQ412PJSn8")