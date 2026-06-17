import asyncio
from playwright.async_api import async_playwright
import q

playwright = None
browser = None
page = None

async def setup():
    global playwright, browser, page

    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir="./chrome_bot_profile",
        headless=False
    )
    page = await browser.new_page()
    await page.goto("https://www.youtube.com")

async def play(song, ctx):
    global page
    await page.goto(song["link"])
    await page.locator(".ytp-play-button").click()
    await ctx.send("Now playing: {song['title']}")
    await asyncio.sleep(song["duration"])

async def player_loop():
    while True:
        song = q.get_next_song()
        if song:
            await play(song["link"])
        else:
            await asyncio.sleep(5)