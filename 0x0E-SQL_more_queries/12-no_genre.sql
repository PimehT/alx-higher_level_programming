-- Script that lists all shows contained in the database hbtn_0d_tvshows
-- Each record display: `tv_shows.title` - `tv_show_genres.genre_id`
-- show only titles where genre is NULL

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
