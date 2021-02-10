import discord
from discord.ext import commands

import os
from datetime import datetime

client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    print(f'XEA has launched at {datetime.now()}')
    amount_servers = len(client.servers)
    activity = discord.Game(name=f"?help | {amount_servers} servers", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)    

@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="SlimBot Commands",
        colour=0xe86823
    )
    bot_url=client.user.avatar_url
    embed.set_thumbnail(url=bot_url)
    embed.add_field(name="Moderation", value="`?help moderation`", inline=True)
    embed.add_field(name="Fun", value="`?help fun`", inline=True)
    await ctx.send(embed=embed)

@help.command()
async def moderation(ctx):
    embed = discord.Embed(
        title="SlimBot Moderation Commands",
        colour=0xe86823
    )
    bot_url=client.user.avatar_url
    embed.set_thumbnail(url=bot_url)
    embed.add_field(name="`?mute [user] [reason]`", value="mutes a user in text channels", inline=False)
    embed.add_field(name="`?unmute [user]`", value="unmutes a user in text channels", inline=False)
    embed.add_field(name="`?clear [amount]`", value="deletes a specified amount of messages", inline=False)
    await ctx.send(embed=embed)

@help.command()
async def fun(ctx):
    embed = discord.Embed(
        title="Xea Fun Commands",
        colour=0xe86823
    )
    bot_url=client.user.avatar_url
    embed.set_thumbnail(url=bot_url)
    embed.add_field(name="`?hug [user]`", value="hugs the specified user", inline=False)
    embed.add_field(name="`?spongebob [text]`", value="turns the given text into sPoNGebOB cAsE", inline=False)
    await ctx.send(embed=embed)

client.load_extension("cogs.moderation")
client.load_extension("cogs.config")
client.load_extension("cogs.fun")

TOKEN = os.environ['TOKEN']
client.run(TOKEN)