from mpd import MPDClient

class MPDWrapper:

    def __init__(self, address = "localhost", port = 6600):
        self.address = address
        self.port = port
        self.client = None
    
    def __enter__(self):
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.connect(self.address, self.port)
        return self

    def __exit__(self, type, value, traceback):
        self.client.close()
        self.client.disconnect()

    def get_status(self):
        return self.client.status()
    
    def get_playlist_song_by_id(self, song_id):
        return self.client.playlistid(song_id)

    def set_volume(self, vol):
        self.client.setvol(vol)
        
    def set_repeat(self, new_state):
        self.client.repeat(new_state)

    def set_random(self, new_state):
        self.client.repeat(new_state)

    def next_song(self):
        self.client.next()

    def prev_song(self):
        self.client.previous()

    def play(self):
        self.client.play()

    def pause(self):
        self.client.pause()

    def stop(self):
        self.client.stop()

