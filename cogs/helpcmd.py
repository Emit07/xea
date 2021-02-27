
import discord
from discord.ext import commands
from discord.ext.commands import Cog

import main

client = commands.Bot(command_prefix="?")
client.remove_command("help")

class helpcmd(Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(
            title="SlimBot Commands",
            colour=0xe86823
        )
        bot_url=client.user.avatar_url
        embed.set_thumbnail(url=bot_url)
        embed.add_field(name="Moderation", value="`?help moderation`", inline=False)
        embed.add_field(name="Fun", value="`?help fun`", inline=False)
        embed.add_field(name="Polls", value="`?help polls`", inline=False)
        embed.add_field(name="Info", value="`?help info`", inline=False)
        embed.add_field(name="Integrations", value="`?help integrations`", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def moderation(self, ctx):
        embed = discord.Embed(
            title="SlimBot Moderation Commands",
            colour=0xe86823
        )
        bot_url=client.user.avatar_url
        embed.set_thumbnail(url=bot_url)
        embed.add_field(name="`?mute [user] [reason]`", value="mutes a user in text channels", inline=False)
        embed.add_field(name="`?unmute [user]`", value="unmutes a user in text channels", inline=False)
        embed.add_field(name="`?warn [user] [reason]`", value="warns user (still working on system)", inline=False)
        embed.add_field(name="`?clear [amount]`", value="deletes a specified amount of messages", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def fun(self, ctx):
        embed = discord.Embed(
            title="Xea Fun Commands",
            colour=0xe86823
        )
        bot_url=client.user.avatar_url
        embed.set_thumbnail(url=bot_url)
        embed.add_field(name="`?hug [user]`", value="hugs the specified user", inline=False)
        embed.add_field(name="`?spongebob [text]`", value="turns the given text into sPoNGebOB cAsE", inline=False)
        embed.add_field(name="`?avatar {user}`", value="will get the avatar of specified user, if left empty gets authors avatar", inline=False)
        embed.add_field(name="`?owo [text]`", value="this will return owofied text", inline=False)
        embed.add_field(name="`?clap [text]`", value="this will add clap emojis to your text", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def polls(self, ctx):
        embed = discord.Embed(
            title="Xea Poll Commands",
            colour=0xe86823
        )
        bot_url=client.user.avatar_url
        embed.set_thumbnail(url=bot_url)
        embed.add_field(name="`?poll [question]`", value="will make a yes, no, \'shrug\' poll", inline=False)
        embed.add_field(name="`?pollx \"[question in quotes]\" \"Option one\" \"Option two\" \"Option three\"`", value="gives you server icon", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def info(self, ctx):
        embed = discord.Embed(
            title="Xea Info Commands",
            colour=0xe86823
        )
        bot_url=client.user.avatar_url
        embed.set_thumbnail(url=bot_url)
        embed.add_field(name="`?userinfo {user}`", value="gives you info about the user", inline=False)
        embed.add_field(name="`?icon`", value="gives you server icon", inline=False)
        await ctx.send(embed=embed)

    @help.command()
    async def integrations(self, ctx):
        embed = discord.Embed(
            title="Xea Integration Commands",
            colour=0xe86823
        )
        bot_url=client.user.avatar_url
        embed.set_thumbnail(url=bot_url)
        embed.add_field(name="`?r {subreddit} {index of post}`", value="returns post from reddit. Remeber index starts at 0", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(helpcmd(bot))