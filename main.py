import discord
from discord.ext import commands
import os
from datetime import datetime

client = commands.Bot(command_prefix="?")
client.remove_command("help")

SHOW_ERRORS = True

@client.event
async def on_ready():
    print(f'XEA has launched at {datetime.now()}')
    amount_servers = len(client.guilds)
    activity = discord.Game(name=f"?help | {amount_servers} servers", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_command_error(ctx, error):
    global SHOW_ERRORS
    
    if SHOW_ERRORS:
        await ctx.send(error)

client.load_extension("cogs.helpcmd")
client.load_extension("cogs.moderation")
client.load_extension("cogs.polls")
client.load_extension("cogs.info")
client.load_extension("cogs.fun")

TOKEN = os.environ['TOKEN']
client.run(TOKEN)