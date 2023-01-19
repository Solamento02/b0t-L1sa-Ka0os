import discord
import os
import time
from datetime import datetime
from discord.ext import commands, tasks
from discord.ext.commands import bot
from dotenv import load_dotenv
from tokenize import Token
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="%", intents=intents)
Activity_string = "on {} servers.format(len(bot.guilds))"
now = datetime.now()
now_string=now.strftime("%d/%m/%Y %H:%M:%S")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "Você 👀"))
    print('Connected to bot: {}'.format(bot.user.name))
    current_time.start()

@bot.command(name="Hey")
async def send_hello(ctx):
    name = ctx.author.name
    print = "Rawr! " + name
    await ctx.send(print)

@bot.command(name="hey")
async def send_hello(ctx):
    name = ctx.author.name
    print = "Rawr!" + name
    await ctx.send(print)

@bot.command(name="Arô")
async def send_message(ctx):
    await ctx.send("Arô😸")
    await ctx.send("Oii")
    await ctx.send("Gay")

@bot.command(name="admin_")
async def send_message(ctx):
    name = "Noahzito#5972 e Zoroégay#3568"
    print = "Rawr!Os donos desse bot são: " + name
    await ctx.send(print)

@bot.command(name="Linhas")
async def send_message(ctx):
    name = ctx.author.name
    print = name

    await ctx.send("Eu espero")
    await ctx.send("que funcione")
    await ctx.send("esse código")
    await ctx.send("Novamente")
    await ctx.send(print + "❤")

@bot.command(name="Ajude")
async def send_message(ctx):
    name = ctx.author.name
    print = name

    await ctx.send("Os comandos são utilizados pelo sufixo de exclamação(!) sendo:")
    await ctx.send("!Hey")
    await ctx.send("!Calcule")
    await ctx.send("!segundos_historinha")
    await ctx.send("!Lisa?(teste de ms)")
    await ctx.send(" Obrigade_Lisa! " + " Obrigada_Lisa! " + " Obrigado_Lisa! ")
    await ctx.send("Divirta-se utilizando eles pelo servidor " + name + "❤")

@bot.command(name="ajude")
async def send_message(ctx):
    name = ctx.author.name
    print = name

    await ctx.send("Os comandos são utilizados pelo sufixo da exclamação(!) sendo:")
    await ctx.send("!Hey")
    await ctx.send("!Calcule")
    await ctx.send("!segundos_historinha")
    await ctx.send("!Lisa?(teste de ms)")
    await ctx.send( "Obrigade_Lisa! " + " Obrigada_Lisa! " + " Obrigado_Lisa! ")
    await ctx.send("Divirta-se utilizando eles pelo servidor " + name + "❤")

@bot.command(name="pi")
async def send_message(ctx):
    print = ("O número de pi,do alfabeto grego traduzido, sendo P, em nossa língua, matemáticamente é formado por: 3.14159265359.....Que é a relação entre o perímetro e diâmetro de uma circuferência se quiser escutar alguém recitando recomendo esse link: https://cutt.ly/SSmhvsQ")
    await ctx.send(print)

@bot.command(name="segundos_historinha")
async def send_message(ctx):
    print = ("Os segundos, foram definidos por um relógio atômico extremamente potente,que é capaz de identificar períodos de oscilação, descobrindo assim que os segundos tem  9.192.631.770 períodos de oscilação no estado fundamental do átomo de césio 133, que é utilizado em radiações de microondas")
    await ctx.send(print)

@bot.command(name="Obrigade_Lisa!")
async def send_message(ctx):
    name = ctx.author.name
    print= "Lisa ama muito você ❤ " + name 
    await ctx.send(print)

@bot.command(name="Obrigada_Lisa!")
async def send_message(ctx):
    name = ctx.author.name
    print = "Lisa ama muito você ❤ " + name
    await ctx.send(print)

@bot.command(name="Obrigado_Lisa!")
async def send_message(ctx):
    name = ctx.author.name
    print = "Lisa ama muito você ❤ " + name
    await ctx.send(print)

@bot.command(name="Lisa?")
async def ping(ctx):
    await ctx.send(f'Meow! {round(bot.latency * 1000)}ms')

@bot.command(name="cls")
async def clear(ctx,amount=1000):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount+1)

@bot.command(name="Calcule")
async def calculate_expression(ctx,expression):
    print = eval(expression)

    await ctx.send("Ah!Amiguinho isso dá " + str(print))

@bot.command(name="calcule")
async def calculate_expression(ctx,expression):
    print = eval(expression)

    await ctx.send("Ah!Amiguinho isso dá " +  str(print))

@bot.command(name="Horas")
async def current_time(ctx):
    now = datetime.now()
    now = now.strftime("%H:%M do dia %d/%m")

    await ctx.send(now)

@bot.command(name="horas")
async def current_time(ctx):
    now = datetime.now()
    now = now.strftime("%H:%M do dia %d/%m")

    await ctx.send(now)

@tasks.loop(minutes=360)
async def current_time():
    now = datetime.now()

    now = time.strftime("%H:%M do dia %d/%m")

    channel1 = bot.get_channel(seu canal)

    await channel1.send("Agora são " + now)

bot.load_extension("cogs.teste.cog")
bot.run(TOKEN)
