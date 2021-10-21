import discord
import twiter_bot as tw
from discord import client
from discord import guild
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option,create_permission
from discord_slash.model import SlashCommandPermissionType
from api_keys import dis_token

token = dis_token
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

slash = SlashCommand(client, sync_commands=True)
guild_ids = [753673556096974907]
class main():

    @client.event
    async def on_ready():
        print("Gestartet")

    @slash.slash(name="Tweet", guild_ids=guild_ids, description="sende einen tweet auf den @Watch_Point_Bot", options=[create_option(name="tweet", description="Was für einen tweet willst du senden",option_type=3,required=True)])
    async def tweet_senden(ctx, tweet):
        print(f"user: {str(ctx.author)} will denn tweet: {tweet} senden!")
        tw.send_tweet(f"{tweet} von {ctx.author} über Watch-bot")
        await ctx.send(f"Der tweet '{tweet}' wird gesendet ")

Main = main()

if __name__ == "__main__":
    client.run(token)