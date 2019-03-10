import io
import os

import aiohttp
import discord

import consts
from helpers import DiscordHelper


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        for name, locative in consts.NAMES_WITH_LOCATIVE.items():
            if DiscordHelper.regex_search(message, name):
                await DiscordHelper.add_reactions(
                    message,
                    (consts.EMOJI_UNICODES.get('thumb_up'))
                )
                await DiscordHelper.say_offensive_text(message, locative)

        for keyword in consts.KEYWORDS_TO_REACT:
            if DiscordHelper.regex_search(message, keyword):
                await DiscordHelper.add_reactions(
                    message,
                    (consts.EMOJI_UNICODES.get(char) for char in keyword)
                )

        if message.content.startswith(';;cat'):
            url = DiscordHelper.get_not_understanding_cat_url()
            filename = 'cat.png'

            if message.content[6:] == 'gif':
                url = DiscordHelper.get_random_cat_gif_url()
                filename = 'cat.gif'
            if message.content[6:] == '':
                url = DiscordHelper.get_random_cat_url()

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        data = io.BytesIO(await resp.read())
                        await message.channel.send(
                            file=discord.File(data, filename)
                        )


if __name__ == "__main__":
    token = os.environ.get('HUGONIK_TOKEN')
    assert token, "Hugonik's token has not been found"

    client = MyClient()
    client.run(token)
