import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

class moderation(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mute(self, ctx, user1 : discord.Member):
        if ctx.author.guild_permissions.administrator:
            role1 = discord.utils.get(user1.guild.roles, name="muted")
            await user1.add_roles(role1)
            user_url = user1.avatar_url
            embed = discord.Embed(
                title=f"{user1} has been muted!",
                description=f"{ctx.author} muted {user1}",
                colour=0xe86823
            )
            embed.set_thumbnail(url=user_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f"{ctx.author} does not have administrator!",
                description=f"{ctx.author} cannot mute people.",
                colour=0xe86823
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def unmute(self, ctx, user1 : discord.Member):
        role1 = discord.utils.get(user1.guild.roles, name="muted")
        await user1.remove_roles(role1)
        user_url = user1.avatar_url
        embed = discord.Embed(
            title=f"{user1} has been unmuted!",
            description=f"{ctx.author} unmuted {user1}",
            colour=0xe86823
        )
        embed.set_thumbnail(url=user_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def clear(self, ctx, amount=1, args=None):
        if amount > 0:
            try:
                await ctx.channel.purge(limit=amount+1)
                if args not in ["-n", "-h"]:
                    if amount > 1:
                        await ctx.send(f":white_check_mark: | successfully cleared {amount} messages")
                    else:
                        await ctx.send(f":white_check_mark: | successfully cleared {amount} message")
            except:
                if args in ["-n", "-h"]:
                    await ctx.send(f":x: | Error! could not clear messages")


def setup(bot):
    bot.add_cog(moderation(bot))