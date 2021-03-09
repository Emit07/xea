import discord
from discord import Embed, Member
from discord.ext import commands
from discord.ext.commands import Cog

from datetime import datetime
import datetime

class info(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def userinfo(self, ctx, user1 : discord.Member=None):
        if user1 is None:
            user1 = ctx.author
        embed = discord.Embed(
            title=f"{user1}\'s info",
            colour=0xe86823
        )

        created_at = user1.created_at.strftime("%d/%m/%Y %H:%M:%S")
        joined_at = user1.joined_at.strftime("%d/%m/%Y %H:%M:%S")

        embed.set_thumbnail(url=user1.avatar_url)

        embed.add_field(name="Name ", value=f"`{str(user1)}`", inline=False)
        embed.add_field(name="Top Role ", value=f"`{user1.top_role}`", inline=False)
        embed.add_field(name="Is Bot ", value=f"`{str(user1.bot)}`", inline=False)
        embed.add_field(name="Created at ", value=f"`{created_at}`", inline=False)
        embed.add_field(name="Joined at ", value=f"`{joined_at}`", inline=False)
        embed.add_field(name="Boosted ", value=f"`{bool(user1.premium_since)}`", inline=False)
        embed.add_field(name="Activity ", value=f"`{str(user1.activity.type).split('.')[-1].title() if user1.activity else 'N/A'} {user1.activity.name if user1.activity else ''}`", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, user : discord.Member=None):
        if user is None:
            user = ctx.author
        embed = discord.Embed(
            title=f"{user}\'s avatar",
            colour=0xe86823
        )
        user_avatar = user.avatar_url
        embed.set_image(url=user_avatar)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def stats(ctx):
        embed = discord.Embed(
            title="SlimBot Statistics",
            colour=0xe86823
        )
        servers_amount = len(client.guilds)
        embed.add_field(name="Servers: ", value=f"`{servers_amount} servers`")
        await ctx.send(embed=embed)

    @commands.command()
    async def icon(self, ctx):
        embed = discord.Embed(
            title=f"Server Icon",
            colour=0xe86823
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))