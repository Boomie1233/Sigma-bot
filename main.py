import os
from dotenv import load_dotenv
import nextcord
from aiohttp import web
from nextcord import Intents
from nextcord.ext import commands
import asyncio

load_dotenv()
intents = Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cogs")


bot = commands.Bot(command_prefix='-', intents=intents, case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game('-help'))
    print('bot is ready')
  
async def handle_health(request):
    return web.Response(text="OK", status=200)

async def start():
    app = web.Application()
    app.router.add_get('/', handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print("Web server opened")
  
async def main():
    for cog in os.listdir(directory):
        if cog.endswith(".py"):
            try:
                bot.load_extension(cog)
                cog = f"cogs.{cog.replace('.py', '')}"
            except Exception as e:
                print(f"{cog} Can not be loaded")
                raise e
    await start()
    await bot.start(os.getenv("TOKEN"))


@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency * 1000)} ms")

if __name__ == "__main__":
    asyncio.run(main())