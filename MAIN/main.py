import discord
from discord.ext import commands, tasks
import random
import os
from dotenv import load_dotenv
from comandosBOT import *
from BomDia import bom_dia_task
import json

load_dotenv()
Token_Bot = os.getenv("Token_Bot")

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)


@bot.event #sincronizar slash comands / inicializar tasks / msg de inicializacao
async def on_ready():
    await bot.tree.sync()
    bom_dia.start()
    print("BOT ligado")
    

#funcoes de commando do comandosBOT.py
@bot.command()
async def comandos(context:commands.Context):
    await context.reply(help_msg)

@bot.command()
async def jhon(context:commands.Context):
    command_jhon (context)   
    await context.reply(embed=embed_jhon)

@bot.command()
async def risada(context:commands.context):
    command_risada(context)
    await context.reply(embed=embed_risada)

@bot.command()
async def saka(context:commands.context):
    command_saka(context)
    await context.reply(embed=embed_saka)    

@bot.command()
async def primi(context:commands.context):
    command_primi(context)
    await context.reply(embed=embed_primi)

@bot.command()
async def thi(context:commands.context):
    command_thi(context)
    await context.reply(embed=embed_thi)
       
@bot.command()
async def delta(context:commands.context):
    command_delta(context)
    await context.reply(embed=embed_delta)

@bot.command()
async def watso(context:commands.context):
    command_watso(context)
    await context.reply(embed=embed_watso)


#outras funcoes
@bot.event #evento ao reagir com 🤓 
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🤓":
        gifs = ["https://c.tenor.com/pUNC06ehYBsAAAAd/tenor.gif", "https://c.tenor.com/vIIrCJvC9KMAAAAd/tenor.gif", "https://c.tenor.com/s3sg_NM0VOUAAAAd/tenor.gif", "https://c.tenor.com/NUzXmsZeSy8AAAAd/tenor.gif"]

        embed = discord.Embed(
            title= "NERDOLA",
            description= f"{user.mention} acha que \n {reaction.message.author.display_name} é exatamente assim:",
            color=14984215
        )
        embed.set_image(url= random.choice(gifs))
        await reaction.message.reply(embed= embed)
        


#abrindo os .json e escolhe um horario pela primeira vez

with open("OUTROS/tempo_exc.json", "r") as arq:
    lista_tempo_exc = json.load(arq)

with open("OUTROS/tempo.json", "r") as arq:
    lista_tempo = json.load(arq)

estado_tempo = {"tempo": random.choice(lista_tempo), "ult_dia": 30}

#inicializacao da funcao

@tasks.loop(minutes=1) #task para mandar bomdia 1x por dia
async def bom_dia():
    await bom_dia_task(bot, lista_tempo, lista_tempo_exc, estado_tempo)
    
            

@bot.tree.command()
async def betinha(interact:discord.Interaction, membro:discord.Member):
    citar = membro.mention
    imagem = discord.File("OUTROS/betinha.png", "beta.png")
    embed_beta = discord.Embed()
    embed_beta.set_image(url="attachment://beta.png")
    embed_beta.title= "BETINHA"
    embed_beta.description= f"SOBRA NADA PRO {membro.mention}"
    embed_beta.set_footer(text="It's Over, Brutal...")
    await interact.response.send_message(citar, embed=embed_beta, file=imagem)

bot.run(Token_Bot)
