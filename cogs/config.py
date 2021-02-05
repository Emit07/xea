import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

import json

class config(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def joinrole(self, ctx, role=None):
        if role is not None:
            guild = ctx.guild
            join_role = discord.utils.get(guild.roles, name=role)
            # if join_role is not None:
            #     with open("/data/join_role.json")

def setup(bot):
    bot.add_cog(config(bot))