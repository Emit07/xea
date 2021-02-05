import discord
from discord.ext import commands

from datetime import datetime

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print(f'XEA has launched at {datetime.now()}')


client.load_extension("cogs.moderation")

client.run("NzgzNTIwODk5MDY4MTk4OTYy.X8b8sw.klwChSjgAiqWTeJDYR05cuJQbGw")