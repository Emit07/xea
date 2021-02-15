import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

import time

class info(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.starttime = time.time()

    @commands.command()
    async def uptime(self, ctx):
        uptime = time.time() - self.starttime()
        embed = discord.Embed(
            title=f"SlimBot has been up for {uptime}",
            colour=0xe86823
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))