from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# creat a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "artist"
    ArtistId = Column("artist_id", Integer, primary_key=True)
    Name = Column("name", String)

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "album"
    AlbumId = Column("album_id", Integer, primary_key=True)
    Title = Column("title", String)
    ArtistId = Column("artist_id", Integer, ForeignKey("artist.artist_id"))

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "track"
    TrackId = Column("track_id", Integer, primary_key=True)
    Name = Column("name", String)
    AlbumId = Column("album_id", Integer, ForeignKey("album.album_id"))
    MediaTypeId = Column("media_type_id", Integer)
    GenreId = Column("genre_id", Integer)
    Composer = Column("composer", String)
    Milliseconds = Column("milliseconds", Integer)
    Bytes = Column("bytes", Integer)
    UnitPrice = Column("unit_price", Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subcalss defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=50).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" of 50 from the "Album" table
# albums = session.query(Album).filter_by(ArtistId=50)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select only the tracks with "AlbumId" of 50 from the "Track" table
tracks = session.query(Track).filter_by(Composer="Metallica")
for track in tracks:
    print(track.TrackId, 
          track.Name,
          track.AlbumId,
          track.MediaTypeId,
          track.GenreId,
          track.Composer,
          track.Milliseconds,
          track.Bytes,
          track.UnitPrice,
          sep=" | ")