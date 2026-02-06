import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random
import asyncio
from io import BytesIO
from PIL import Image
import humanfriendly

class utilityandfun(commands.Cog):
    """
    A comprehensive Cog combining Fun and Utility features.
    """
    # Centralized Guild IDs for easier maintenance
    guild_ids = [808704986485620736, 985909972971950110, 1010526444646060062, 1012306961364168774]

    def __init__(self, bot):
        self.bot = bot

    # --- UTILITY COMMANDS ---

    @nextcord.slash_command(name="timer", description="Sets a countdown timer", guild_ids=guild_ids)
    async def timer(self, interaction: Interaction, topic: str, time: str = "60s"):
        """Calculates time units and alerts the user when the duration expires."""
        try:
             seconds = humanfriendly.parse_timespan(time)
        except humanfriendly.InvalidTimespan:
            return await interaction.response.send_message("Invalid time format. Use formats like '30s', '5m', or '2h'.", ephemeral=True)

        
        
        embed = nextcord.Embed(
            title="Timer Set ⏱️", 
            description=f"Reminder for **{topic}** in {time}.", 
            color=nextcord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)
        
        await asyncio.sleep(seconds)
        await interaction.followup.send(f"{interaction.user.mention}, your timer for **{topic}** is up!")
        try:
            await interaction.user.send(f"Notification: Your timer for {topic} has finished.")
        except nextcord.Forbidden:
            pass # Ignore if User DMs are closed

    @nextcord.slash_command(name="timedpoll", description="Creates a poll that closes after a set time", guild_ids=guild_ids)
    async def timedpoll(self, interaction: Interaction, title: str, time: str, options: str):
        """Generates a poll, collects reactions, and summarizes results after a delay."""
        option_list = [opt.strip() for opt in options.split(",")]
        if not (2 <= len(option_list) <= 10):
            return await interaction.response.send_message("Please provide between 2 and 10 options.", ephemeral=True)

        time_convert = {"s": 1, "m": 60, "h": 3600}
        unit = time[-1].lower()
        time_period = int(time[:-1]) * time_convert.get(unit, 1)

        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        embed = nextcord.Embed(title=f"📊 {title}", description="React to vote!", color=nextcord.Color.green())

        for i, opt in enumerate(option_list):
            embed.add_field(name=f"Option {i+1}", value=f"{emojis[i]} {opt}", inline=False)

        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_message()

        for i in range(len(option_list)):
            await msg.add_reaction(emojis[i])

        await asyncio.sleep(time_period)
        
        # Refresh message to count reactions
        msg = await interaction.channel.fetch_message(msg.id)
        results_embed = nextcord.Embed(title=f"Final Results: {title}", color=nextcord.Color.gold())
        
        for i, opt in enumerate(option_list):
            reaction = nextcord.utils.get(msg.reactions, emoji=emojis[i])
            count = reaction.count - 1 if reaction else 0
            results_embed.add_field(name=opt, value=f"{count} votes", inline=True)

        await interaction.followup.send(embed=results_embed)
        await msg.delete()

    # --- FUN / SOCIAL COMMANDS ---

    @nextcord.slash_command(name="rate", description="Check your stats for various categories", guild_ids=guild_ids)
    async def rate(self, interaction: Interaction, category: str = SlashOption(choices=["sigma", "casual", "sus"]), member: nextcord.Member = None):
        """A unified rating command using SlashOption choices for a cleaner UI."""
        target = member or interaction.user
        percent = random.randint(0, 100)
        
        titles = {
            "sigma": "Sigma Rate 🗿",
            "casual": "Casual Rate 🎮",
            "sus": "Suspect Rate 📮"
        }
        
        embed = nextcord.Embed(
            title=titles[category], 
            description=f"{target.mention} is **{percent}%** {category}.",
            color=nextcord.Color.random()
        )
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="8ball", description="Ask the magic 8-ball a question", guild_ids=guild_ids)
    async def magic_8ball(self, interaction: Interaction, question: str):
        """Provides a randomized response to a user's question."""
        responses = ["Definitely!", "Most likely", "Maybe...", "I wouldn't count on it.", "Absolutely not.", "Ask again later."]
        embed = nextcord.Embed(title=f"❓ {question}", description=f"🎱 {random.choice(responses)}", color=nextcord.Color.purple())
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="dog", description="Edit a user's avatar onto a dog", guild_ids=guild_ids)
    async def patti(self, interaction: Interaction, user: nextcord.Member):
        """Uses Pillow to manipulate images by overlaying a user's PFP onto a template."""
        await interaction.response.defer()
        try:
            background = Image.open(r"Sigma-bot\pics\patti.jpg'")
            asset = user.display_avatar.with_size(128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data).convert("RGBA").resize((153, 160))

            background.paste(pfp, (423, 131), pfp if pfp.mode == 'RGBA' else None)

            with BytesIO() as img_bin:
                background.save(img_bin, 'PNG')
                img_bin.seek(0)
                await interaction.followup.send(file=nextcord.File(img_bin, 'dog_edit.png'))
        except Exception:
            await interaction.followup.send("Error processing image. Check file paths!")

    # --- FRIEND QUOTES (Simplified logic) ---

    @nextcord.slash_command(name="dhillan", guild_ids=guild_ids)
    async def dhillan(self, interaction: Interaction):
        quotes = ["Think what you want!", "ok", "la la lae", "Good for you!", "We are homies."]
        await interaction.response.send_message(random.choice(quotes))

    @nextcord.slash_command(name="hecker", guild_ids=guild_ids)
    async def hecker(self, interaction: Interaction):
        quotes = ["Wassup guys!", "It's Jonathan who gave the code!", "Please don't remove me! :("]
        await interaction.response.send_message(random.choice(quotes))

    @nextcord.slash_command(name="emil", guild_ids=guild_ids)
    async def emil(self, interaction: Interaction):
        quotes = ["jk.....ROWLING", "ok man", "Wishing the same to you!", "banjo depresso kazooie"]
        await interaction.response.send_message(random.choice(quotes))

def setup(bot):
    bot.add_cog(utilityandfun(bot))