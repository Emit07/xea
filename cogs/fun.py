import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

from spongebobcase import tospongebob
import json
import requests

def pull_sub(sub=None, index=0):
    if sub is None:
        sub="all"
    URL = f"https://www.reddit.com/r/{sub}.json"
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
        if image_url.split(".")[-1] not in ["jpg", "jpeg", "png", "bmp"]:
            image_url = None
        return {"error": None, "title": title, "author": author, "subreddit":subreddit, "score":score, "image_url":image_url, "permalink": permalink}
    else:
        return {"error": r}

class fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, user1 : discord.Member=None):
        if user1 is not None:
            r = requests.get("https://some-random-api.ml/animu/hug")
            r_json = r.json()

            author = str(ctx.author).split('#')[0]
            hugged = str(user1).split('#')[0]

            embed = discord.Embed(
                title=f"{author} hugs {hugged}",
                colour=0xe86823
            )
            embed.set_image(url=r_json["link"])
        else:
            embed = discord.Embed(
                title="You can\'t hug nobody!",
                colour=0xe86823
            )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def spongebob(self, ctx, *, text=None):
        await ctx.send(tospongebob(text))

    @commands.command()
    async def reddit(self, ctx, sub=None, index=0):
        reddit_data = pull_sub(sub, index)
        if reddit_data["error"] is None:
            permalink = reddit_data["permalink"]
            link = f"https://reddit.com{permalink}"
            score = reddit_data["score"]
            title = reddit_data["title"]
            subreddit = reddit_data["subreddit"]
            embed_title = f"{title} | {subreddit}"
            embed = discord.Embed(
                    title=embed_title,
                    url=link,
                    colour=0xe86823
                )
            img_url = reddit_data["image_url"]
            author = reddit_data["author"]
            embed.set_footer(text=f"u/{author} | score : {score}")
            if img_url != None:
                embed.set_image(url=img_url)
        else:
            error = reddit_data["error"]
            embed = discord.Embed(
                    title=f"Error : {error}",
                    colour=0xe86823
                )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))