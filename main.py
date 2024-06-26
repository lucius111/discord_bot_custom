import requests
import discord
from discord.ext import commands
from discord.ui import View, Item, TextInput, Button
from discord import Interaction
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from pydub import AudioSegment
from fate_dise import fate
from dise import dise, Salli_1, Shrek_1
from AI_picture import AI_print
import yt_dlp as youtube_dl
import os
import asyncio
import re
import csv
import random
from pathlib import Path
import eyed3
intents = discord.Intents.all()
config = {
    'token': '',
    'prefix': '!',
}

bot = commands.Bot(command_prefix=config['prefix'],intents=intents)

ffmpeg_options = {
    'options': '-vn',
    'executable': 'ffmpeg.exe'
} 


vose=''
ctxb=''
point=False
mp=''
@bot.command(help='Запуск музыки с Ютуба')
async def work(ctx,url):
    global vose, mp, point
    point=False
    if ctx.author.voice is None:
        await ctx.send("Хозяин, вы не находитесь в голосовом канале")
        return
    try:
        vc = await ctx.author.voice.channel.connect()
        vose=vc
        await ctx.send("https://tenor.com/view/12years-a-slave-drama-chiwetel-ejiofor-trailer-gif-3434019")
        
    except:
        vc=vose
        await ctx.send("Я уже играю, мне похуй")
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
            voice_client.stop()
    ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}, {'key': 'FFmpegMetadata', 'add_metadata': True, }],'outtmpl': 'music_all//music/%(id)s.%(ext)s'})
    metadata = {
    'title': 'Название трека',
    'artist': 'Исполнитель',}
    info = ydl.extract_info(url, download=False,extra_info={'metadata': metadata})
    description = (info['title'])
    mes = await ctx.send(f'Хозяин, я начинаю играть {description}')
    video_title = info['id']+'.mp3'
    print (f'Мой файл {video_title}')
    vose=vc
    done_music=''
    for file in os.listdir('./music_all/'):
        d = os.path.join('./music_all/', file)
        if os.path.isdir(d):
            for file in (sorted(Path(d).glob('*.mp3'))):
                print (file.name, video_title)
                if file.name == video_title:
                    done_music=(list(map(str, [file])))[0]
    if done_music !='':
        print(f'//////////////////////////////////////////////////////////////////////////')
        mp=done_music
        
    else: 
        ydl.process_info(info)
        mp3_file_path = ydl.prepare_filename(info)
        print(f"Файл {mp3_file_path} загружен и сохранен как MP3.")
        mp=mp3_file_path
        asyncio.sleep(3)
    vc.play(discord.FFmpegPCMAudio(mp))    
    point=True
    sch = 1
    while point==True:
        if not vc.is_playing():
            voice_client.stop()
            sch += 1
            await mes.edit(content=f'Хозяин, я продолжаю играть {description} уже {sch} раз')
            vc.play(discord.FFmpegPCMAudio(mp))
        await asyncio.sleep(3)

@bot.command(help='Охренеть насколько случайный трек')
async def work_random(ctx):
    global point, point
    point=False
    paths=[]
    for file in os.listdir('./'):
        d = os.path.join('./', file)
        if os.path.isdir(d):
            paths=paths+(sorted(Path(d).glob('*.mp3')))
    global vose, mp
    if ctx.author.voice is None:
        await ctx.send("Хозяин, вы не находитесь в голосовом канале")
        return
    try:
        vc = await ctx.author.voice.channel.connect()
        vose=vc
        await ctx.send("https://tenor.com/view/12years-a-slave-drama-chiwetel-ejiofor-trailer-gif-3434019")
    except:
        vc=vose
        await ctx.send("Я уже играю, мне похуй")
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
            voice_client.stop()
    vose=vc
    rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
    audio_file = eyed3.load(rand_mus)
    await ctx.send(f'Хозяин, я играю {audio_file.tag.title}')
    vc.play(discord.FFmpegPCMAudio(rand_mus))
    point=True
    while point==True:
        if not vc.is_playing():
            rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
            audio_file = eyed3.load(rand_mus)
            await ctx.send(f'Хозяин, я играю {audio_file.tag.title}')
            vc.play(discord.FFmpegPCMAudio(rand_mus))
        await asyncio.sleep(1)
    
@bot.command(help='Случайный phonk')
async def work_random_phonk(ctx):
    paths = sorted(Path('./phonk').glob('*.mp3'))
    global vose, mp, point
    if ctx.author.voice is None:
        await ctx.send("Хозяин, вы не находитесь в голосовом канале")
        return
    try:
        vc = await ctx.author.voice.channel.connect()
        vose=vc
        await ctx.send("https://tenor.com/view/12years-a-slave-drama-chiwetel-ejiofor-trailer-gif-3434019")
    except:
        vc=vose
        await ctx.send("Я уже играю, мне похуй")
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
            voice_client.stop()
    vose=vc
    rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
    audio_file = eyed3.load(rand_mus)
    await ctx.send(f'Хозяин, я играю {audio_file.tag.title}')
    vc.play(discord.FFmpegPCMAudio(rand_mus))
    while point==True:
        if not vc.is_playing():
            rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
            audio_file = eyed3.load(rand_mus)
            await ctx.send(f'Хозяин, я играю {audio_file.tag.title}')
            vc.play(discord.FFmpegPCMAudio(rand_mus))
        await asyncio.sleep(1)

@bot.command(help='Случайный Первый KLA$')
async def work_random_KLAS(ctx):
    paths = sorted(Path('./KLA$').glob('*.mp3'))
    global vose, mp
    if ctx.author.voice is None:
        await ctx.send("Хозяин, вы не находитесь в голосовом канале")
        return
    try:
        vc = await ctx.author.voice.channel.connect()
        vose=vc
        await ctx.send("https://tenor.com/view/12years-a-slave-drama-chiwetel-ejiofor-trailer-gif-3434019")
    except:
        vc=vose
        await ctx.send("Я уже играю, мне похуй")
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
            voice_client.stop()
    vose=vc
    rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
    audio_file = eyed3.load(rand_mus)
    await ctx.send(f'Хозяин, я играю {audio_file.tag.title}')
    vc.play(discord.FFmpegPCMAudio(rand_mus))
    while point==True:
        if not vc.is_playing():
            rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
            audio_file = eyed3.load(rand_mus)
            await ctx.send(f'Хозяин, я играю {audio_file.tag.title}')           
            vc.play(discord.FFmpegPCMAudio(rand_mus))
        await asyncio.sleep(1)

@bot.command(help='Случайная классика')
async def work_random_classic(ctx):
    paths = sorted(Path('./classic').glob('*.mp3'))
    global vose, mp, point
    if ctx.author.voice is None:
        await ctx.send("Хозяин, вы не находитесь в голосовом канале")
        return
    try:
        vc = await ctx.author.voice.channel.connect()
        vose=vc
        await ctx.send("https://tenor.com/view/12years-a-slave-drama-chiwetel-ejiofor-trailer-gif-3434019")
    except:
        vc=vose
        await ctx.send("Я уже играю, мне похуй")
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
            voice_client.stop()
    vose=vc
    rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
    audio_file = eyed3.load(rand_mus)
    await ctx.send(f'Хозяин, я играю {audio_file.tag.title}') 
    vc.play(discord.FFmpegPCMAudio(rand_mus))
    while point==True:
        if not vc.is_playing():
            rand_mus= list(map(str, paths))[random.randrange(len(list(map(str, paths))))]
            audio_file = eyed3.load(rand_mus)
            await ctx.send(f'Хозяин, я играю {audio_file.tag.title}') 
            vc.play(discord.FFmpegPCMAudio(rand_mus))
        await asyncio.sleep(1) 
class MyView(View):
    async def on_timeout(self):
        self.stop()



class MyButton(Button):
    async def callback(self, interaction: discord.Interaction):
        global vose,ctxb, point
        point= True
        done_music=''        
        for file in os.listdir('./'):
            d = os.path.join('./', file)
            if os.path.isdir(d):
                for file in (sorted(Path(d).glob('*.mp3'))):
                    print (file.name, self.custom_id)
                    if file.name == self.custom_id:
                        done_music=(list(map(str, [file])))[0]
        print (done_music)
        audio_file = eyed3.load(done_music)
        if audio_file.tag.title !='Tick Tock':
            await interaction.response.send_message("https://tenor.com/view/12years-a-slave-drama-chiwetel-ejiofor-trailer-gif-3434019")
            await interaction.message.delete()
        else:
            await interaction.response.send_message("https://tenor.com/view/tf2-engineer-gif-26567122")
            await interaction.message.delete()


        if done_music !='':
            print('//////////////////////////////////////////////////////////////////////////')
        mp=done_music
        vose.play(discord.FFmpegPCMAudio(mp))
        while point==True:
            if not vose.is_playing():
                await ctxb.send(f'Хозяин, я продолжаю играть {audio_file.tag.title}')
                vose.play(discord.FFmpegPCMAudio(mp))
            await asyncio.sleep(3)

@bot.command()
async def buttons(ctx):
    global vose, ctxb, point
    view = MyView(timeout=10000)
    point= False
    try:
        vc = await ctx.author.voice.channel.connect()
        vose=vc
    except:
        print('.!.')
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
            voice_client.stop()
    ctxb=ctx
    title_music=[]
    for file in os.listdir('./'):
        d = os.path.join('./', file)
        if os.path.isdir(d):
            flag=0
            for file in (sorted(Path(d).glob('*.mp3'))):
                audio_file = eyed3.load(file)
                print (file.name,audio_file.tag.title)
                title_music.append([file.name,audio_file.tag.title])
                view.add_item(MyButton(label=audio_file.tag.title[:80], custom_id=file.name))
                print(view)
                if flag>=10:
                    await ctx.send('Выберите музыку вашего вечера:', view=view)
                    flag=0
                    view = MyView(timeout=10000)
                flag+=1
                print('1')
    await ctx.send('Выберите музыку вашего вечера:', view=view)    


@bot.command(help='Прекратить воспроизводить')
async def done(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()

@bot.command()
async def fate_dise(ctx,*args: int):
    emoji_person_minu = discord.utils.get(ctx.guild.emojis, name="person_minu")
    emoji_person_zero = discord.utils.get(ctx.guild.emojis, name="person_zero")
    emoji_person_plus = discord.utils.get(ctx.guild.emojis, name="person_plus")
    resu = fate(emoji_person_minu, emoji_person_zero, emoji_person_plus)
    await ctx.send(resu[0])
    await ctx.send(f'Выпало: {resu[1]}')
    if args != tuple():
        await ctx.send(f'С модификатором: {resu[1] + sum(args)}')

@bot.command()
async def roll(ctx,col: int, td: int,*args: int):
    res = dise(col, td)
    with open('combined_image.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    await ctx.send(f'Выпало: {res}')
    if args != tuple():
        await ctx.send(f'С модификатором: {res + sum(args)}')

@bot.command()
async def Salli(ctx,type, col: int):
    Salli_1(type, col)
    with open('combined_image.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def shrek(ctx,type, col: int):
    Shrek_1(type, col)
    with open('combined_image.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


@bot.command()
async def print(ctx, *args : str):
    promt= ' '.join(args)
    file_do = await AI_print(promt)
    with open(file_do, 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def edit(ctx, *args : str):
    mes = await ctx.send(f'Пще, я поляк')
    for i in range(10):
        await asyncio.sleep(5)
        await mes.edit(content=f'Иди траву трогай {i}')


















bot.run(config['token'])

