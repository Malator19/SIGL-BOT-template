import os

import discord as discord
from discord import Member
from discord.ext import commands
from discord.utils import get

from warmup import *

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 352589590307012611  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

#@bot.command()
#async def test(ctx, arg):
 #   await ctx.send(arg)

#--------------------------------------
#Warm-up
@bot.command()
async def name(ctx):
    print('-----------')
    print(ctx.message.author.mention)
    print('-----------')
    await ctx.send(ctx.message.author.mention)


@bot.command(aliases=["mc"])
async def count(ctx):
    print('-----------')
    a=ctx.guild.member_count
    b=discord.Embed(title=f"members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)


@bot.command()
async def count2(ctx):
    for guild in bot.guilds:
        print("guild : " + str(guild))
        print("guild.members " + str(guild.members))
        for member in guild.members:
            print(member)
            print("member.status : " + str(member.status))

#--------------------------------------
#Administration

@bot.command()
async def admin(ctx, user: discord.Member):
    client = discord.Client()
    perms = discord.Permissions(manage_guild=True, kick_members=True, ban_members= True)
    #admin_role = discord.utils.get(ctx.message.guild.roles, name = "admin")
    #detecter s'il a le role admin avant
    print("member.nick : "+ str(user.nick))
    admin = ctx.guild.create_role(name='admin', permissions=perms)
    this_role = get(ctx.guild.roles, id=int(admin.id))

#if not user.has_role(admin):
    print ("admin role : " + str(this_role))
    print ("user : " + str(user))
    await user.add_roles(this_role)

#--------------------------------------
#It's all fun and games


token = "ODkyODIzMTk0Nzk1Mzc2NjUw.YVSgZQ.COMVz_wTprXIJep2rxKjq3ZFJqk"
bot.run(token)  # Starts the bot