from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


     
def save(album):
    sql = f"INSERT INTO albums (name, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id 
    return album