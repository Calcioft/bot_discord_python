import config
import discord
from discord.ext import commands

bot_teste = True  # <----------------------- Alterar entre bot teste e bot normal
ligar = True

def run():
    intents = discord.Intents.default()
    discord.Intents()
    bot = commands.Bot(command_prefix="*", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("______________")
    @bot.command(
        aliases=['p'],
        help="Responde com pong e o ping atual do bot",
        brief="Responde com pong e o ping atual do bot",
        eneable=True,
        hidden=False
    )
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command()
    async def helpy(ctx):
        await ctx.send("ajuda")

    if ligar:
        bot.run(config.token)


if __name__ == "__main__":
    run()
