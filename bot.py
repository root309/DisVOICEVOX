import discord
from discord.ext import commands
import asyncio
import os
from voicevox import Himari

FFmpeg_PATH = os.getenv('FFmpeg_PATH')
TOKEN_DATA = os.getenv('TOKEN_DATA')
TOKEN = TOKEN_DATA
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Botが準備完了したときに実行するイベント
@bot.event
async def on_ready():
    print('ログイン')

# !speakコマンドが入力されたときに実行する関数
@bot.command()
async def speak(ctx, *, text):
    if not ctx.message.author.voice:
        await ctx.send("音声チャンネルに接続していません")
        return
    # Botが既にボイスチャンネルに接続している場合
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect() # ボイスチャンネルから切断する

    voice_channel = ctx.message.author.voice.channel
    # ボイスチャンネルに接続する
    vc = await voice_channel.connect()
    # VoiceVoxでテキストを音声に変換する
    Himari.generate_wav(text)
    # ボイスチャンネルで音声を再生する
    vc.play(discord.FFmpegPCMAudio(executable=FFmpeg_PATH, source='audio.wav'))
    # 音声が再生されている間、待機する
    while vc.is_playing():
        await asyncio.sleep(1)
    await vc.disconnect()

bot.run(TOKEN)
