import discord
from discord.ext import commands
import os
import random
import nacl

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
    await canal.send(f"El bot esta listo como {bot.user.name}")
    
@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return  # Ignora los mensajes enviados por el propio bot
    if "ceno" in ctx.content.lower():
        n = random.randint(0,4)
        frases = ["Ya esta el tontito con lo de siempre😘.",
                  " Mar y KOng",
                  "AsaltaCunas",
                  "RebañaCondones",
                  "Para Pelotudo",
                  "PeinaCalvas",
                  "BarrePiscinas",
                  "PellizcaBombillas"]
        # La palabra o frase específica está presente en el mensaje
        # Realiza la acción deseada, como enviar un mensaje o realizar alguna acción adicional.
        
        if n == 1 or n == 5:
            await ctx.channel.send(f"{ctx.author.name} " + frases[n])
        else:
            await ctx.channel.send(f"" + frases[n])

    # Procesa los demás eventos de mensaje como de costumbre
    await bot.process_commands(ctx)
    
    

#Se une al chat de voz
@bot.command(name="join", description="Entra al chat de voz")
async def join(ctx):
    if ctx.author.voice is None:
        print(f"{ctx.author.name} no esta en un chat de voz")
    
    else:
        print(f"{ctx.author.name} esta en un chat de voz")
        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

#sale del chat de voz
@bot.command(name="leave", description="Sale del chat de voz")
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send(f"{ctx.author.name} tu eres tonto, no estoy en un canal de voz")
        
    else:
        await ctx.voice_client.disconnect()
        print("Estoy fuera")
        
#elimina la cantidad de mensajes que le digas del canal desde el que lo envias    
@bot.command(name="clear", description="Elimina la cantidad de mensjaes que le digas del canal que lo envias")
async def cls(ctx, amount=0):
        await ctx.channel.purge(limit=amount+1)

#guarda un audio que tienes que adjuntar con el nombre que lo va a guardar
import os

@bot.command(name="save", description="Guarda en audio que le digas en la carpeta de los audios")
async def save(ctx, variable):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No se ha adjuntado ningún archivo de audio")
        return
    
    elif variable is None:
        await ctx.send("No hay ningún nombre para el audio")
        return
    
    audio_attachment = ctx.message.attachments[0]
    save_path = os.path.join("C:\\Users\\luism\\OneDrive\\Documents\\dc_audios", f"{variable}.mp3")
    await audio_attachment.save(save_path)
    await ctx.send(f"El audio se guardó correctamente como {variable}.mp3 en la carpeta de audios.")



@bot.command(name="play", description="Reproduce el audio que le digas")
async def play(ctx, sound_name):
    if ctx.voice_client is None:
        await ctx.invoke(bot.get_command('join'))
    
    if ctx.author.voice is None:
        await ctx.send("Debes estar en un canal de voz para utilizar este comando.")
        return 0
    
    try:
        # Ruta de la carpeta donde se encuentran los audios
        audios_folder = r'C:\Users\luism\OneDrive\Documents\dc_audios'
        
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
        print(f'Error al reproducir el audio: {sound_name}.mp3')



@bot.command()
async def delete(ctx, sound_name):
    try:
        # Ruta de la carpeta donde se encuentran los audios
        audios_folder = r'C:\Users\luism\OneDrive\Documents\dc_audios'
        
        # Obtener la lista de archivos de audio en la carpeta
        audio_files = os.listdir(audios_folder)
        
        # Verificar si el archivo de audio solicitado existe
        if sound_name + '.mp3' in audio_files:
            audio_path = os.path.join(audios_folder, sound_name + '.mp3')
            
            # elimina el archivo
            os.remove(audios_folder)
                
        else:
            await ctx.send('El audio solicitado no existe.')
            
    except Exception as e:
        print(f'Error al reproducir el audio: {sound_name}.mp3')



#Es el Embed
@bot.command(name="panel", description="muestra todos los audios disponibles")
async def panel(ctx):
    folder_path = r'C:\Users\luism\OneDrive\Documents\dc_audios'
    audio_files = os.listdir(folder_path)

    embed = discord.Embed(title="Panel de Audios", color=discord.Color.blue())
    
    for file_name in audio_files:

        embed.add_field(name="", value=file_name, inline=False)
        
    await ctx.send(embed=embed)



bot.run(Token)
