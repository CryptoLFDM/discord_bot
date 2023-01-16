import discord
from discord import app_commands

from config import load_config

cfg = load_config()
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        await tree.sync(guild=discord.Object(id=guild.id))
        print("Ready!")


@tree.command(name="exchange", description="Display All Exchange Url", guild=discord.Object(id=cfg["guild"]))
async def code_examples(interaction):
    embed = discord.Embed(
    )
    embed.add_field(name="Binance", value=cfg["binance_url"], inline=False)
    embed.add_field(name="Kucoin", value=cfg["kucoin_url"], inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(name="binance", description="Display Binance Exchange Url", guild=discord.Object(id=cfg["guild"]))
async def binance(interaction):
    embed = discord.Embed(
        color=discord.Color.yellow(),
    )
    embed.set_author(name="Binance", url=cfg["binance_url"], icon_url="https://upload.wikimedia.org/wikipedia/commons/5/57/Binance_Logo.png")
    await interaction.response.send_message(embed=embed)


@tree.command(name="kucoin", description="Display Kucoin Exchange Url", guild=discord.Object(id=cfg["guild"]))
async def kucoin(interaction):
    embed = discord.Embed(
        color=discord.Color.green(),
    )
    embed.set_author(name="Kucoin", url=cfg["kucoin_url"], icon_url="https://assets.staticimg.com/public-web/2.6.3/static/logo.3766af92.svg")
    await interaction.response.send_message(embed=embed)

client.run(cfg["token"])
