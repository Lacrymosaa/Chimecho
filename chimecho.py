import os
import sys
import time
import json
import psutil
import pystray
import spotipy
import threading
from PIL import Image
from plyer import notification
from pystray import MenuItem as item
from spotipy.oauth2 import SpotifyOAuth

class Chimecho:
    def __init__(self):
        self.running = True
        self.name = "Chimecho"
        self.app_icon = os.path.join(sys.path[0], "Chimecho.ico")

    def check_user_activity(self):
        scope = "user-read-currently-playing"

        credentials_path = os.path.join(sys.path[0], "credentials.json")
        with open(credentials_path, "r") as file:
            credentials = json.load(file)

        client_id = credentials["client_id"]
        client_secret = credentials["client_secret"]

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost:8888/callback', scope=scope))

        while self.running:
            if self.is_spotify_running():
                current_track = sp.current_user_playing_track()

                if current_track is not None and current_track["is_playing"]:
                    pass
                else:
                    self.show_notification("Você não está ouvindo música no Spotify")

            time.sleep(500)

    def is_spotify_running(self):
        spotify_processes = [proc for proc in psutil.process_iter(['pid', 'name']) if 'Spotify' in proc.info['name']]
        return len(spotify_processes) > 0

    
    def show_notification(self, message):
        notification.notify(
            title=self.name,
            message=message,
            timeout=5,
            app_icon=self.app_icon
        )

    def start(self):
        threading.Thread(target=self.check_user_activity).start()

    def stop(self):
        self.running = False

def show_menu(icon, item):
    if item.text == 'Encerrar':
        prog.stop()
        icon.stop()

def main():
    global prog
    prog = Chimecho()
    prog.start()

    image = Image.open("Chimecho.ico")

    menu = (
        item('Encerrar', show_menu),
    )

    menu_icon = pystray.Icon(prog.name, image, prog.name, menu)
    menu_icon.run()

if __name__ == '__main__':
    main()