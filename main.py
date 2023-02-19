import logging
import discord
from discord import app_commands
import requests
import humanize

from config import load_config
from coin import Coin, MapperSite, MapperApi

humanize.i18n.activate("fr_FR")
cfg = load_config()
MY_GUILD = discord.Object(cfg["guild"])


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        print("{} is connected to the following guild:", client.user)
        print("{} ( id: {} )".format(guild.name, guild.id))


@client.tree.command(name="exchange", description="Affiche les urls des exchanges")
async def exchange(interaction):
    embed = discord.Embed(
    )
    embed.add_field(name="", value="<:binance:1064661268834824233> [Binance]({})".format(cfg["binance_url"]), inline=True)
    embed.add_field(name="", value="<:kucoin:1064661290678759424> [Kucoin]({})".format(cfg["kucoin_url"]), inline=True)
    embed.add_field(name="", value="<:coinbase:1064704376763064330> [Coinbase]({})".format(cfg["coinbase_url"]), inline=True)
    embed.add_field(name="", value="<:kraken:1064704380986740826> [Kraken]({})".format(cfg["kraken_url"]), inline=True)
    embed.add_field(name="", value="<:okex:1064705226935914547> [Okex]({})".format(cfg["okex_url"]), inline=True)
    embed.add_field(name="", value="<:gate_io:1064704684796940348> [Gate.io]({})".format(cfg["gate_io_url"]), inline=True)

    await interaction.response.send_message(embed=embed)


@client.tree.command(name="help", description="Affiche l'aide")
async def exchange(interaction):
    embed = discord.Embed(
    )
    file = discord.File("assets/lfdm.png", filename="image.png")

    embed.set_author(name="Salut c'est le bot LFDM, pour vous servir", icon_url="attachment://image.png")
#    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="/exchange", value="Affiche les urls officiels des exchanges", inline=False)
    embed.add_field(name="/coin denom", value="Affiche des infos sur le token choisis", inline=False)
    embed.add_field(name="Tu veux contribuer  ?", value="[Click ici]({})".format(cfg["pr_url"]), inline=False)
    embed.add_field(name="Tu as une demande ou trouvé un bug ?", value="[Click ici]({})".format(cfg["bug_url"]), inline=False)
    embed.set_footer(text="A+")

    await interaction.response.send_message(embed=embed, file=file)


@client.tree.command(name="coin", description="Affiches les info financieres du token")
@app_commands.describe(denom='Collecte les info de ce token')
async def coin(interaction: discord.Interaction, denom: Coin):
    url = "{}/{}".format(cfg["gecko_api_url"],  MapperApi[denom.name])
    resp = requests.get(url)
    body = resp.json()
    embed = discord.Embed(
        color=discord.Color.purple(),
    )
    url = "{}/{}".format(cfg["gecko_front_url"], MapperSite[denom.name])
    logging.info(body)
    embed.set_author(name=denom.name, url=url, icon_url=body["image"]["thumb"])
    embed.add_field(name="market_cap_rank", value="{}".format(body["market_cap_rank"]), inline=True)
    embed.add_field(name="current_price",
                    value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["current_price"]["usd"]),
                                               humanize.intcomma(body["market_data"]["current_price"]["eur"])), inline=True)
    embed.add_field(name="ath",
                    value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["ath"]["usd"]),
                                               humanize.intcomma(body["market_data"]["ath"]["eur"])), inline=True)
    embed.add_field(name="market_cap",
                    value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["market_cap"]["usd"]),
                                               humanize.intcomma(body["market_data"]["market_cap"]["eur"])), inline=True)
    embed.add_field(name="total_volume",
                    value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["total_volume"]["usd"]),
                                               humanize.intcomma(body["market_data"]["total_volume"]["eur"])), inline=True)

    await interaction.response.send_message(embed=embed,)


@client.tree.command(name="faucet", description="Affiche les urls des faucets")
async def faucet(interaction):
    embed = discord.Embed(
    )
    embed.add_field(name="", value="<:bnb:1076971042062467163> [BNB]({})".format(cfg["bnb_faucet_url"]), inline=True)
    embed.add_field(name="", value="<:cardano:1076971009908936824>  [ADA]({})".format(cfg["ada_faucet_url"]), inline=True)
    embed.add_field(name="", value="<:avax:1076971070696988675> [AVA]({})".format(cfg["ava_faucet_url"]), inline=True)
    embed.add_field(name="", value="<:eth:1076971027063644231> [ETH]({})".format(cfg["eth_faucet_url"]), inline=True)
    embed.add_field(name="", value="<:matic:1076971057468145664> [MATIC]({})".format(cfg["matic_faucet_url"]), inline=True)
    embed.add_field(name="", value="<:lfdmcoin:1073999398821961829> [Multi-coin]({})".format(cfg["multi_coin_faucet_url"]), inline=True)

    await interaction.response.send_message(embed=embed)



client.run(cfg["token"])
