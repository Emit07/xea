import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

import youtube_dl

import os
from datetime import datetime

client = commands.Bot(command_prefix="?")
client.remove_command("help")


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@client.event
async def on_ready():
    print(f'XEA has launched at {datetime.now()}')
    amount_servers = len(client.guilds)
    activity = discord.Game(name=f"?help | {amount_servers} servers", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)    

@client.command()
async def jazz(ctx, url=None):
    if url is not None:
        if not ctx.author.voice:
            await ctx.send(":x: You are not connected to a voice channel!")
            return
        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

        server = ctx.message.guild
        voice_channel = server.voice_client
        
        player = await YTDLSource.from_url(url, loop=client.loop)
    else:
        await ctx.send(":x: Empty URL")

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
