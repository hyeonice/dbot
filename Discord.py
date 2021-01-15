import discord
from discord.ext import commands
import os

count = 0

app = commands.Bot(command_prefix='성수야 ')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        app.load_extension(f'cogs.{filename[:-3]}')

def count1():
    global count
    count += 1 

def count2():
    global count
    count = 0 

@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="성수야 도움말"))

@app.command(aliases=['왜살아?', '왜사냐고', '왜살아', '왜삶?', '왜삼?', '왜삼'])
async def hello(ctx):
    if count <= 2:
        await ctx.send('죄송합니다.')
        count1()
    else:
        await ctx.send(ctx.author.name +'님 자꾸 선넘으시네요. 마피아 계정 영구정지 드렸으니까 재접속 해보세요.')
        count2()

@app.command(name='서영이왜산대?')
async def seoyoung(ctx):
    await ctx.send("빈아 넌 왜사는데?")
    

app.run('Nzk5Mjg0MTI3MDgwNjQ0Njg5.YABVWQ.Zf2t6Jo4IigVPJm45mqamvtIVgg')