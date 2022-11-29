
/* Exercise 1 */

-- Query 1 : Display the CDs that came out in 1998. (line count: 35)
SELECT Title
FROM Disc
WHERE Year = 1998
-- Query 2 : Display the CDs published in 21st century. (line count: 142)
SELECT Title
FROM Disc
WHERE Year > 2000
-- Query 3 : Display the CDs that came out in the 90s. (line count: 291)
SELECT Title, Year
FROM Disc
WHERE Year BETWEEN 1990 AND 1999
-- Query 4 : Display the different names of states of CDs (without repretition). (line count: 4)
SELECT DISTINCT State
FROM Disc
-- Query 5 : Find the titles of all damaged CDs. (line count: 170)
SELECT Title
FROM Disc
WHERE State LIKE 'Damaged'
-- Query 6 : Find cheap used CDs (price below 11). Order the result by the price (ascending). (line count: 30)
SELECT Title, Price
FROM Disc
WHERE Price < 11 AND State LIKE 'used'
ORDER BY Price DESC
-- Query 7 : Find CDs that came out either in 1990 or 1995 and whose price is between 10 and 15. (line count: 26)
SELECT Title, Price
FROM Disc
WHERE (Year = 1990 OR Year = 1995) AND Price BETWEEN 10 AND 15 

-- Query 8 : Find the number of CDs that came out in the 80s and their price is between 12 and 14. (line count:42)
SELECT Title, Price
FROM Disc
WHERE Year BETWEEN 1980 AND 1989 AND Price BETWEEN 12 AND 14

-- Query 9 : Find the total of prices of destroyed CD. (the answer is 627.97) (line count: 1)
SELECT SUM(Price)
FROM Disc
WHERE State LIKE 'Destroyed'

-- Query 10 : Find CD by ’The Beatles’. (line count: 6)
SELECT Artist.Name, Disc.Title
FROM Disc
JOIN Artist ON Artist_ID = ID
WHERE Artist.Name LIKE 'The Beatles'

-- Query 11 : Find CDs by ’AC DC’ that came out in the 90s. (line count: 4)
SELECT Artist.Name, Disc.Title
FROM Disc
JOIN Artist ON Artist_ID = ID
WHERE (Artist.Name LIKE 'AC%DC') AND Year BETWEEN 1990 AND 1999

-- Query 12 : Find artists names who had a CD in 1991. (line count: 25)
SELECT DISTINCT Artist.Name
FROM Disc
JOIN Artist ON Artist_ID = ID
WHERE Year = 1991

-- Query 13 : Find the sum of prices of all CD by Georges Brassens. (the answer is 200.73) (line count: 1)
SELECT SUM(Disc.Price)
FROM Disc
JOIN Artist ON Artist_ID = ID
WHERE Artist.Name LIKE 'Georges Brassens'

-- Query 14 : Find titles of song of the Rock genre. (line count: 5504)
SELECT Song.Title
FROM Song
JOIN Genre ON Song.Genre_ID = Genre.ID
WHERE Genre.Name LIKE 'Rock'

-- Query 15 : List titles of songs whose genre description uses the word ’afric’. (line count: 334)
SELECT Song.Title
FROM Song
JOIN Genre ON Song.Genre_ID = Genre.ID
WHERE Genre.Description LIKE '%afric%'

-- Query 16 : Find the number of folk songs whose lyrics are not covered by copyright. (the answer is 124) (line count: 1)
SELECT COUNT(Song.Title)
FROM Song
JOIN Genre ON Song.Genre_ID = Genre.ID
WHERE Genre.Name LIKE 'Folk' AND Song.Free_lyrics = 1

-- Query 17 : Find song titles written by Jacques Brel. (line count: 134)
SELECT Song.Title
FROM Song
JOIN Written ON Song.ID = Written.Song_ID
WHERE Written.Artist_ID = (SELECT ID FROM Artist WHERE Name LIKE 'Jacques Brel' )

-- Query 18 : Find artists who have written the song ’Anybody Seen My Baby?’. (line count: 2)
SELECT Artist.Name
FROM Artist
JOIN Written ON Artist.ID = Written.Artist_ID
WHERE Written.Song_ID = (SELECT ID FROM Song WHERE Title LIKE 'Anybody Seen My Baby?')

-- Query 19 : find the number of CDs with songs written by Mick Jagger. (the answer is 54) (line count: 1)
SELECT DISTINCT COUNT(Disc.Title)
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
JOIN Song ON Listing.Song_ID = Song.ID
JOIN Written ON Song.ID = Written.Song_ID
JOIN Artist ON Written.Artist_ID = Artist.ID
WHERE Artist.Name LIKE 'Mick%Jagger'

/* Become now harder */
/*Si vous avez des requêtes imbriquées, il faut utiliser un WITH ! */

-- Query 20 : Find the song list on the CD A Night at the Opera, in the order of their position. (line count: 12)
SELECT Song.Title
FROM Song
JOIN Listing ON Song.ID = Listing.Song_ID
JOIN Disc ON Disc.CDDB = Listing.CDDB
WHERE DIsc.Title LIKE 'A Night at the Opera'
ORDER BY Listing.Pos

-- Query 21 : Find name of Artists who have not written a single song. (line count: 506)
SELECT Artist.Name
FROM Artist
LEFT JOIN Written ON Written.Artist_ID = Artist.ID
LEFT JOIN Song ON Song.ID = Written.Song_ID
WHERE Song.Title IS NULL

-- Query 22 : List songs performed by Lenny Kravitz that are present on David Bowie’s CDs. (line count: 1)
SELECT Disc.Title
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
WHERE Listing.Artist_ID = (SELECT ID FROM Artist WHERE Name LIKE '%kravitz%')
AND Disc.Artist_ID = (SELECT ID FROM Artist WHERE Name LIKE 'David%Bowie')

-- Query 23 : Find CDs that contain at least one song performed by an artist different from the (main) artist of the
-- disc. (line count: 37)
SELECT DISTINCT Disc.Title
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
WHERE Listing.Artist_ID != Disc.Artist_ID

-- Query 24 : Find CDs that contain at least one song written by an artist different from the (main) artist of the
-- CD. (line count: 83)
SELECT DISTINCT Disc.Title
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
JOIN Written ON Listing.Song_ID = Written.Song_ID
WHERE Disc.Artist_ID != Written.Artist_ID

-- Query 25 : List the number and the average price of CD for every different state. (line count: 4)
SELECT State, COUNT(Title),AVG(Price)
FROM Disc
GROUP BY State

-- Query 26 : For every artist find the number of their CDs. Display the results in the descending order of the
-- number of CDs (line count: 273)
SELECT Artist.Name, Disc.Artist_ID, COUNT(Disc.Title)
FROM Disc
JOIN Artist ON Artist.ID = Disc.Artist_ID
GROUP BY Artist.Name
ORDER BY COUNT(Disc.Title) DESC

-- Query 27 : For every CD list its title and the number of songs it contains. display only CD with at least 10 songs
-- (line count: 688)
SELECT Disc.Title, COUNT(Listing.Song_ID) as count_songs
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
GROUP BY Disc.Title
HAVING count_songs >= 10

-- Query 28 : For every genre find the number of CDs that contain a song of this genre. Mind not to count the
-- same CD more than once. Display genres with more than 50 songs (line count: 4)
SELECT Genre.Name, COUNT(DISTINCT Disc.Title)
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
JOIN Song ON Listing.Song_ID = Song.ID
JOIN Genre ON Song.Genre_ID = Genre.ID
GROUP BY Genre.Name
HAVING COUNT(DISTINCT Disc.Title) > 50

-- Query 29 : List the artists in the descending order of the average price of their CDs. List only those artists who
-- have at least 4 CDs for which the average CD price is above 12. (line count: 61)
SELECT Artist.Name, AVG(Disc.Price)as avg_price, COUNT(Disc.Title) as count_discs
FROM Disc
JOIN Artist ON Disc.Artist_ID = Artist.ID
GROUP BY Artist.Name
HAVING count_discs >= 4 AND avg_price > 12
ORDER BY avg_price DESC

/* Questions Bonus (Optionnelles) */

-- Query 30 : Find CD whose list of songs is potentially incomplete. (Hint: compare the number of songs with
-- the position of the last song). (line count: 24)
SELECT Disc.Title, COUNT(Listing.Song_ID) as count_songs, MAX(Pos) as max_pos
FROM Disc
JOIN Listing ON Disc.CDDB = Listing.CDDB
GROUP BY Disc.CDDB
HAVING count_songs != max_pos

-- Query 31 : Find frequent collaborators. Any pair of artists who have performed a song on the same CD are
-- collaborators. If there are at least 2 CDs, then this pair are frequent collaborators. (there is only 5 such pairs)
-- (line count: 10)

