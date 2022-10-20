-- a script that list all comedy shows in a database
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres AS show_gen ON tv_shows.id = show_gen.show_id
JOIN tv_genres ON show_gen.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title
