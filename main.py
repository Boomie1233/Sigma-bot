import os
from dotenv import load_dotenv
import nextcord
from flask import Flask
from nextcord import Intents
from threading import Thread
from nextcord.ext import commands

load_dotenv()
intents = Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'Bot is running!'

def run_flask():
    port = int(os.environ.get('PORT', 8000))
    print("Web server started")
    app.run(host='0.0.0.0', port=port)

directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cogs")


bot = commands.Bot(command_prefix='-', intents=intents, case_insensitive=True)
bot.remove_command('help')



@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game('-help'))
    print('bot is ready')
  
     

for cog in os.listdir(directory):
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

if __name__ == "__main__":
    server_thread = Thread(target=run_flask)
    server_thread.start()
    bot.run(os.getenv('TOKEN'))