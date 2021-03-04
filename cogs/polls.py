import discord
from discord import Embed, Member
from discord.ext import commands
from discord.ext.commands import Cog

from datetime import datetime
import datetime

import json 
import requests

def pull_sub(sub=None, index=0):
    if sub is None:
        sub="all"
    URL = "https://www.reddit.com/r/polls.json"
    r = requests.get(URL, headers = {'User-agent': 'Chrome'})
    if str(r) == "<Response [200]>":
        r_json = r.json()
        top_post = r_json["data"]["children"][index]["data"]
        subreddit = top_post["subreddit_name_prefixed"]
        title = top_post["title"]
        author = top_post["author"]
        score = top_post["score"]
        image_url = top_post["url"]
        permalink = top_post["permalink"]
        if image_url.split(".")[-1] not in ["jpg", "jpeg", "png", "bmp", "gif"]:
            image_url = None
        return {"error": None, "title": title, "author": author, "subreddit":subreddit, "score":score, "image_url":image_url, "permalink": permalink}
    else:
        return {"error": r}

class polls(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, question=None):
        emojis = ["👍", "👎", "🤷‍♂️"]

        for emoji in emojis:
            await ctx.message.add_reaction(emoji)
    
    @commands.command()
    async def pollx(self, ctx, question, *options):
        if ctx.author.guild_permissions.manage_messages:
            embed_new = discord.Embed(
                title=question,
                colour=0xe86823
            )

            numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

            lines = ""
            for index, option in enumerate(options):
                lines += f"\n{numbers[index]} {option}"

            embed_new.add_field(name="**Options**", value=lines)
            message = await ctx.send(embed=embed_new)
            for index, option in enumerate(options):
                await message.add_reaction(numbers[index])

    @commands.command(aliases=['rpoll'])
    async def pollr(self, ctx):
        URL = "https://www.reddit.com/r/polls.json"
        r = requests.get(URL, headers = {'User-agent': 'Chrome'})
        if str(r) == "<Response [200]>":
            idx = 2
            post = r.json["data"]["children"][idx]["data"]

            options = post["poll_data"]["options"]

            embed = discord.Embed(
                title=post["title"],
                colour=0xe86823
            )

            numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

            lines = ""
            for index, option in enumerate(list(options)):
                reddit_option = options[index]["text"]
                lines += f"\n{numbers[index]} {reddit_option}"

            embed_new.add_field(name="**Options**", value=lines)
            message = await ctx.send(embed=embed_new)
            for index, option in enumerate(options):
                await message.add_reaction(numbers[index])

def setup(bot):
    bot.add_cog(polls(bot))