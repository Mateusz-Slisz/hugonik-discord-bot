import random
import re

import consts


class DiscordHelper:
    @staticmethod
    def say_offensive_text(message, locative=None):
        text = 'Jeśli mowa o {0} to {1} {2} z niego {3}'.format(
            locative or consts.DEFAULT_LOCATIVE,
            random.choice(consts.ADJECTIVES),
            random.choice(consts.PLEASANT_WORDS),
            random.choice(consts.EMOTICONS)
        )

        return message.channel.send(text)

    @staticmethod
    def get_random_cat_url():
        return consts.RANDOM_CAT_URL + '/cat'

    @staticmethod
    def get_random_cat_gif_url():
        return consts.RANDOM_CAT_URL + '/cat/gif'

    @staticmethod
    def get_not_understanding_cat_url():
        return consts.RANDOM_CAT_URL + '/cat/says/NIE%20ROZUMIEĆ?size=100&color=red'

    @staticmethod
    def regex_search(message, name):
        return re.search(fr'\b({name})', message.content, re.IGNORECASE)

    @staticmethod
    async def add_reactions(message, reactions=None):
        for reaction in reactions or []:
            await message.add_reaction(reaction)
