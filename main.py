import config
import discord
from discord.ext import commands

bot_teste = False  # <----------------------- Alterar entre bot teste e bot normal


def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="*", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("______________")

    bot.run(config.token)


if __name__ == "__main__":
    run()
