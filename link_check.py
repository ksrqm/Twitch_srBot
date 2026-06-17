import yt_dlp

async def handle_song(ctx):
    id = ctx.message.content.split(" ")[1]

    print(f"Sprawdzam ID: {id}")

    if len(id) == 11:
        link = "https://www.youtube.com/watch?v=" + id

        print(f"Sprawdzam link: {link}")

        try:
            with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
                info = ydl.extract_info(link, download=False)

            print("Link poprawny!")
            print(f"Tytuł: {info.get('title')}")

            return True

        except Exception as e:
            print("Link niepoprawny!")
            print(f"Błąd: {e}")

            return False

    else:
        print("ID ma złą długość")
        return False