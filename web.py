import os
import json

from flask import Flask, render_template, request, jsonify

import mb_settings
from mpd_wrapper import MPDWrapper

app = Flask(__name__)
client = MPDWrapper()

success_status = 'success'
failure_status = 'failure'

status_name = 'status'
message_name = 'message'
vol_name = 'vol'

@app.route("/artist_list", methods=['GET'])
def get_artists():
    result = os.listdir(mb_settings.config.get('DEFAULT', 'library_path'))
    return json.dumps(result)

@app.route("/status", methods=['GET'])
def get_status():
    with client as active_client:
        status = active_client.get_status()
        current_song = active_client.get_playlist_song_by_id(status['songid'])[0]
    return render_template('status.html',
            status=status,
            status_dump=json.dumps(status),
            current_song=current_song)

@app.route("/api/set_vol", methods=['POST'])
def set_volume():
    if vol_name in request.form:
        try:
            with client as active_client:
                active_client.set_volume(int(request.form[vol_name]))
            return jsonify({status_name: success_status}), 200
        except ValueError:
            return jsonify({status_name: failure_status, message_name: vol_name + " was not an integer"}), 400
        
    else:
        return jsonify({status_name: failure_status, message_name: vol_name + " value missing"}), 400

if __name__ == "__main__":
    app.run()
