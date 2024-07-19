-- list all shows contain in hbtn_0d_tvshows that have at least one genre linked.
-- each record should display: `tv-shows.title - tv_show_genres.genre_id
-- can only use one SELECT statement

SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_show_genres JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
