from random import randint
import nextcord
import asyncio
from nextcord.ext import commands
from nextcord.member import Member

class utility(commands.Cog):
    def __init__(self, bot):
        self. bot = bot


    @commands.command()
    async def timer(self,ctx, time,*, topic = None):
     time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
     if len(time) == 2:
         time_period = int(time[0]) * time_convert[time[-1]]
     elif len(time) == 3:
         time_count = time[0] + time[1]
         time_period = int(time_count) * time_convert[time[-1]]
     elif len(time) == 4:
          time_count = time[0] + time[1] + time[2]
          time_period = int(time_count) * time_convert[time[-1]]
     else:
         await ctx.send("Use a bigger unit please")

         
     embed = nextcord.Embed(title = "Timer set", description= f"Time set for {time} due to {topic}")
     await ctx.send(embed=embed)
     await asyncio.sleep(time_period)
     await ctx.send(f"{ctx.author.mention} the timer for {topic} has run out")
     await ctx.author.send(f"Your timer for {topic} has run out")

    @commands.command()
    async def timedpoll(self,ctx, title,time, optionone=None, optiontwo=None):
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

    @commands.command()
    async def _8ball(self, ctx,*, Title = None):
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
    @commands.command()
    async def poll(self,ctx, title, optionone=None, optiontwo=None):
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

    @commands.command()
    async def sigma(self, ctx,*, member = None):
        percent = randint(0, 100)
        if member is None:
            embed = nextcord.Embed(title = "Sigma rate", description= f"{ctx.author.mention} is {percent}% sigma")
        elif member is nextcord.Member:
            embed = nextcord.Embed(title = "Sigma rate" , description= f"{member.mention} is {percent}% sigma")
        else:
            embed = nextcord.Embed(title = "Sigma rate" , description= f"{member} is {percent}% sigma")
        await ctx.send(embed=embed)
    @commands.command()
    async def casual(self, ctx,*, member = None):
        percent = randint(0, 100)
        if member is None:
            embed = nextcord.Embed(title = "Casual rate", description= f"{ctx.author.mention} is {percent}% casual")
        elif member is nextcord.Member:
            embed = nextcord.Embed(title = "Casual rate" , description= f"{member.mention} is {percent}% casual")
        else:
            embed = nextcord.Embed(title = "Casual rate" , description= f"{member} is {percent}% casual")
        await ctx.send(embed=embed)

    @commands.command()
    async def stark(self, ctx,*, member = None):
        percent = randint(0, 100)
        if member is None:
            embed = nextcord.Embed(title = "Stupid Thendi Alavaladi Rascal (STARK) rate", description= f"{ctx.author.mention} is {percent}% stark")
        elif member is nextcord.Member:
            embed = nextcord.Embed(title = "Stupid Thendi Alavaladi Rascal (STARK) rate" , description= f"{member.mention} is {percent}% stark")
        else:
            embed = nextcord.Embed(title = "Stupid Thendi Alavaladi Rascal (STARK) rate" , description= f"{member} is {percent}% stark")
        await ctx.send(embed=embed)

    @commands.command()
    async def starp(self, ctx,*, member = None):
        percent = randint(0, 100)
        if member is None:
            embed = nextcord.Embed(title = "Stupid Thendi Alavaladi Patti (STARP) rate", description= f"{ctx.author.mention} is {percent}% starp")
        elif member is nextcord.Member:
            embed = nextcord.Embed(title = "Stupid Thendi Alavaladi Rascal (STARP) rate" , description= f"{member.mention} is {percent}% starp")
        else:
            embed = nextcord.Embed(title = "Stupid Thendi Alavaladi Rascal (STARP) rate" , description= f"{member} is {percent}% starp")
        await ctx.send(embed=embed)
    








def setup(bot):
    bot.add_cog(utility(bot))