import discord

TOKEN = 'TOKEN'

client = discord.Client()

@client.eventasync
def on_ready():
    print('ログイン')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/himari':
        await message.channel.send('himaridayo')


client.run(TOKEN)