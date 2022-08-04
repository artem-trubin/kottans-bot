import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$htaq"):
        await message.channel.send(
            """
Пропонуємо нашу інструкцію про те, як краще задавати питання!
https://github.com/kottans/frontend/blob/2022_UA/HTAQ.md
        """
        )

    if message.content.startswith("$faq"):
        await message.channel.send(
            """
Щоб продивитись популярні питання перейдіть за цим посиланням:
https://github.com/kottans/frontend/blob/2022_UA/faq.md
            """
        )


client.run(os.getenv("TOKEN"))
