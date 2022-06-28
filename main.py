import discord
import requests
import json
from Coder import Coder

client = discord.Client()

def fetchmsg():
    req = requests.get("https://api.kanye.rest/")
    convert = json.loads(req.text)
    return convert["quote"]

@client.event # -- how you register an event for discord api
async def on_ready(): # -- utilises callback functions
    print(f"discite started {client.user}")

@client.event
async def on_message(msg):

    print(f"{msg.author}")

    if msg.content.startswith('inspire'):
        await msg.channel.send(fetchmsg())

    if msg.content.startswith('encode'):
        pswrd = msg.content.split('encode ',1)[1]
        encoded = Coder.encode(pswrd)
        await msg.channel.send(f"```{encoded}```")

    if msg.content.startswith('decode'):
        pswrd = msg.content.split('decode ',1)[1]
        decoded = Coder.decode(int(pswrd))
        await msg.channel.send(f"```{decoded}```")

client.run("OTkxMTA5NDUwMjM0NjA1NjA4.G9hzdt.YuF-izuZuQtrGXdZWlQ-8DAyHjlYW1RXG-cdx4")