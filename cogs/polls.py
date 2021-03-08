import discord
from discord import Embed, Member
from discord.ext import commands
from discord.ext.commands import Cog

from datetime import datetime
import datetime

import json 
import requests

class polls(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, question=None):

        """
        This command adds some simple reactions to
        the message for a simple poll.
        """

        emojis = ["👍", "👎", "🤷‍♂️"]

        # this adds reactions to the original message
        for emoji in emojis:
            await ctx.message.add_reaction(emoji)
    
    @commands.command()
    async def pollx(self, ctx, question, *options):
        
        """
        This command returns a more complex poll 
        with different specified options.
        The author needs manage messages
        permissions to send this poll,
        this will prevent spam.
        """

        # checks if author has manage messages permissions
        # to prevent spam
        if ctx.author.guild_permissions.manage_messages:
            embed_new = discord.Embed(
                title=question,
                colour=0xe86823
            )

            numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

            # this function formats a single string
            # into multiple lines for the embed
            lines = ""
            for index, option in enumerate(options):
                lines += f"\n{numbers[index]} {option}"

            # formats embed and sends it
            embed_new.add_field(name="**Options**", value=lines)
            message = await ctx.send(embed=embed_new)

            # adds reactions to message
            for index, option in enumerate(options):
                await message.add_reaction(numbers[index])

    @commands.command(aliases=['rpoll'])
    async def pollr(self, ctx, idx=1):

        """
        Takes a poll from r/polls
        """

        if ctx.author.guild_permissions.manage_messages:
            URL = "https://www.reddit.com/r/polls.json"
            r = requests.get(URL, headers = {'User-agent': 'Chrome'})
            if str(r) == "<Response [200]>":
                post = r.json()["data"]["children"][idx]["data"]

                options = post["poll_data"]["options"]

                embed = discord.Embed(
                    title=post["title"],
                    colour=0xe86823
                )

                numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

                lines = ""
                for index, option in enumerate(list(options)):
                    reddit_option = options[index]["text"]
                    if reddit_option.upper() != 'RESULTS':
                        lines += f"\n{numbers[index]} {reddit_option}"

                embed.add_field(name="**Options**", value=lines)
                message = await ctx.send(embed=embed)
                for index, option in enumerate(options):
                    await message.add_reaction(numbers[index])

def setup(bot):
    bot.add_cog(polls(bot))