import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import datetime
import humanfriendly
from nextcord.ext.commands.core import has_permissions

intents = nextcord.Intents.default()
intents.members = True


class moderation(commands.Cog):
    """
    Standard Moderation Suite.
    Designed for professional server management and administrative oversight.
    """
    
    guild_ids = [808704986485620736, 985909972971950110, 1010526444646060062, 1012306961364168774]

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="kick", description="Removes a member from the server", guild_ids=guild_ids)
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, member: nextcord.Member, reason: str = "No reason provided"):
        if member.top_role >= interaction.user.top_role:
            return await interaction.response.send_message("Administrative Error: Target has a higher or equal role.", ephemeral=True)
        
        await member.kick(reason=reason)
        embed = nextcord.Embed(
            title="Action: Kick", 
            description=f"**User:** {member}\n**Moderator:** {interaction.user.mention}\n**Reason:** {reason}", 
            color=nextcord.Color.orange()
        )
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="ban", description="Permanently restricts a member", guild_ids=guild_ids)
    @commands.has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction, member: nextcord.Member, reason: str = "No reason provided"):
        if member.top_role >= interaction.user.top_role:
            return await interaction.response.send_message("Administrative Error: Target has a higher or equal role.", ephemeral=True)

        await member.ban(reason=reason)
        embed = nextcord.Embed(
            title="Action: Ban", 
            description=f"**User:** {member}\n**Moderator:** {interaction.user.mention}\n**Reason:** {reason}", 
            color=nextcord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="clear", description="Bulk deletes messages", guild_ids=guild_ids)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, interaction: Interaction, amount: int = SlashOption(description="Messages to delete", min_value=1, max_value=100)):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Successfully purged {amount} messages.", ephemeral=True)

    @nextcord.slash_command(name="timeout", description="Temporarily restricts member communication", guild_ids=guild_ids)
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, interaction: Interaction, member: nextcord.Member, duration: str, reason: str = "No reason provided"):
        if member.top_role >= interaction.user.top_role:
            return await interaction.response.send_message("Hierarchy Error: Cannot moderate users with equal/higher status.", ephemeral=True)

        try:
            seconds = humanfriendly.parse_timespan(duration)
            await member.edit(timeout=nextcord.utils.utcnow() + datetime.timedelta(seconds=seconds))
            await interaction.response.send_message(f"**{member}** has been timed out for {duration}.\nReason: {reason}")
        except Exception:
            await interaction.response.send_message("Format Error: Please use units like '10m', '1h', or '1d'.", ephemeral=True)

    @nextcord.slash_command(name="channel_lock", description="Toggles message permissions", guild_ids=guild_ids)
    @commands.has_permissions(manage_channels=True)
    async def channel_lock(self, interaction: Interaction, action: str = SlashOption(choices=["lock", "unlock"])):
        should_lock = (action == "lock")
        overwrite = interaction.channel.overwrites_for(interaction.guild.default_role)
        overwrite.send_messages = not should_lock
        
        await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
        status = "locked 🔒" if should_lock else "unlocked 🔓"
        await interaction.response.send_message(f"Channel status updated: **{status}**")

def setup(bot):
    bot.add_cog(moderation(bot))

