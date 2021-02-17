import discord
from discord import Embed, Member
from discord.ext import commands
from discord.ext.commands import Cog

from datetime import datetime
import datetime

class info(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.starttime = str(datetime.datetime.now()).split('.')[0]

    @commands.command()
    async def uptime(self, ctx):
        embed = discord.Embed(
            title=f"SlimBot has been up since {self.starttime}",
            colour=0xe86823
        )
        await ctx.send(embed=embed)
    
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
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title=f"Server Info",
            colour=0xe86823
        )
        created_at = ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S")

        bans_raw = await ctx.guild.bans()
        bans = len(bans_raw)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        embed.set_thumbnail(url=ctx.guild.icon_url)

        embed.add_field(name="Owner ", value=f"`{ctx.guild.owner}`", inline=False)
        embed.add_field(name="ID ", value=f"`{ctx.guild.id}`", inline=False)
        embed.add_field(name="Region ", value=f"`{ctx.guild.region}`", inline=False)
        embed.add_field(name="Created at ", value=f"`{created_at}`", inline=False)
        embed.add_field(name="Members ", value=f"`{len(ctx.guild.members)}`", inline=False)
        embed.add_field(name="Humans ", value=f"`{len(list(filter(lambda m: not m.bot, ctx.guild.members)))}`", inline=False)
        embed.add_field(name="Bots ", value=f"`{len(list(filter(lambda m: m.bot, ctx.guild.members)))}`", inline=False)
        embed.add_field(name="Bans", value=f"`{bans}`", inline=False)
        embed.add_field(name="Status", value=f"`Online: {statuses[0]} \nIdle: {statuses[1]} \nDND: {statuses[2]} \nOffline: {statuses[3]}`", inline=False)
        embed.add_field(name="Text Channels ", value=f"`{len(ctx.guild.text_channels)}`", inline=False)
        embed.add_field(name="Voice Channels ", value=f"`{len(ctx.guild.voice_channels)}`", inline=False)
        embed.add_field(name="Categories ", value=f"`{len(ctx.guild.categories)}`", inline=False)
        embed.add_field(name="Roles ", value=f"`{len(ctx.guild.roles)}`", inline=False)
        embed.add_field(name="\u200b ", value="\u200b", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))