import os
from dotenv import load_dotenv
import nextcord
from nextcord import Intents
from nextcord.ext import commands

load_dotenv()
intents = Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True



bot = commands.Bot(command_prefix='-', intents=intents, case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game('-help'))
    print('bot is ready')
  

     
  

for cog in os.listdir("Sigma-bot\cogs"):
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

bot.run(os.getenv("TOKEN"))
