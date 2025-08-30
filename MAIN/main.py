import discord
from discord.ext import commands, tasks
from datetime import datetime, time
import pytz
import random
import os
from dotenv import load_dotenv
from comandosBOT import *
import json

load_dotenv()
ID_Sakas = int(os.getenv("ID_Sakas"))
ID_Chat_Geral = int(os.getenv("ID_Chat_Geral"))
Token_Bot = os.getenv("Token_Bot")

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)


@bot.event #sincronizar slash comands / inicializar tasks / msg de inicializacao
async def on_ready():
    await bot.tree.sync()
    bomdia.start()
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
        

#variaveis da task bomdia
with open("OUTROS/tempo_exc.json", "r") as arq:
    lista_tempo_exc = json.load(arq)

with open("OUTROS/tempo.json", "r") as arq:
    lista_tempo = json.load(arq)

estado_tempo = {"tempo": random.choice(lista_tempo), "ult_dia": 30}

@tasks.loop(minutes=1) #task para mandar bomdia 1x por dia
async def bomdia(lista_tempo=lista_tempo, lista_tempo_exc=lista_tempo_exc, estado_tempo=estado_tempo):

    agora = datetime.now(pytz.timezone("America/Sao_Paulo"))
    id_membro = bot.get_user(ID_Sakas) #sakas
    msg = ""
    canal = bot.get_channel(ID_Chat_Geral) #geral

    embed = discord.Embed(
        title="BOM DIA",
        description=(f" Ja são {agora.hour:0{2}}:{agora.minute:0{2}}, bora trabalhar"),
        color= 6854333
    )
    embed.set_image(url= "https://c.tenor.com/lRoBY1GfD0kAAAAC/tenor.gif")

    tempo = datetime.strptime(estado_tempo["tempo"], "%H:%M")
    
    ult_dia = estado_tempo["ult_dia"]


        
    if not agora.day == ult_dia:
        if tempo.hour == agora.hour and tempo.minute == agora.minute:
            if tempo.hour == 6 and tempo.minute == 30:
                embed.add_field(name="ACORDEI NO HORARIO", value="finalmente chegou o dia")
                msg = "@everyone"

            lista_total = 1440
            lista_atual = len(lista_tempo)
            chance = (1 / lista_atual) * 100
            fixo = agora.replace(hour=6, minute=30) #passa o horario fixo das 6h30
            timming = ""
            
            if agora >= fixo: #se agora for depois ou msm tempo de fixo
                delta = str(agora - fixo) #delta é a str da diferença dos malandro
                if len(delta) < 8: #essa brincadeira caso a hora<10, pra completar os caracter
                    delta = ("0" + delta).replace(":", "h")
                timming = f"Só {delta[0:5]} Atrasado"

            else: #msm coisa de antes, sóq agora é antes de fixo
                delta = str(fixo - agora)
                if len(delta) < 8:
                    delta = ("0" + delta).replace(":", "h")
                timming = f"Só {delta[0:5]} Adiantado"
            

            embed.set_footer(text= f"Chance: {chance:.2f}% || Days: {len(lista_tempo_exc)}/{lista_total}\nTimming: {timming}")
            await canal.send(f"{msg} {id_membro.mention}", embed=embed)

            lista_tempo_exc.append(tempo.strftime("%H:%M"))
            with open("OUTROS/tempo_exc.json", "w") as arq:
                json.dump(lista_tempo_exc, arq)

            lista_tempo.remove(tempo.strftime("%H:%M"))
            with open("OUTROS/tempo.json", "w") as arq:
                json.dump(lista_tempo, arq)

            estado_tempo["tempo"] = random.choice(lista_tempo)
            estado_tempo["ult_dia"] = agora.day
            

            embed.remove_field(index=0)
            msg = ""
            


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
