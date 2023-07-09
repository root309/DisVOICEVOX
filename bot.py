import discord
import os

TOKEN_DATA = os.getenv('TOKEN_DATA')
TOKEN = TOKEN_DATA

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログイン')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/himari':
        await message.channel.send('himaridayo')

client.run(TOKEN)
