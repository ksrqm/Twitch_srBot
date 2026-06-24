from bot_files.logger import current_time


##########################################################################################
#FILE: bot_files/events_and_commands/bot_commands.py
def log_event_ready(streamer_channel):
    current_time.log_time(
        f"Bot is working: {streamer_channel}"
    )

def log_volume(is_a_rascal, volume, nick):
    if not is_a_rascal:
        current_time.log_time(
            f"{nick}: Volume set to: {volume}"
        )
    else:
        current_time.log_time(
            f"{nick}: Rascal tried to set volume to: {volume}"
        )


def log_pause(is_a_rascal, is_paused, nick):
    if not is_a_rascal:
        if is_paused:
            current_time.log_time(
                f"{nick}: Song paused"
            )
        else:
            current_time.log_time(
                f"{nick}: Song unpaused"
            )
    else:
        current_time.log_time(
            f"{nick}: Rascal tried to pause song"
        )


def log_skip(is_a_rascal, nick):
    if not is_a_rascal:
        current_time.log_time(
            f"{nick}: Skipped"
        )
    else:
        current_time.log_time(
            f"{nick}: Rascal tried to skip song"
    )


def log_song(title, user, link):
    current_time.log_time(
            f"Tried to add: {title} | "
            f"requested by {user} | "
            f"{link}"
    )

def log_queue(nick):
    current_time.log_time(
        f"{nick}: Asked for queue"
    )

def log_current(nick):
    current_time.log_time(
        f"{nick}: Asked for current"
    )
##########################################################################################
#FILE: bot_files/SR/player/player_local.py
def log_play_local(path_to_local_song):
    print("________________________________________________________________________________")
    current_time.log_time(
        f"Play local: {path_to_local_song}"

    )
##########################################################################################
#FILE: bot_files/SR/player/player_youtube.py
def log_play_youtube(link, title):
    print("________________________________________________________________________________")
    current_time.log_time(
        f"Play Youtube: {title} | {link}"
    )
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
def log_answer(answer):
    print(f"Answer: {answer}")