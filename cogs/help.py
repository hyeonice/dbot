import discord
from discord.ext import commands
import time


class help(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def 도움말(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="도움말", description="반갑습니다. 나성수입니다.")
        embed.add_field(name='**명령어**', value='**`왜살아?`, `아바타`**')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(help(client))