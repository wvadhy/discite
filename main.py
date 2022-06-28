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
    if msg.content.startswith('inspire'):
        await msg.channel.send(fetchmsg())

    if msg.content.startswith('encode'):
        pswrd = msg.content.split('encode ',1)[1]
        await msg.channel.send(f"```{Coder.encode(pswrd)}```")

    if msg.content.startswith('decode'):
        pswrd = msg.content.split('decode ',1)[1]
        await msg.channel.send(f"```{Coder.decode(int(pswrd))}```")

client.run("OTkxMTA5NDUwMjM0NjA1NjA4.G9hzdt.YuF-izuZuQtrGXdZWlQ-8DAyHjlYW1RXG-cdx4")