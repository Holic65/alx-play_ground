-- a script that list all cities contained in a database
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
