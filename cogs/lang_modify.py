from typing import Union
import random


#           ~~~~~~~~~~~~~~~~~~~~~~~~ TABLE OF CONTENTS ~~~~~~~~~~~~~~~~~~~~~~~~
# Line 13 - def owofy(
#               text: Union[str, list, tuple, set], *, wanky: bool = False, _print: bool = False
#       )
# Line 107 - def clap_emojifier(
#               text: Union[str, list, tuple, set], *, _print: bool = False
#           )
# Line 131 - def strong_british_accent(
#                           text: Union[str, list, tuple, set], *, add_dashes: bool = False, _print: bool = False
#                       )

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