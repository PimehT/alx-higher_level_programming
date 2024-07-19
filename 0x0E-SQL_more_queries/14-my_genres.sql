-- Script that lists all genres from hbtn_0d_tvshows linked to the show `Dexter`
-- Display: tv_genres.name
-- Result sorted in ascending order by the genre name

SELECT tv_genres.name AS name
FROM tv_show_genres NATURAL JOIN tv_genres NATURAL JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.name = 'Dexter'
ORDER BY tv_genres.name ASC;
