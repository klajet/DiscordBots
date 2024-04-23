import discord
import os
from discord import app_commands
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv('TOKEN')
guildID = os.getenv('GUILDID')

intents = discord.Intents.default()
intents.message_content = True

bot = discord.User.bot
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guildID))
    print(f'We have logged in as {client.user}')

@tree.command(name = "fox", description = "Fox", guild=discord.Object(id=guildID))
async def GetFox(interaction):
    url = "https://randomfox.ca/floof/"
    r = requests.get(url)
    data = r.json()['image']
    print(f"Fox for {interaction.user} {data}")
    em = discord.Embed(title="<:Fox:1074773502613270569> Fox", colour=discord.Colour.orange())
    em.set_image(url=data)
    await interaction.response.send_message(embed=em)

client.run(token)

