import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class help(commands.Cog):
    """
    Custom Help menu to display available bot functionality.
    """
    
    guild_ids = [808704986485620736, 985909972971950110, 1010526444646060062, 1012306961364168774]

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="help", description="Displays a list of available commands", guild_ids=guild_ids)
    async def help(self, interaction: Interaction):
        """Generates a professional multi-field embed for bot documentation."""
        
        embed = nextcord.Embed(
            title="📜 Bot Command Directory",
            description="Use `/` to access these commands. Below is the list of available modules.",
            color=nextcord.Color.blue()
        )

        # --- Moderation Section ---
        embed.add_field(name="🛡️ Moderation", value=(
            "`/kick` - Remove a member\n"
            "`/ban` - Permanently ban a member\n"
            "`/timeout` - Temporarily mute a user\n"
            "`/clear` - Bulk delete messages"
        ), inline=False)

        # --- Utility Section ---
        embed.add_field(name="🛠️ Utility", value=(
            "`/timer` - Set a task reminder\n"
            "`/timedpoll` - Create a timed vote\n"
            "`/channel_lock` - Toggle channel permissions\n"
            "`/ping` - Check bot latency"
        ), inline=False)

        # --- Entertainment Section ---
        embed.add_field(name="🎮 Entertainment", value=(
            "`/rate` - Check Sigma, Casual, or Sus levels\n"
            "`/8ball` - Ask a magic prediction\n"
            "`/toss` - Flip a coin\n"
            "`/dog` - Edit a user into a dog\n"
            "`/rickroll` - Classic Rick Astley"
        ), inline=False)

        # --- Friend Quotes Section ---
        embed.add_field(name="💬 Social", value=(
            "`/dhillan` - Random Dhillan quotes\n"
            "`/hecker` - Random Hecker quotes\n"
            "`/emil` - Random Emil quotes"
        ), inline=False)

        embed.set_footer(text=f"Requested by {interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)
        
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))