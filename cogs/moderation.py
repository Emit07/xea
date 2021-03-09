
"""
This file is to do with all the moderation commands.

TODO check some permissions
TODO manage messages can mute themselfs
"""

import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog
import main
import json

client = commands.Bot(command_prefix="?")

class moderation(Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_mute(self, ctx):

        """
        This command adds the muted role permissions
        to every text channel.
        """

        if ctx.author.guild_permissions.manage_messages:
            # gets muted role
            guild = ctx.guild
            muted_role = discord.utils.get(guild.roles, name="Muted")
            
            # if muted_role doesnt exist, make one
            if not muted_role:
                muted_role = await guild.create_role(name="Muted")

            try:
                # goes through every channel and changes permissions for muted role
                guild = ctx.guild
                for channel in guild.channels:
                    await channel.set_permissions(muted_role, send_messages=False, add_reactions=False)
            except Exception as e:
                await ctx.send(e)

    @commands.command()
    async def mute(
        self,
        ctx,
        user1 : discord.Member = None,
        *, 
        reason=None
    ):

        # this command mutes the specified user

        # checks if author has manage messages perm
        if ctx.author.guild_permissions.manage_messages:
            # checks if victim is not an administrator
            if not user1.guild_permissions.administrator:
                # gets role
                guild = ctx.guild
                muted_role = discord.utils.get(guild.roles, name="Muted")

                # creates muted role and adds it to every channel
                if not muted_role:
                    muted_role = await guild.create_role(name="Muted")

                    # loops over channels and adds permissions
                    for channel in guild.channels:
                        await channel.set_permissions(muted_role, send_messages=False, add_reactions=False)
                
                # adds muted role to specified user
                await user1.add_roles(muted_role)

                embed = discord.Embed(
                    title=f"{user1} has been muted!",
                    description=f"**Reason:** {reason}",
                    colour=0xe86823
                )

                # sets thumbnail to the users avatar
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
        if ctx.author.guild_permissions.manage_messages:
            if not user1.guild_permissions.administrator:
                guild = ctx.guild
                muted_role = discord.utils.get(guild.roles, name="Muted")

                if not muted_role:
                    muted_role = await guild.create_role(name="Muted")

                    for channel in guild.channels:
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
    async def kick(
        self,
        ctx,
        user1 : discord.Member=None,
        *,
        reason=None
    ):
        if ctx.author.guild_permissions.kick_members:
            await user1.kick(reason=reason)
            embed = discord.Embed(
                title=f":white_check_mark: {user1} has been kicked",
                description=f"reason: {reason}",
                colour=0xe86823
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["slow", "delay"])
    async def slowmode(self, ctx, seconds: int):
        if ctx.author.guild_permissions.manage_messages:
            if seconds is not None:
                if seconds <= 21600 and seconds >= 0:
                    try:
                        await ctx.channel.edit(slowmode_delay=seconds)
                        if seconds == 1: s = ""
                        else: s = "s"
                        await ctx.send(f":white_check_mark: Set the slowmode delay to {seconds} second{s}")
                    except Exception as e:
                        await ctx.send(f":x: {e}")
                else:
                    if seconds > 21600: await ctx.send(":x: slowmode delay cannot be longer than 6 hours")
                    if seconds < 0: await ctx.send(":x: slowmode delay must be a positive number")
            else:
                await ctx.send(":x: time was empty")

    @commands.command()
    async def warn(
        self,
        ctx,
        user1 : discord.Member=None,
        *,
        reason=None
    ):
        if ctx.author.guild_permissions.manage_messages:
            if not user1.guild_permissions.administrator:
                embed = discord.Embed(
                    title=f"{user1} has been Warned",
                    description=f"reason: {reason}",
                    colour=0xeb4034
                )
                user_url = user1.avatar_url
                embed.set_thumbnail(url=user_url)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    title=":x: you cannot warn an administrator",
                    colour=0xe86823
                )

                await ctx.send(embed=embed)


    @commands.command()
    async def clear(self, ctx, amount=1, args=None):
        if ctx.author.guild_permissions.manage_messages:
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