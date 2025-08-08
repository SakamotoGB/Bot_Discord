import discord
from discord.ext import commands, tasks
import datetime
import pytz
import random
import os
from dotenv import load_dotenv
from comandosBOT import *

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
tempo_horas = random.randint(0, 23)
tempo_mins = random.randint(0, 59)
ult_dia = 1
tempo_excluido = [0000]

@tasks.loop(minutes=1) #task para mandar bomdia 1x por dia
async def bomdia():
    global tempo_horas, tempo_mins, ult_dia, tempo_excluido
    agora = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
    id_membro = bot.get_user(ID_Sakas) #sakas
    msg = ""
    canal = bot.get_channel(ID_Chat_Geral) #geral

    embed = discord.Embed(
        title="BOM DIA",
        description=(f" Ja são {agora.hour:0{2}}:{agora.minute:0{2}}, bora trabalhar"),
        color= 6854333
    )
    embed.set_image(url= "https://c.tenor.com/lRoBY1GfD0kAAAAC/tenor.gif")
        
    if not agora.day == ult_dia:
        if tempo_horas == agora.hour and tempo_mins == agora.minute:
            if tempo_horas == 6 and tempo_mins == 30:
                embed.add_field(name="ACORDEI NO HORARIO", value="finalmente chegou o dia")
                msg = "@everyone"

            await canal.send(f"{msg} {id_membro.mention}", embed=embed)

            tempo_excluido.append((tempo_horas*100)+(tempo_mins))
            n = 0
            while  n < len(tempo_excluido):   
                if(tempo_horas*100)+(tempo_mins) == tempo_excluido[n]:
                    tempo_horas = random.randint(0, 23)
                    tempo_mins = random.randint(0, 59)
                    n = -1          
                n = n+1
                
            
            ult_dia = agora.day
            embed.remove_field(index=0)
            msg = ""
            print(f"{tempo_excluido[len(tempo_excluido) - 1]:0{4}}")


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
