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

@tree.command(name = "food", description = "Food", guild=discord.Object(id=guildID))
#@tree.command(name = "food", description = "Food")
async def GetFox(interaction):
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    r = requests.get(url)
    data = r.json()['meals'][0]['strMealThumb']
    name = r.json()['meals'][0]['strMeal']
    idmeal = r.json()['meals'][0]['idMeal']
    link = "https://www.themealdb.com/meal/" + str(idmeal)
    print(f"Food for {interaction.user} {data}")
    #em = discord.Embed(title=f"<a:tastychamp:858816186032062494>")
    em = discord.Embed(title=f"<a:tastychamp:858816186032062494> {name}", url=link, colour=discord.Colour.yellow())
    em.set_image(url=data)
    await interaction.response.send_message(embed=em)

client.run(token)

