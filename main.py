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

@client.event
async def on_command_error(ctx, error):
    print(error)

@client.event
async def on_message(message):

    mention = f'<@!{client.user.id}>'
    if mention in message.content:
        embed = discord.Embed(
            title="You Mentioned Me!",
            description="my prefix is `?`. Need more help? you can do `?help` and continue from there. Wanna see my code? Check it out here https://github.com/emit07/xea",
            colour=0xe86823
        )
        await message.channel.send(embed=embed)

    await client.process_commands(message)

client.load_extension("cogs.helpcmd")
client.load_extension("cogs.moderation")
client.load_extension("cogs.polls")
client.load_extension("cogs.info")
client.load_extension("cogs.fun")

TOKEN = os.environ['TOKEN']
client.run(TOKEN)