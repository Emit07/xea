import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

import json

class config(Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(config(bot))