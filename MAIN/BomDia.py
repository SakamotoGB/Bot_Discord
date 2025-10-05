import discord
import random
import json
import datetime
from discord.ext import commands
import os
import pytz
from dotenv import load_dotenv

load_dotenv()
ID_Sakas = int(os.getenv("ID_Sakas"))
ID_Chat_Geral = int(os.getenv("ID_Chat_Geral"))

#inicializacao da funcao

async def bom_dia_task(bot, lista_tempo, lista_tempo_exc,estado_tempo):

    #declarar variavies para os condicionais
    agora = datetime.now(pytz.timezone("America/Sao_Paulo"))
    ult_dia = estado_tempo["ult_dia"]
    tempo = datetime.strptime(estado_tempo["tempo"], "%H:%M")

    if agora.day == ult_dia:
        return

    if tempo.hour != agora.hour or tempo.minute != agora.minute:
        return


#criacao da embed e set de variaveis basicas

    id_membro = bot.get_user(ID_Sakas) #sakas
    canal = bot.get_channel(ID_Chat_Geral) #geral
    msg = ""

    embed = discord.Embed(
        title="BOM DIA",
        description=(f" Ja são {agora.hour:0{2}}:{agora.minute:0{2}}, bora trabalhar"),
        color= 6854333
    )
    embed.set_image(url= "https://c.tenor.com/lRoBY1GfD0kAAAAC/tenor.gif")

    if tempo.hour == 6 and tempo.minute == 30:
        embed.add_field(name="ACORDEI NO HORARIO", value="finalmente chegou o dia")
        msg = "@everyone"

#setando variaveis para calculo   
    lista_total = 1440
    lista_atual = len(lista_tempo)
    chance = (1 / lista_atual) * 100
    fixo = agora.replace(hour=6, minute=30) #passa o horario fixo das 6h30


#calculando valores        
    
    if agora >= fixo: #se agora for depois ou msm tempo de fixo
        delta = str(agora - fixo) #delta é a str da diferença dos malandro
        atrasado_adiantado = "Atrasado"

    else: #msm coisa de antes, sóq agora é antes de fixo
        delta = str(fixo - agora)
        atrasado_adiantado = "Adiantado"
            
    if len(delta) < 8: 
        delta = ("0" + delta).replace(":", "h")
        timming = f"Só {delta[0:5]} {atrasado_adiantado}"

    embed.set_footer(text= f"Chance: {chance:.2f}% || Days: {len(lista_tempo_exc)}/{lista_total}\nTimming: {timming}")
    await canal.send(f"{msg} {id_membro.mention}", embed=embed)


#atualiza os arquivos .json, seleciona um novo valor e seta os valores padrao

    lista_tempo_exc.append(tempo.strftime("%H:%M"))
    with open("OUTROS/tempo_exc.json", "w") as arq:
        json.dump(lista_tempo_exc, arq)

    lista_tempo.remove(tempo.strftime("%H:%M"))
    with open("OUTROS/tempo.json", "w") as arq:
        json.dump(lista_tempo, arq)

    estado_tempo["tempo"] = random.choice(lista_tempo)
    estado_tempo["ult_dia"] = agora.day

    msg = ""      
    if tempo.hour == 6 and tempo.minute == 30:
        embed.remove_field(index=0)