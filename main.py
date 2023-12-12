import config
import discord
from discord.ext import commands

bot_teste = True  # <----------------------- Alterar entre bot teste e bot normal


def run():
    intents = discord.Intents.default()

    discord.Intents.all()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("______________")
    @bot.command()
    async def ping(ctx):
        await ctx.send("pong")

    bot.run(config.token)


if __name__ == "__main__":
    run()
