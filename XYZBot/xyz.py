import discord
import json
import tracemalloc
import discord_slash as interactions
import typing
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("xyz!", "xyz ", "?"), intents=discord.Intents.all())
slash = interactions.SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)
bot.remove_command("help")

with open("./token.json") as tokenfile:
    token = json.load(tokenfile)
with open("./XYZ/XYZBot/misc/assets/embed.json") as embedfile:
    embed = json.load(embedfile)

tracemalloc.start()

@bot.event
async def on_ready():
    channel: discord.TextChannel = bot.get_channel(858733322866786325)
    await channel.send(f"XYZ is ready and running on discord.py v{discord.__version__}!")

@bot.event
async def on_command_error(ctx: commands.Context, error):
    e = discord.Embed(title="An Error Occurred", color=int(embed["color"], 16), description=f"{error}")
    e.set_author(name=embed["author"], icon_url=embed["icon"])
    e.set_footer(text=embed["footer"], icon_url=embed["icon"])
    await ctx.send(embed=e)

    raise error

@bot.event
async def on_slash_command_error(ctx: typing.Union[interactions.SlashContext, interactions.MenuContext], ex):
    e = discord.Embed(title="An Error Occurred", color=int(embed["color"], 16), description=f"{ex}")
    e.set_author(name=embed["author"], icon_url=embed["icon"])
    e.set_footer(text=embed["footer"], icon_url=embed["icon"])
    await ctx.send(embed=e)

    raise ex

extensions = ["cogs.core", "cogs.help", "cogs.moderation", "cogs.utility", "jishaku"]
for extension in extensions:
    bot.load_extension(extension)

bot.run(token["xyz"])