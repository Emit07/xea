import discord
from discord import Embed
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
        if discord.Member == None:
            user1 = ctx.author
        embed = discord.Embed(
            title=f"{user1}\'s info",
            colour=0xe86823
        )
        created_at = user1.created_at.strftime("%d/%m/%Y %H:%M:%S")
        joined_at = user1.joined_at.strftime("%d/%m/%Y %H:%M:%S")
        embed.add_field(name="Name ", value=f"`{str(user1)}`", inline=False)
        embed.add_field(name="Top Role ", value=f"`{target.top_role.mention}`", inline=False)
        embed.add_field(name="Is Bot ", value=f"`{str(user1)}`", inline=False)
        embed.add_field(name="Created at ", value=f"`{created_at}`", inline=False)
        embed.add_field(name="Joined at ", value=f"`{joined_at}`", inline=False)
        embed.add_field(name="Boosted ", value=f"`{bool(user1.premium_since)}`", inline=False)
        embed.add_field(name="Activity ", value=f"`{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}`", inline=False)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title=f"{user1}\'s info",
            colour=0xe86823
        )
        created_at = ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S")
        joined_at = user1.joined_at.strftime("%d/%m/%Y %H:%M:%S")
        embed.add_field(name="Owner ", value=f"`{ctx.guild.owner}`", inline=False)
        embed.add_field(name="ID ", value=f"`{ctx.guild.id}`", inline=False)
        embed.add_field(name="Region ", value=f"`{ctx.guild.region}`", inline=False)
        embed.add_field(name="Created at ", value=f"`{created_at}`", inline=False)
        embed.add_field(name="Members ", value=f"`{len(ctx.guild.members)}`", inline=False)
        embed.add_field(name="Humans ", value=f"`{len(list(filter(lambda m: not m.bot, ctx.guild.members)))}`", inline=False)
        embed.add_field(name="Bots ", value=f"`{len(list(filter(lambda m: m.bot, ctx.guild.members)))}`", inline=False)
        embed.add_field(name="Bans", value=f"`{len(ctx.guild.bans())}`", inline=False)
        embed.add_field(name="Status", value=f"`{🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}}`", inline=False)
        embed.add_field(name="Text Channels ", value=f"`{len(ctx.guild.text_channels)}`", inline=False)
        embed.add_field(name="Voice Channels ", value=f"`{len(ctx.guild.voice_channels)}`", inline=False)
        embed.add_field(name="Categories ", value=f"`{len(ctx.guild.categories)}`", inline=False)
        embed.add_field(name="Roles ", value=f"`{len(ctx.guild.roles)}`", inline=False)
        embed.add_field(name="\u200b ", value="\u200b", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))