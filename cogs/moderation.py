import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

import json

class moderation(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mod_roles = []
    
    @commands.command()
    async def mute(self, ctx, user1 : discord.Member, *, reason=None):
        if ctx.author.guild_permissions.administrator:
            if not user1.guild_permissions.administrator:
                guild = ctx.guild
                muted_role = discord.utils.get(guild.roles, name="Muted")

                if not muted_role:
                    muted_role = await guild.create_role(name="Muted")

                    for channel in guild.channels:
                        print(channel)
                        await channel.set_permissions(muted_role, speak=False, send_messages=False)
                await user1.add_roles(muted_role)

                embed = discord.Embed(
                    title=f"{user1} has been muted!",
                    description=f"**Reason:** {reason}",
                    colour=0xe86823
                )
                user_url = user1.avatar_url
                embed.set_thumbnail(url=user_url)

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: you cannot mute an administrator",
                    colour=0xe86823
                )
                await ctx.send(embed=embed)

    @commands.command()
    async def unmute(self, ctx, user1 : discord.Member):
        if ctx.author.guild_permissions.administrator || ctx.author.roles in self.mod_roles:
            if not user1.guild_permissions.administrator:
                guild = ctx.guild
                muted_role = discord.utils.get(guild.roles, name="Muted")

                if not muted_role:
                    muted_role = await guild.create_role(name="Muted")

                    for channel in guild.channels:
                        print(channel)
                        await channel.set_permissions(muted_role, speak=False, send_messages=False)
                await user1.remove_roles(muted_role)

                embed = discord.Embed(
                    title=f"{user1} has been unmuted!",
                    colour=0xe86823
                )
                user_url = user1.avatar_url
                embed.set_thumbnail(url=user_url)

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=":x: you cannot unmute an administrator",
                    colour=0xe86823
                )
                await ctx.send(embed=embed)

    @commands.command()
    async def setmod(self, ctx, role1 : discord.Role=None):
        if role1 is not None:
            try:
                self.mod_roles.append(role1)
                embed = discord.Embed(
                    title=f":white_check_mark: Added {role1} to mod roles",
                    colour=0xe86823
                )
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(
                    title=":x: Error",
                    colour=0xe86823
                )
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=":x: Error : There needs to be an input for the role",
                colour=0xe86823
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def clear(self, ctx, amount=1, args=None):
        if ctx.author.guild_permissions.administrator:
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