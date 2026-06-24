import os
from dotenv import load_dotenv
from twitchio.ext import commands

load_dotenv()

bot = commands.Bot(
    token=str(os.getenv("TWITCH_TOKEN")),
    prefix="!",
    initial_channels=[os.getenv("TWITCH_CHANNEL")],
)

channel = os.getenv("TWITCH_CHANNEL")
users_with_perms = str(os.getenv("USERS_WITH_PERMS")).split(",")
