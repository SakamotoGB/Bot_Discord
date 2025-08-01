import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()
ID_Jhon = int(os.getenv("ID_Jhon"))
ID_Sakas = int(os.getenv("ID_Sakas"))
ID_Risada = int(os.getenv("ID_Risada"))
ID_Primi = int(os.getenv("ID_Primi"))
ID_Thi = int(os.getenv("ID_Thi"))
ID_Delta = int(os.getenv("ID_Delta"))
ID_Watso = int(os.getenv("ID_Watso"))
corEMB = 6854333 #0x1DB954

help_msg ="!jhon \n!risada \n!saka \n!primi \n!thi \n!delta \n!watso"


embed_jhon = discord.Embed()
def command_jhon(ctx):
    Jhon = ctx.guild.get_member(ID_Jhon)
    love = ctx.message.author.mention
    xingo = ["Vai tomar no cu", "Vai se foder", "Incel ->", "Patético ->", "Estrume ->", "Lixo ->", "Vadia ->",
             f"🏳️‍🌈  {love} QUER DAR PRO", f"🏳️‍🌈 {Jhon.mention} QUER DAR PRO {love}"]
    escolha = random.choice(xingo)
    
    embed_jhon.set_image(url=Jhon.avatar.url)
    embed_jhon.title= "Xingamento Merecido"
    embed_jhon.description= f"{escolha} {Jhon.mention}"
    embed_jhon.color= corEMB
    if escolha == xingo[8]:
        embed_jhon.description= f"{escolha}"
    

embed_risada = discord.Embed()
def command_risada(ctx):
    risada = ctx.guild.get_member(ID_Risada)
    falas = ["Viciado em Romance", "Maldito Romântico", "Mago dos Animes", "Hater de Harém", "Oráculo do E7", "Emilia SIMP"]

    embed_risada.set_image(url=risada.avatar.url)
    embed_risada.title= f"La vem o {falas[5]}"
    embed_risada.description= f"vulgo {risada.mention}"
    embed_risada.color= corEMB


embed_saka = discord.Embed()
def command_saka(ctx):
    saka = ctx.guild.get_member(ID_Sakas)
    falas = ["Esperou o Fujimoto Cozinhar...", "Hater dos Gachas"]
    gif_esqueleto = "https://c.tenor.com/JaI_717cUxQAAAAC/tenor.gif"
    fala_final = random.choice(falas)

    if fala_final == falas[0]:
        embed_saka.set_image(url=gif_esqueleto)
        embed_saka.title= f"{falas[0]}"
    else:
        embed_saka.set_image(url= saka.avatar.url)
        embed_saka.title= f"La vem o {fala_final}"

    embed_saka.description= f"Vulgo {saka.mention}"
    embed_saka.color= corEMB


embed_primi = discord.Embed()
def command_primi(ctx):
    primi = ctx.guild.get_member(ID_Primi)
    falas = ["CEO de MEI", "Tarado da meia-noite", "ZZZ Enjoyer", "Busco SEXO, em pessoa"]

    embed_primi.set_image(url=primi.avatar.url)
    embed_primi.title= f"La vem o {random.choice(falas)}"
    embed_primi.description= f"vulgo {primi.mention}"
    embed_primi.color= corEMB


embed_thi = discord.Embed()
def command_thi(ctx):
    thi = ctx.guild.get_member(ID_Thi)
    falas = ["Inimigo das Férias", "Trabalhador escala 7x0", "Último FAN de Genshin", "Segurança de Pitty"]

    embed_thi.set_image(url= thi.avatar.url)
    embed_thi.title= f"La vem o {random.choice(falas)}"
    embed_thi.description= f"vulgo {thi.mention}"
    embed_thi.color= corEMB


embed_delta = discord.Embed()
def command_delta(ctx):
    delta = ctx.guild.get_member(ID_Delta)
    falas = ["Homem de 1,50m", "FEMBOY", "Defensor de Linux", "BA Enjoyer"]

    embed_delta.set_image(url= delta.avatar.url)
    embed_delta.title= f"La vem o {random.choice(falas)}"
    embed_delta.description= f"vulgo {delta.mention}"
    embed_delta.color= corEMB


embed_watso = discord.Embed()
def command_watso(ctx):
    watso = ctx.guild.get_member(ID_Watso)
    falas = ["Dooby Simp", "Dono de PC Bomba", "Trader de conta em GACHA", "Mestre das Novels"]

    embed_watso.set_image(url= watso.avatar.url)
    embed_watso.title= f"La vem o {random.choice(falas)}"
    embed_watso.description= f"vulgo {watso.mention}"
    embed_watso.color= corEMB
