from mpd import MPDClient

def refresh_client(func):
    def wrapper(*args):
        args[0]._new_client()
        result = func(*args)
        args[0]._close_client()
        return result
    return wrapper

class MPDWrapper:

    def __init__(self, address = "localhost", port = 6600):
        self.address = address
        self.port = port
        self.client = None
    
    def _new_client(self):
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.connect(self.address, self.port)

    def _close_client(self):
        self.client.close()
        self.client.disconnect()

    @refresh_client
    def get_status(self):
        return self.client.status()
    
    @refresh_client
    def get_playlist_song_by_id(self, song_id):
        return self.client.playlistid(song_id)
