import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

from datetime import datetime
import datetime

class info(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.starttime = print(str(datetime.datetime.now()).split('.')[0])

    @commands.command()
    async def uptime(self, ctx):
        embed = discord.Embed(
            title=f"SlimBot has been up since {self.starttime}",
            colour=0xe86823
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))