import nextcord
import random
from nextcord.ext import commands
from nextcord.abc import GuildChannel
from nextcord import Interaction, interactions, SlashOption, ChannelType


class slash(commands.cog):
    def _init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name = "dhillan", description= "Give dhillan dialogues")
    async def dhillan(self, Interaction: Interaction):
        dhillan = [
               "all hates me anyways",
        "think what u want",
        "tell what u want",
        "roast what u want",
        "frick u mate",
        "poi chavada",
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
        "GOOGLE SEND 100 GUNDAAS TO MAAM'S HOUSE",
        "tududududdududud"
        ]
        dhillan = random.choice(dhillan)
        await Interaction.response.send_message(dhillan)


def setup(bot):
    bot.add_cog(slash(bot))




