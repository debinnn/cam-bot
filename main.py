import discord
import os
import random

client = discord.Client()


@client.event
async def on_ready():
    print('Bot has been activated as {0.user}'.format(client))
    
    await client.change_presence(status=discord.Status.online, activity = discord.Game('s!help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_message(message):
    if message.content.startswith('s!help'):
        embedVar = discord.Embed(title="cam's basement", description="a guide to help u traverse through cam's dimly lit basement", color=0x00ff00)
        embedVar.add_field(name="・roles", value="roles are self assignable and can be found in #roles.", inline=False)
        embedVar.add_field(name="・minecraft server", value="ip address of the server: CamsHell.minehut.gg | version: 1.18", inline=False)
        await message.channel.send(embed=embedVar)
        


client.run(os.environ['token'])
