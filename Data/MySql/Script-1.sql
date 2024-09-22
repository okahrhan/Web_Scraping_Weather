SELECT *,
       CAST(REPLACE(`Feels Like`, ' °C', '') AS SIGNED) AS feels_like_int
FROM city_weather_data
ORDER BY feels_like_int DESC
limit 10

SELECT * from list_of_country loc 
	