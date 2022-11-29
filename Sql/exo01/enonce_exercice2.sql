USE Chinook;

-- Exercise 1
-- QUERY 1: Explore PlaylistTrack (line count : 8715)

-- QUERY 2: How many track does each playlist have? Order from largest to smallest playlists. (line count : 14)

SELECT PlaylistId, count(TrackId)
FROM playlist_track
GROUP BY PlaylistId

-- QUERY 3: Is there a difference between the unit price contained in invoice_items and tracks ?
SELECT playlist_track.TrackId, invoice_items.UnitPrice
FROM playlist_track
JOIN invoice_items
ON playlist_track.TrackId = invoice_items.TrackId
-- QUERY 4: Identify the rows where either TrackId or PlaylistId is NULL (PlaylistTrack table).
SELECT TrackId, PlaylistId
FROM playlist_track
WHERE TrackId is null OR PlaylistId is null
-- QUERY 5: Group the songs according to the different types of media (use a count) (line count : 5)
SELECT MediaTypeId, count(MediaTypeId)
FROM tracks
Group by MediaTypeId
-- QUERY 6: Show the number of tracks for each playlist that have more than 100 tracks. (line count : ())
SELECT PlaylistId, COUNT(TrackId) as counttrack
FROM playlist_track
GROUP BY PlaylistId
HAVING counttrack > 100
-- QUERY 7: Show the number of tracks for each playlist with an even PlaylistId that have more than 100 tracks. (line count : 2)
SELECT PlaylistId, COUNT(TrackId) as counttrack
FROM playlist_track
WHERE PlaylistId%2 = 0
GROUP BY PlaylistId
HAVING counttrack > 100
-- QUERY 8: Join table PlaylistTrack with Playlist (line count : 8715)
SELECT *
FROM playlist_track
JOIN playlists
ON playlist_track.PlaylistId = playlists.PlaylistId
-- QUERY 9: Join table PlaylistTrack with Playlist without any column duplicate (line count : 8715)
SELECT TrackId, Name, playlist_track.PlaylistId
FROM playlist_track
JOIN playlists
ON playlist_track.PlaylistId = playlists.PlaylistId
-- QUERY 10: Join table PlaylistTrack with Playlist without any column duplicate and using aliases in your code (AS) (line count : 8715)
SELECT TrackId, Name, playlist_track.PlaylistId as saucisse_de_morteau
FROM playlist_track
JOIN playlists
ON playlist_track.PlaylistId = playlists.PlaylistId
-- QUERY 11: How many track does each playlist have? Show the name of the playlist in your result. (line count : 14)
SELECT name, COUNT(TrackId)
FROM playlist_track
JOIN playlists
ON playlist_track.PlaylistId = playlists.PlaylistId
GROUP BY name
-- QUERY 12: Are they albums title whose names are similar to playlists name ?
SELECT albums.Title
FROM albums
WHERE (SELECT playlists.Name from playlists ) = albums.Title
-- QUERY 13: Count the number of albums for each genre. Order the results by most to least popular genre. (line count : 25)
Select GenreId, count(AlbumId) as popu
from tracks
group by GenreId
order by popu DESC
-- QUERY 14: Show the same result and add the name of the genre. (line count : 25)
Select genres.Name, count(AlbumId) popu
  from tracks
  JOIN genres
    ON genres.GenreId = tracks.GenreId
 group by tracks.GenreId
 order by popu DESC
-- QUERY 15: Count the number of playlists for each genre. Order the results by most to least popular genre. (line count : 25)
Select  tracks.GenreId, count(playlist_track.PlaylistId) as pop
  from tracks
  JOIN playlist_track
    ON playlist_track.TrackId = tracks.TrackId
 group by tracks.GenreId
 order by pop DESC
-- QUERY 16: How many different media, genre, tracks, albums and artists are there in this DB (1 request) ?
SELECT count( DISTINCT MediaTypeId),count(DISTINCT AlbumId),count(DISTINCT name), count(DISTINCT GenreId),count(DISTINCT Composer)
FROM tracks
-- QUERY 17: Which playlist or playlists have no tracks? (line count : 4)
Select PlaylistId
from playlist_track
where TrackId is not null
