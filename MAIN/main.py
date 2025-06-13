import discord
from discord.ext import commands, tasks
import datetime
import pytz
import random

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)


@bot.event #dar o sinal de inicializacao
async def on_ready():
    bomdia.start()
    print("BOT ESTRALANDO")


@bot.command() #comando pra mandar o jhon sucumbir
async def jhon(ctx:commands.Context):
    id_Jhon = ctx.guild.get_member(1359543956387397705)
    love = ctx.message.author.mention
    xingo = ["Vai tomar no cu", "Vai se foder", "Incel ->", "Patético ->", "Estrume ->", "Lixo ->", "Vadia ->",
             f"🏳️‍🌈  {love} QUER DAR PRO"]
    embed = discord.Embed(
        title= "AVISO DE SUMA IMPORTANCIA",
        description= f"{random.choice(xingo)} {id_Jhon.mention}",
        color= 0x1DB954
        # url=
    )
    embed.set_image(url=id_Jhon.avatar.url)
    await ctx.reply(embed=embed)
       

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🤓":
        await reaction.message.reply(f"{user.mention} acha que {reaction.message.author.display_name} é NERD")
        

agora = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
tempo_horas = random.randint(0, 23)
tempo_mins = random.randint(0, 59)
ult_dia = agora.day


@tasks.loop(minutes=1)
async def bomdia():
    global tempo_horas, tempo_mins, ult_dia, agora
    id_membro = bot.get_user(704238407274201151) #sakas
    msg = ""
    canal = bot.get_channel(1277024565788413999) #geral

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
             

bot.run("")
