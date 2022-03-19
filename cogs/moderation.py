import nextcord
from nextcord.ext import commands
import datetime
import humanfriendly
from nextcord.ext.commands.core import has_permissions


class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @has_permissions(kick_members = True)
  async def kick(self,ctx, member: nextcord.Member, *, reason=None):
    if  member.top_role <= ctx.author.top_role:
      embed = nextcord.Embed(title = f"Kicked{member}", description = f"{member} is being kicked in the butt by {ctx.author.mention}for {reason}")
      await member.kick(reason=reason)
      await ctx.send(embed=embed)
    else:
      await ctx.send("We dont support overthrowing people here. PREIOD")

  @kick.error()
  async def kick_error(self, ctx, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = nextcord.Embed(title = f"Command: Kick", description = " Syntax: kick <member> <reason>\n This command kicks a member ")
      await ctx.send(embed = embed)
      




  @commands.command()
  @has_permissions(ban_members = True)
  async def ban(self,ctx, member: nextcord.Member, *, reason=None):
      if member.top_role <= ctx.author.top_role:
         await member.ban(reason=reason)
         embed = nextcord.Embed(title = f"Banned{member}", description = f"{member} is banished from the cult by{ctx.author.mention}for {reason}")
         await ctx.send(embed=embed)
      else:
         await ctx.send("We dont support overthrowing people here. PERIOD")


  @commands.command()
  @has_permissions(manage_messages = True)
  async def clear(self,ctx, amount=10):
    await ctx.channel.purge(limit=amount)


  @commands.command()
  @has_permissions(ban_members = True)
  async def unban(self,ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
       user = ban_entry.user

       if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
          await ctx.guild.unban(user)
          embed = nextcord.Embed(title = f"Unbanned {user}", description = f"{user} is removed from the blacklist of the cult. Party time")
          await ctx.send(embed=embed)


  @commands.command()
  @has_permissions(ban_members = True)
  async def timeout(self,ctx, member:nextcord.Member, time, reason = None):
     if member.top_role <= ctx.author.top_role:


       time = humanfriendly.parse_timespan(time)
       await member.edit(timeout = nextcord.utils.utcnow()+datetime.timedelta(seconds = time))
       embed = nextcord.Embed(title = f"Timedout {member}", description =f"{member}s mouth is shut by {ctx.author.mention}. Good luck trying to speak")
       await ctx.send(embed=embed)

  @commands.command()
  @has_permissions(ban_members = True)
  async def untimeout(self,ctx, member:nextcord.Member):
       if member.top_role <= ctx.author.top_role:
          await member.edit(timeout = None)
          embed = nextcord.Embed(title = f"Removed timeout from {member}", description = f"{member}s mouth is not shut anymore. Tell us what you want tot tell mate")
          await ctx.send(embed=embed)

  @commands.command()
  @has_permissions(manage_roles = True)
  async def addrole(self,ctx, member:nextcord.Member, role:nextcord.Role):
      await member.add_roles(role)
      await ctx.send(f"Added {role} to {member}")

  @commands.command()
  @has_permissions(manage_roles = True)
  async def removerole(self,ctx, member:nextcord.Member, role:nextcord.Role):
      await member.remove_roles(role)
      await ctx.send(f"Removed {role} from {member}")

  @commands.command()
  @has_permissions(manage_channels = True)
  async def lock(self,ctx, channel: nextcord.TextChannel = None):
     overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
     overwrite.send_messages = False
     await ctx.channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)
     await ctx.send("This channel is locked now shoo")


  @commands.command()
  @has_permissions(manage_channels = True)
  async def unlock(self,ctx, channel:nextcord.TextChannel = None):
       overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
       overwrite.send_messages = True
       await ctx.channel.set_permissions(ctx.guild.default_role, overwrite = overwrite)
       await ctx.send("This channel is unlocked. Now tell what u want")



def setup(bot):
  bot.add_cog(Moderation(bot))
  