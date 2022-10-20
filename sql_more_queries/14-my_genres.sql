-- a script that list all genres of the show dexter
SELECT gen.name
FROM tv_show_genres as show_gen
RIGHT JOIN tv_genres AS gen ON show_gen.genre_id = gen.id
WHERE show_gen.show_id = 8
ORDER BY gen.name
