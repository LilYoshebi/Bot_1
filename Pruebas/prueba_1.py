import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

prefix = '$'

bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

audio_variables = {}

# Comprueba si el bot está conectado a un canal de voz
def is_connected(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


@bot.command()
async def save(ctx, variable_name: str):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        if attachment.content_type.startswith('audio'):
            audio = await attachment.read()
            audio_variables[variable_name] = audio
            await ctx.send(f'El audio se ha guardado en la variable "{variable_name}"')
        else:
            await ctx.send('El archivo adjunto no es un audio válido.')
    else:
        await ctx.send('No se encontró ningún archivo adjunto de audio.')


@bot.command()
async def play(ctx, variable_name: str):
    if not is_connected(ctx):
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
    else:
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if variable_name in audio_variables:
        audio = audio_variables[variable_name]
        with open('temp_audio.mp3', 'wb') as f:
            f.write(audio)

        source = FFmpegPCMAudio('temp_audio.mp3')
        voice_client.play(source)
    else:
        await ctx.send(f'No se encontró ningún audio en la variable "{variable_name}".')

@bot.command()
async def close(ctx):
    if is_connected(ctx):
        await ctx.voice_client.disconnect()
    else:
        await ctx.send('No estoy conectado a ningún canal de voz.')

@bot.command()
async def delete(ctx, variable_name: str):
    if variable_name in audio_variables:
        del audio_variables[variable_name]
        await ctx.send(f'La variable "{variable_name}" ha sido eliminada.')
    else:
        await ctx.send(f'No se encontró ninguna variable con el nombre "{variable_name}".')

    
bot.run('MTExMDIyODY1MzE4NDM5MzMyMA.G5lGam.ctpj_qkKqQDDdRDjlRs9ySe9jyFeN7Iza_fRAQ')

