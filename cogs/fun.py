import discord
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog

from spongebobcase import tospongebob

from typing import Union
import random

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
        if image_url.split(".")[-1] not in ["jpg", "jpeg", "png", "bmp", "gif"]:
            image_url = None
        return {"error": None, "title": title, "author": author, "subreddit":subreddit, "score":score, "image_url":image_url, "permalink": permalink}
    else:
        return {"error": r}

def owofy(text: Union[str, list, tuple, set], *, wanky: bool = False, _print: bool = False):
    """translates your given text to owo!

    :param text: the string/array you want to translate to owo on
    :type text: Union[str, list, tuple, set]
    :param wanky: A boolean that represents if you want the word 'wank' in your translated text. Defaults to `False`
    :type wanky: bool
    :param _print: If you want to print the given output. Defaults to `False`
    :type _print: bool
    :return: Your requested, translated text in str/array/printed form!
    :rtype: Union[str, list, print()]
    """

    def last_replace(s, old, new):
        li = s.rsplit(old, 1)
        return new.join(li)

    def text_to_owo(textstr):

        exclamations = ("?", "!", ".", "*")

        prefixes = ["uwu ",
                    "owo ",
                    "Hewo >w< ",
                    "*W* ", "mmm~ uwu ",
                    "Oh... Hi there {} ".format(random.choice(['·///·', '(。O⁄ ⁄ω⁄ ⁄ O。)']))]  # I need a life, help me

        subs = {
            "why": "wai",
            "Why": "Wai",
            "Hey": "Hai",
            "hey": "hai",
            "ahw": "ao",
            "Hi": "Hai",
            "hi": "hai",
            "you": "u",
            'L': 'W',
            "l": "w",
            "R": "W",
            "r": "w"
        }

        textstr = random.choice(prefixes) + textstr
        if not textstr.endswith(exclamations):
            textstr += " uwu"

        smileys = [';w;', '^w^', '>w<', 'UwU', r'(・`ω\´・)']

        if not wanky:  # to prevent wanking * w *
            textstr = textstr.replace("Rank", "Ⓡank").replace(
                "rank", "Ⓡank"
            )
            textstr = textstr.replace("Lank", "⒧ank").replace(
                "lank", "⒧ank"
            )

        textstr = last_replace(textstr, "there!", "there! *pounces on u*")

        for key, val in subs.items():
            textstr = textstr.replace(key, val)

        textstr = last_replace(textstr, '!', '! {}'.format(random.choice(smileys)))
        textstr = last_replace(textstr, '?', '? {}'.format(random.choice(['owo', "O·w·O"])))
        textstr = last_replace(textstr, '.', '. {}'.format(random.choice(smileys)))

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        if not wanky:
            textstr = textstr.replace("Ⓡank", "rank").replace("⒧ank", "lank")

        for v in vowels:
            if 'n{}'.format(v) in textstr:
                textstr = textstr.replace('n{}'.format(v), 'ny{}'.format(v))
            if 'N{}'.format(v) in textstr:
                textstr = textstr.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

        return textstr

    if isinstance(text, list) or isinstance(text, tuple) or isinstance(text, set):
        owoed_msgs = []

        for abt_to_owo in text:
            owoed_msgs.append(
                text_to_owo(abt_to_owo)
            )

        return owoed_msgs if not _print else print(*owoed_msgs, sep="\n")

    return text_to_owo(text) if not _print else print(text_to_owo(text))


def clap_emojifier(text: Union[str, list, tuple, set], *, _print: bool = False):
    """Appends your given string/array the clap 👏 emoji after every word/space.

    :param text: The text/array you want to "translate"
    :param _print: A boolean that represents if the given text is going to get printed to the console or not. Defaults to `False`.
    :return: Your clapped text/array!
    :rtype: Union[str, list, print()]
    """

    # Main translator is one line long LMAO
    def clap_it(_):
        return " 👏 ".join([*_.split(" ")])

    if isinstance(text, list) or isinstance(text, tuple) or isinstance(text, set):
        clapped_msgs = []

        for msg in text:
            clapped_msgs.append(clap_it(msg))

        return clapped_msgs if not _print else print(*clapped_msgs, sep="\n")

    return clap_it(text) if not _print else print(clap_it(text))

class fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
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
    async def avatar(self, ctx, user : discord.Member=None):
        if user is None:
            user = ctx.author
        embed = discord.Embed(
            title=f"{user}\'s avatar",
            colour=0xe86823
        )
        user_avatar = user.avatar_url
        embed.set_thumbnail(url=user_avatar)
        await ctx.send(embed=embed)

    @commands.command()
    async def owo(self, ctx, *, text=None):
        if text is not None:
            owo_text = owofy(text)
            await ctx.send(owo_text)
        else:
            embed = discord.Embed(
                title=":x: | You have to input text to owofy",
                colour=0xe86823
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def clap(self, ctx, *, text=None):
        if text is not None:
            clap_text = clap_emojifier(text)
            await ctx.send(clap_text)
        else:
            embed = discord.Embed(
                title=":x: | You have to input text to clapify",
                colour=0xe86823
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=["reddit", "red"])
    async def r(self, ctx, sub=None, index=0):
        if sub not in ["5050", "fiftyfifty", "gore"]:
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
        else:
            embed = discord.Embed(
                title=f"This Subreddit has been banned from this bot",
                colour=0xe86823
            )

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
