import os
import json

from flask import Flask

import mb_settings

app = Flask(__name__)

@app.route("/artist_list")
def get_artists():
    result = os.listdir(mb_settings.config.get('DEFAULT', 'library_path'))
    return json.dumps(result)

if __name__ == "__main__":
    app.run()
