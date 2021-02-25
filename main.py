import discord
from discord.ext import commands

import os
from datetime import datetime

client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    print(f'XEA has launched at {datetime.now()}')
    amount_servers = len(client.guilds)
    activity = discord.Game(name=f"?help | {amount_servers} servers", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)    

@client.command()
async def jazz(self, ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()
        
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")

    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }


    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(["https://www.youtube.com/watch?v=Rm48uz2emp8"])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def stats(ctx):
    embed = discord.Embed(
        title="SlimBot Statistics",
        colour=0xe86823
    )
    servers_amount = len(client.guilds)
    embed.add_field(name="Servers: ", value=f"`{servers_amount} servers`")
    await ctx.send(embed=embed)

@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(
        title="SlimBot Commands",
        colour=0xe86823
    )
    bot_url=client.user.avatar_url
    embed.set_thumbnail(url=bot_url)
    embed.add_field(name="Moderation", value="`?help moderation`", inline=False)
    embed.add_field(name="Fun", value="`?help fun`", inline=False)
    embed.add_field(name="Info", value="`?help info`", inline=False)
    embed.add_field(name="Integrations", value="`?help integrations`", inline=False)
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
    embed.add_field(name="`?warn [user] [reason]`", value="warns user (still working on system)", inline=False)
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
    embed.add_field(name="`?avatar {user}`", value="will get the avatar of specified user, if left empty gets authors avatar", inline=False)
    embed.add_field(name="`?owo [text]`", value="this will return owofied text", inline=False)
    embed.add_field(name="`?clap [text]`", value="this will add clap emojis to your text", inline=False)
    await ctx.send(embed=embed)

@help.command()
async def info(ctx):
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
async def integrations(ctx):
    embed = discord.Embed(
        title="Xea Integration Commands",
        colour=0xe86823
    )
    bot_url=client.user.avatar_url
    embed.set_thumbnail(url=bot_url)
    embed.add_field(name="`?r {subreddit} {index of post}`", value="returns post from reddit. Remeber index starts at 0", inline=False)
    await ctx.send(embed=embed)

client.load_extension("cogs.moderation")
client.load_extension("cogs.info")
client.load_extension("cogs.fun")

TOKEN = os.environ['TOKEN']
client.run(TOKEN)
