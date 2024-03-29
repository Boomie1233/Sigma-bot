import nextcord
from nextcord.ext import commands

class help(commands.Cog):
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
    embed.add_field(name = "timer", value = "Syntax: -timer <time> <topic>\n Use: Sets remainder for a task", inline = True)
    embed.add_field(name = "sigma", value = "Gives how sigma a person is  (just mention to find out)", inline = True)
    embed.add_field(name = "casual", value = "Gives how casual a person is (just mention to find out)", inline= True)
    embed.add_field(name = "stark", value = "Gives how stark a person is (just mention to find out)", inline= True)
    embed.add_field(name = "starp", value = "Gives how starp a person is (just mention to find out)", inline= True)
    

    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(help(bot))