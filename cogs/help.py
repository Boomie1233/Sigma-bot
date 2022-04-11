import nextcord
from nextcord.ext import commands

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx):
    embed = nextcord.Embed(title="Commands")
    embed.add_field(name="ping",
                    value="Returns the latency in ms",
                    inline=True)
    embed.add_field(
        name="kick",
        value="Syntax: kick <member> <reason>, Kicks a member from the server",
        inline=True)
    embed.add_field(
        name="ban",
        value="Syntax: ban <member> <reason>, Bans a member from the server",
        inline=True)
    embed.add_field(
        name="warn",
        value="Syntax: warn <member> <reason>, Warns a member from the server",
        inline=True)
    embed.add_field(name="timeout",
                    value="Syntax: timeout <member> <time> <reason>, puts a timeout on a member ",
                    inline=True)
    embed.add_field(name="untimeout",
                    value="Syntax: unmute <member> , Removes a timeout from a member ",
                    inline=True)
    embed.add_field(
        name="unban",
        value="Syntax: unban <member> <tag>, unbans a member from the server",
        inline=True)
    embed.add_field(
        name="clear",
        value=
        "Syntax: clear <amount of messages> , clears a number of messages",
        inline=True)
    embed.add_field(
        name="addrole",
        value=
        "Syntax: addrole <member> <role name, id or mention>, Adds a role to a member",
        inline=True)
    embed.add_field(
        name="removerole",
        value=
        "Syntax: removerole <member> <role name, id or mention>, Removes a role to a member",
        inline=True)
    embed.add_field(name="lock",
                    value="Syntax: lock <channel>, Locks a channel",
                    inline=True)
    embed.add_field(name="unlock",
                    value="Syntax: unlock <channel>, Unlcoks a channel",
                    inline=True)
    embed.add_field(name="rickroll", value="rickrolls someone", inline=True)
    embed.add_field(name="hecker",
                    value="gives secret quotes told by a zoom raider",
                    inline=True)
    embed.add_field(name = "toss", value = "tosses a coin", inline = True)
    embed.add_field(name = "8ball", value = "Gives the bot's opinion/prediction on a question", inline = True)
    embed.add_field(name = "timer", value = "Sets a remainder for a task you want to do without using a seperate app", inline = True)

    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(Help(bot))