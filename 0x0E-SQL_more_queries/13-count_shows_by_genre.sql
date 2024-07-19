-- Script that lists all genres from hbtn_0d_tvshows and display the no. of shows linked to each
-- Display: <TV Show genre> - <Number of shows linked to this genre>
-- Result is sorted in descending order

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
