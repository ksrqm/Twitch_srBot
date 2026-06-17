import asyncio
from playwright.async_api import async_playwright
import q

playwright = None
browser = None
page = None
ctx = None
skip_song = False

async def setup():
    global playwright, browser, page

    playwright = await async_playwright().start()

    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir="./brave_bot_profile",
        executable_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        headless=False
    )

    page = await browser.new_page()
    await page.goto("https://www.youtube.com")

async def play(song, ctx):
    global page, skip_song
    skip_song = False
    await page.goto(song["link"])
    await page.wait_for_selector("video")
    is_paused = await page.locator("video").evaluate("(video) => video.paused")
    if is_paused:
        await page.locator(".ytp-play-button").click()

    await ctx.send(f"Now playing: {song['title']}")
    for _ in range(song["duration"]):
        if skip_song:
            break
        await asyncio.sleep(1)


async def player_loop():
    global ctx
    while True:
        song = q.get_next_song()
        if song:
            await play(song, ctx)
        else:
            await asyncio.sleep(5)

def skip():
    global skip_song
    skip_song = True