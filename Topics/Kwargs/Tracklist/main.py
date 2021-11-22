def tracklist(**songs):
    for artist in songs:
        print(artist)
        for album in songs[artist]:
            print(f'ALBUM: {album} TRACK: {songs[artist][album]}')