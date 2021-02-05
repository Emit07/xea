import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

from spongebobcase import tospongebob
import json
import requests

class fun(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hug(self, ctx, user1 : discord.Member=None):
        if user1 is not None:
            r = requests.get("https://some-random-api.ml/animu/hug")
            r_json = r.json()

            author = str(ctx.author).split('#')[0]
            hugged = str(user1).split('#')[0]

            embed = discord.Embed(
                title=f"{author} hugs {hugged}",
                colour=0xe86823
            )
            embed.set_image(url=r_json["link"])
        else:
            embed = discord.Embed(
                title="You can\'t hug nobody!",
                colour=0xe86823
            )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def spongebob(self, ctx, *, text=None):
        await ctx.send(tospongebob(text))        


def setup(bot):
    bot.add_cog(fun(bot))