artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]

unique_artists = set()

def playlist(artist_names):
    if len(artist_names) == len(set(artist_names)):
        print(True)
    else:
        print(False)

    for artist in artist_names:
        unique_artists.add(artist)
    print(unique_artists)


playlist(artist_names)