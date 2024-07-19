-- Script that lists all genres from hbtn_0d_tvshows linked to the show `Dexter`
-- Display: tv_genres.name
-- Result sorted in ascending order by the genre name

SELECT tv_genres.name AS name
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
