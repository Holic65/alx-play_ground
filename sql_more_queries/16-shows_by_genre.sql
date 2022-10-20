-- a script that shows all the shows and genre linked to it
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres AS show_gen ON tv_shows.id = show_gen.show_id
LEFT JOIN tv_genres ON show_gen.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
