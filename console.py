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

artist_repository.save(artist3)
album_repository.save(album3)


pdb.set_trace()