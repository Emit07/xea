import discord
from discord.ext import commands
import os
from datetime import datetime

client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    # Output to the console
    print(f'XEA has launched at {datetime.now()}')
    
    # this sets the bots status to the amount of servers it is in
    amount_servers = len(client.guilds)
    activity = discord.Game(name=f"?help | {amount_servers} servers", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_command_error(ctx, error):
    # prints simpler errors without cluttering console,
    # also handles errors so bot doesnt freak
    print(error)

@client.event
async def on_message(message):

    # detects if a user mentions the bot
    mention = f'<@!{client.user.id}>'
    if mention == message.content:
        # sends information if a user DID ping them
        embed = discord.Embed(
            title="You Mentioned Me!",
            description="my prefix is `?`. I am currently on version 1. Need more help? you can do `?help` and continue from there. Wanna see my code? Check it out here https://github.com/emit07/xea",
            colour=0xe86823
        )
        await message.channel.send(embed=embed)

    # allows other commands to be proccessed
    await client.process_commands(message)


# loads cogs
client.load_extension("cogs.helpcmd")
client.load_extension("cogs.moderation")
client.load_extension("cogs.polls")
client.load_extension("cogs.info")
client.load_extension("cogs.fun")

# gets bot token from env vars and runs the bot
TOKEN = os.environ['TOKEN']
client.run(TOKEN)