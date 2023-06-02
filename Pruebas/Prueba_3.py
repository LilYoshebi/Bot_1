import discord
from discord.ext import commands

prefix = '!'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = prefix, intents = intents, description="this is a testing bot")

@bot.event
async def on_ready():
    print(f"El bot esta listo como {bot.user.name} - {bot.user.id}")
    

@bot.command(name="ping", )
async def ping(ctx):
     await ctx.send('pong')

@bot.command()
async def cls(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f"Se elimeinaron {amount} mensajes")
    
    
    
@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send(f"{ctx.author.name} metete en un canal de voz degraciao")
        
    else:
        try:
            await ctx.author.voice.channel.connect(reconnect=True, self_deaf=False, self_mute=False)
            await ctx.send("Estoy en el chat de voz")

        except:
            await ctx.send("No me he podido conectar")
            
@bot.command()
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send("No estoy en ningun canal de voz")
    
    else:
        await ctx.voice_client.disconnect()
        await ctx.send("Ya estoy sali del chat de voz")
    
    
bot.run('MTExMDIyODY1MzE4NDM5MzMyMA.G5lGam.ctpj_qkKqQDDdRDjlRs9ySe9jyFeN7Iza_fRAQ')
