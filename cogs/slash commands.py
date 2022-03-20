import nextcord
import random
from nextcord.ext import commands
from nextcord import Interaction


class slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name = "dialogues", description= "Give dialogues", guild_ids = [808704986485620736, 947151111037526096, 910811019608223754])
    async def dhillan(self, interaction: Interaction):
        dhillan = [
               "all hates me anyways",
        "think what u want",
        "tell what u want",
        "roast what u want",
        "frick u mate",
        "REVIVE REVIVE REVIVE TUUUUUUUUUUUUUU",
        "ok",
        "the shiddy never sleeps tonight DADADADA DADADA DADADADADAADA",
        "go frick yourself mate",
        "la la lae",
        "we are homies.  we eat together, we play together, we sleep together",
        "gud for you",
        "i tried so far and got so far. BUT IN THE END IT DOSENT EVEN MAAAAAAAATTTAR",
        "bye motherfathers",
        "bish",
        "this makes my butt feel good",
        "GOOGLE SEND 100 GANGSTERS TO MAAM'S HOUSE",
        "tududududdududud",
        "poi chavada"
        ]
        dhillan = random.choice(dhillan)
        await interaction.response.send_message(dhillan)


def setup(bot):
    bot.add_cog(slash(bot))




