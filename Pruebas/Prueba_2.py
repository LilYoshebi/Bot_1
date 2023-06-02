import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

prefix = '$'

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name} - {bot.user.id}')

@bot.command()
async def save(ctx, variable):
    # Verifica si se adjuntó un archivo de audio al mensaje
    if len(ctx.message.attachments) == 0:
        await ctx.send("No se ha adjuntado ningún archivo de audio.")
        return

    # Descarga el archivo de audio adjunto
    audio_attachment = ctx.message.attachments[0]
    await audio_attachment.save(f'{variable}.mp3')

    await ctx.send(f"Audio guardado en la variable '{variable}'.")

@bot.command()
async def play(ctx, variable):
    voice_channel = discord.utils.get(ctx.guild.voice_channels,)

    # Verifica si el bot está en un canal de voz
    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(voice_channel)
    else:
        voice_client = await voice_channel.connect()

    # Verifica si el archivo de audio existe
    try:
        voice_client.stop()
        audio_file = f'{variable}.mp3'
        voice_client.play(discord.FFmpegPCMAudio(audio_file))
        await ctx.send(f"Reproduciendo el audio de la variable '{variable}'.")
    except FileNotFoundError:
        await ctx.send(f"No se encontró el archivo de audio para la variable '{variable}'.")

@bot.command()
async def close(ctx):
    # Verifica si el bot está en un canal de voz
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
        await ctx.send("Saliendo del canal de voz.")
    else:
        await ctx.send("No estoy en un canal de voz.")

import os

@bot.command()
async def delete(ctx, variable):
    try:
        audio_file = f'{variable}.mp3'
        os.remove(audio_file)
        await ctx.send(f"Variable '{variable}' eliminada.")
    except FileNotFoundError:
        await ctx.send(f"No se encontró el archivo de audio para la variable '{variable}'.")




bot.run('MTExMDIyODY1MzE4NDM5MzMyMA.G5lGam.ctpj_qkKqQDDdRDjlRs9ySe9jyFeN7Iza_fRAQ')