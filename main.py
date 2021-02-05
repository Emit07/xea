import discord
from discord.ext import commands

import os
from datetime import datetime

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print(f'XEA has launched at {datetime.now()}')


client.load_extension("cogs.moderation")

TOKEN = os.environ['TOKEN']
#client.run(os.environ.get("TOKEN"))
