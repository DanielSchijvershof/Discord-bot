import discord
from discord.ext import commands
import os

token = "MTM0NjU1MTMzNzE0NzY5NTIzNg.GPbujK.WcEh2xjWPepiZfcmKdbO16aOUOanypzNWSOyyo"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv(token))
