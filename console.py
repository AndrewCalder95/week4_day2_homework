import pdb 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist1 = Artist("Arctic Monkeys")
artist2 = Artist("The Beatles")
artist3 = Artist("Tame Implala")

album1 = Album("Tranquility Base Hotel and Casino", "Rock", artist1)
album2 = Album("Abbey Road", "Rock", artist2)
album3 = Album("Currents", "Rock", artist3)
album4 = Album("The Slow Rush", "Rock", artist3)

artist_repository.save(artist3)
album_repository.save(album3)
album_repository.save(album4)

album_repository.delete_all()
artist_repository.delete_all()

artist_repository.select(5)
album_repository.select(6)

album_list_from_artist = artist_repository.select_all(artist3)
for album in album_list_from_artist:
    print(album.__dict__)

pdb.set_trace()