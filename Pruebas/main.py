import discord
from discord.ext import commands
import os

prefix = '!'
intents = discord.Intents.all()
description = "Esto es un bot de pruebas BY Yoshebas"
Token = 'MTExMDIyODY1MzE4NDM5MzMyMA.G5lGam.ctpj_qkKqQDDdRDjlRs9ySe9jyFeN7Iza_fRAQ'

bot = commands.Bot(command_prefix = prefix, intents = intents, description = description)

@bot.event
async def on_ready():
    id = 1110251172482257066
    canal = bot.get_channel(id)
    print(f"El bot esta listo como {bot.user.name}")
    #await canal.send(f"El bot esta listo como {bot.user.name}")

#Se une al chat de voz
@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        print(f"{ctx.author.name} no esta en un chat de voz")
    
    else:
        print(f"{ctx.author.name} esta en un chat de voz")
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

#sale del chat de voz
@bot.command()
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send(f"{ctx.author.name} tu eres tonto, no estoy en un canal de voz")
        
    else:
        await ctx.voice_client.disconnect()
        print("Estoy fuera")
        
#elimina la cantidad de mensajes que le digas del canal desde el que lo envias    
@bot.command()
async def cls(ctx, amount=0):
        await ctx.channel.purge(limit=amount+1)

#guarda un audio que tienes que adjuntar con el nombre que lo va a guardar
@bot.command()
async def save(ctx, variable):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No se ha adjuntado nungun archivo de audio")
        return
    
    elif variable is None:
        ctx.send("No hay ningun nombre para el audio")
    
    audio_attachment = ctx.message.attachments[0]
    await audio_attachment.save(f'{variable}.mp3')
    await ctx.send(f"El audio se guardo correctamente como {variable}.mp3")


@bot.command()
async def play(ctx, sound_name):
    if ctx.voice_client is None:
        await ctx.invoke(bot.get_command('join'))
    
    if ctx.author.voice is None:
        await ctx.send("Debes estar en un canal de voz para utilizar este comando.")
        return 0
    
    try:
        # Ruta de la carpeta donde se encuentran los audios
        audios_folder = 'audios/'
        
        # Obtener la lista de archivos de audio en la carpeta
        audio_files = os.listdir(audios_folder)
        
        # Verificar si el archivo de audio solicitado existe
        if sound_name + '.mp3' in audio_files:
            audio_path = os.path.join(audios_folder, sound_name + '.mp3')
            
            # Reproducir el audio solicitado
            await ctx.voice_client.play(discord.FFmpegPCMAudio(audio_path))
            await ctx.send(f'Reproduciendo: {sound_name}')
                
        else:
            await ctx.send('El audio solicitado no existe.')
            
    except Exception as e:
        await ctx.send("No se pudo reproducir el audio.")
        print(f'Error al reproducir el audio: {e}')






bot.run(Token)
