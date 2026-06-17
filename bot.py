import os
from dotenv import load_dotenv
from twitchio.ext import commands

# Ładowanie danych z pliku .env
load_dotenv()

# Inicjalizacja bota z podstawowymi ustawieniami
bot = commands.Bot(
    token=os.getenv("TWITCH_TOKEN"),
    prefix="!",
    initial_channels=[os.getenv("TWITCH_CHANNEL")]
)

# Komunikat w konsoli, gdy bot pomyślnie połączy się z Twitchem
@bot.event()
async def event_ready():
    print(f"Bot działa! Czytam czat na kanale: {os.getenv('TWITCH_CHANNEL')}")

# Wyłapywanie każdej wiadomości na czacie
@bot.event()
async def event_message(ctx):
    print(f"[{ctx.author.name}]: {ctx.content}")

# Uruchomienie bota
if __name__ == "__main__":
    bot.run()