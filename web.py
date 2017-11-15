import os
import json

from flask import Flask, render_template

import mb_settings
from mpd_wrapper import MPDWrapper

app = Flask(__name__)
client = MPDWrapper()

@app.route("/artist_list")
def get_artists():
    result = os.listdir(mb_settings.config.get('DEFAULT', 'library_path'))
    return json.dumps(result)

@app.route("/status")
def get_status():
    status = client.get_status()
    return render_template('status.html',
            status=status,
            status_dump=json.dumps(status),
            current_song=client.get_playlist_song_by_id(status['songid'])[0])

if __name__ == "__main__":
    app.run()
