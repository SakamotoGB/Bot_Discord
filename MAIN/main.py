import discord
from discord.ext import commands, tasks
import datetime
import pytz
import random
import os
from dotenv import load_dotenv

load_dotenv()
ID_Jhon = int(os.getenv("ID_Jhon"))
ID_Sakas = int(os.getenv("ID_Sakas"))
ID_Chat_Geral = int(os.getenv("ID_Chat_Geral"))
Token_Bot = os.getenv("Token_Bot")

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)


@bot.event #dar o sinal de inicializacao
async def on_ready():
    bomdia.start()
    print("BOT ligado")
    

@bot.command() #comando pra xingar um membro
async def jhon(ctx:commands.Context):
    #await ctx.message("AAAAAAAAAAAAAAAAAA")
    Jhon = ctx.guild.get_member(ID_Jhon)
    love = ctx.message.author.mention
    xingo = ["Vai tomar no cu", "Vai se foder", "Incel ->", "Patético ->", "Estrume ->", "Lixo ->", "Vadia ->",
             f"🏳️‍🌈  {love} QUER DAR PRO"]
    embed = discord.Embed(
        title= "AVISO DE SUMA IMPORTANCIA",
        description= f"{random.choice(xingo)} {Jhon.mention}",
        color= 0x1DB954
        # url=
    )
    embed.set_image(url=Jhon.avatar.url)
    await ctx.reply(embed=embed)
    
       

@bot.event #evento para adicionar msg ao reagir com 🤓 gif url: "https://c.tenor.com/pUNC06ehYBsAAAAd/tenor.gif" 
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🤓":
        gifs = ["https://c.tenor.com/pUNC06ehYBsAAAAd/tenor.gif", "https://c.tenor.com/vIIrCJvC9KMAAAAd/tenor.gif",
                 "https://c.tenor.com/s3sg_NM0VOUAAAAd/tenor.gif", "https://c.tenor.com/NUzXmsZeSy8AAAAd/tenor.gif"]
        embed = discord.Embed(
            title= "AVISO DE SUMA IMPORTANCIA",
            description= f"{user.mention} acha que \n {reaction.message.author.display_name} é exatamente assim:",
            color=14984215
        )
        embed.set_image(url= random.choice(gifs))
        await reaction.message.reply(embed= embed)
        

#variaveis da task bomdia
tempo_horas = random.randint(0, 23)
tempo_mins = random.randint(0, 59)
ult_dia = 16

@tasks.loop(minutes=1) #task para mandar bomdia 1x por dia
async def bomdia():
    global tempo_horas, tempo_mins, ult_dia
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
                        
            tempo_horas = random.randint(0, 23)
            tempo_mins = random.randint(0, 59)
            ult_dia = agora.day
            embed.remove_field(index=0)
            msg = ""


bot.run(Token_Bot)
