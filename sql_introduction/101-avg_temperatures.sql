-- a script that displays average temperature of city
SELECT city, AVG(VALUE) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
