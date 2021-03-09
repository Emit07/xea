
"""
This cog is for the ?help command
some ugly looking lines in here fix those

TODO fix bot url issue with help commands
TODO ugly writing, do better

"""

import discord
from discord.ext import commands
from discord.ext.commands import Cog

import main

client = commands.Bot(command_prefix="?")
client.remove_command("help")

class helpcmd(Cog):
    def __init__(self, bot):
        self.bot = bot

    # puts command in a group
    @client.group(invoke_without_command=True)
    async def help(self, ctx):
        
        # This is the main help command

        embed = discord.Embed(
            title="SlimBot Commands",
            colour=0xe86823
        )

        # bot_url=client.user.avatar_url
        # embed.set_thumbnail(url=bot_url)

        # do this with tuples instead of having it cluttered and ugly
        embed.add_field(name="Moderation", value="`?help moderation`", inline=False)
        embed.add_field(name="Fun", value="`?help fun`", inline=False)
        embed.add_field(name="Polls", value="`?help polls`", inline=False)
        embed.add_field(name="Info", value="`?help info`", inline=False)
        embed.add_field(name="Integrations", value="`?help integrations`", inline=False)
        await ctx.send(embed=embed)

    # command group
    @help.command()
    async def moderation(self, ctx):

        # this command is for help with moderation commands

        embed = discord.Embed(
            title="SlimBot Moderation Commands",
            colour=0xe86823
        )

        # bot_url=client.user.avatar_url
        # embed.set_thumbnail(url=bot_url)

        embed.add_field(name="`?mute [user] [reason]`", value="mutes a user in text channels", inline=False)
        embed.add_field(name="`?unmute [user]`", value="unmutes a user in text channels", inline=False)
        embed.add_field(name="`?add_mute`", value="automaticlly adds mute perms to channels", inline=False)
        embed.add_field(name="`?kick [user] {reason}`", value="this will kick the specified user", inline=False)
        embed.add_field(name="`?slowmode [seconds]`", value="will change the slowmode delay in specified channel, 0 is off", inline=False)
        embed.add_field(name="`?warn [user] [reason]`", value="warns user (still working on system)", inline=False)
        embed.add_field(name="`?clear [amount] {arguments}`", value="deletes a specified amount of messages. Adding -n or -h will hide success message.", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def fun(self, ctx):

        # this command is for help with the 'fun' commands

        embed = discord.Embed(
            title="Xea Fun Commands",
            colour=0xe86823
        )

        # bot_url=client.user.avatar_url
        # embed.set_thumbnail(url=bot_url)

        embed.add_field(name="`?hug [user]`", value="hugs the specified user", inline=False)
        embed.add_field(name="`?spongebob [text]`", value="turns the given text into sPoNGebOB cAsE", inline=False)
        embed.add_field(name="`?avatar {user}`", value="will get the avatar of specified user, if left empty gets authors avatar", inline=False)
        embed.add_field(name="`?owo [text]`", value="this will return owofied text", inline=False)
        embed.add_field(name="`?clap [text]`", value="this will add clap emojis to your text", inline=False)
        await ctx.send(embed=embed)

    @help.command(aliases=["poll"])
    async def polls(self, ctx):

        # help with the poll commands

        embed = discord.Embed(
            title="Xea Poll Commands",
            colour=0xe86823
        )

        # bot_url=client.user.avatar_url
        # embed.set_thumbnail(url=bot_url)

        embed.add_field(name="`?poll [question]`", value="will make a yes, no, \'shrug\' poll", inline=False)
        embed.add_field(name="`?pollx \"[question in quotes]\" \"Option one\" \"Option two\" \"Option three\"`", value="creates a poll with custom options, requires manage messages permissions", inline=False)
        embed.add_field(name="`?pollr {Index}`", value="sends a poll from r/polls", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def info(self, ctx):

        # help with comands that give you stats and info

        embed = discord.Embed(
            title="Xea Info Commands",
            colour=0xe86823
        )

        # bot_url=client.user.avatar_url
        # embed.set_thumbnail(url=bot_url)

        embed.add_field(name="`?userinfo {user}`", value="gives you info about the user", inline=False)
        embed.add_field(name="`?icon`", value="gives you server icon", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def integrations(self, ctx):

        # help with integration commands

        embed = discord.Embed(
            title="Xea Integration Commands",
            colour=0xe86823
        )

        # bot_url=client.user.avatar_url
        # embed.set_thumbnail(url=bot_url)

        embed.add_field(name="`?r {subreddit} {index of post}`", value="returns post from reddit. Remeber index starts at 0", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpcmd(bot))