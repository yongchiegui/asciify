import aiohttp
import ascii
import base64
import discord
import json
import math

with open('config.json', 'r') as f:
    config = json.load(f)

APP_CLIENT_ID = config['DISCORD']['APP_CLIENT_ID']
BOT_TOKEN = config['DISCORD']['BOT_TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is up and running!")


@client.event
async def on_message(message):
    bot_tag = '<@' + str(APP_CLIENT_ID) + '>'

    if message.attachments and bot_tag in message.content:
        await asciify(message)


async def asciify(message):
    for attachment in message.attachments:
        url = attachment['url']
        dimensions = get_largest_allowable_dimensions(attachment['width'], attachment['height'])

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    image = await resp.read()
                    image = base64.b64encode(image)
                    result = ascii.asciify_base64(image, dimensions['width'], dimensions['height'])
                    await client.send_message(message.channel, '```' + result + '```')
                else:
                    await client.send_message(message.channel, 'I could not process your request, sorry!')


def get_largest_allowable_dimensions(width, height):
    """Get the largest possible width and height such that width x height <= 2000.
    2000 is the Discord message character limit."""

    ratio = width / height
    new_height = math.sqrt(2000 / ratio)
    new_width = ratio * new_height

    return {
        'width': int(new_width),
        'height': int(new_height)
    }


client.run(BOT_TOKEN)
