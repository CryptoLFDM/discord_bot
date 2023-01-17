# # #
# # # @client.tree.command()
# # # @app_commands.describe(
# # #     coin_name='The first value you want to add something to',
# # # )
# # # async def coin(interaction: discord.Interaction, coin_name: str):
# # #     resp = requests.get(cfg["atom_coin_url"])
# # #     body = resp.json()
# # #     embed = discord.Embed(
# # #         color=discord.Color.purple(),
# # #     )
# # #     logging.info(body)
# # #     embed.set_author(name=coin_name, url=cfg["atom_geko_url"], icon_url=body["image"]["thumb"])
# # #     embed.add_field(name="market_cap_rank", value="{}".format(body["market_cap_rank"]), inline=True)
# # #     embed.add_field(name="current_price",
# # #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["current_price"]["usd"]),
# # #                                                humanize.intcomma(body["market_data"]["current_price"]["eur"])), inline=True)
# # #     embed.add_field(name="ath",
# # #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["ath"]["usd"]),
# # #                                                humanize.intcomma(body["market_data"]["ath"]["eur"])), inline=True)
# # #     embed.add_field(name="market_cap",
# # #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["market_cap"]["usd"]),
# # #                                                humanize.intcomma(body["market_data"]["market_cap"]["eur"])), inline=True)
# # #     embed.add_field(name="total_volume",
# # #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["total_volume"]["usd"]),
# # #                                                humanize.intcomma(body["market_data"]["total_volume"]["eur"])), inline=True)
# # #
# # #     await interaction.response.send_message(embed=embed,)
# #
# #
# # @client.tree.command(name="atom", description="Display Atom Info")
# # async def atom(interaction):
# #     resp = requests.get(cfg["atom_coin_url"])
# #     body = resp.json()
# #     embed = discord.Embed(
# #         color=discord.Color.purple(),
# #     )
# #     logging.info(body)
# #     embed.set_author(name="Atom", url=cfg["atom_geko_url"], icon_url=body["image"]["thumb"])
# #     embed.add_field(name="market_cap_rank", value="{}".format(body["market_cap_rank"]), inline=True)
# #     embed.add_field(name="current_price",
# #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["current_price"]["usd"]),
# #                                                humanize.intcomma(body["market_data"]["current_price"]["eur"])), inline=True)
# #     embed.add_field(name="ath",
# #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["ath"]["usd"]),
# #                                                humanize.intcomma(body["market_data"]["ath"]["eur"])), inline=True)
# #     embed.add_field(name="market_cap",
# #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["market_cap"]["usd"]),
# #                                                humanize.intcomma(body["market_data"]["market_cap"]["eur"])), inline=True)
# #     embed.add_field(name="total_volume",
# #                     value="{} $ | {} €".format(humanize.intcomma(body["market_data"]["total_volume"]["usd"]),
# #                                                humanize.intcomma(body["market_data"]["total_volume"]["eur"])), inline=True)
# #
# #     await interaction.response.send_message(embed=embed,)
#
# @client.tree.command(name="binance", description="Display Binance Exchange Url")
# async def binance(interaction):
#     file = discord.File("assets/binance.png", filename="image.png")
#     embed = discord.Embed(
#         color=discord.Color.yellow(),
#     )
#     embed.set_author(name="Binance", url=cfg["binance_url"], icon_url="attachment://image.png")
#     await interaction.response.send_message(embed=embed, file=file,)
#
#
# @client.tree.command(name="kucoin", description="Display Kucoin Exchange Url")
# async def kucoin(interaction):
#     file = discord.File("assets/kucoin.png", filename="image.png")
#     embed = discord.Embed(
#         color=discord.Color.green(),
#     )
#     embed.set_author(name="Kucoin", url=cfg["kucoin_url"], icon_url="attachment://image.png")
#     await interaction.response.send_message(embed=embed, file=file,)
