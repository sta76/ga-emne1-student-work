-- Enkel spørring for å hente alle kolloner og rader i oppgitt tabell(city)
SELECT *
FROM city;

SELECT *
FROM city
WHERE CountryCode = 'NOR'


SELECT Name, Population, ID
FROM city

SELECT Name, Population, ID
FROM city
WHERE CountryCode = 'SWE'


SELECT Name, Population, ID
FROM city
WHERE Population > 1000000

SELECT Name, Population
FROM country
WHERE Continent = 'Europe';

SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
    AND Population > 200000;

SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
    OR CountryCode = 'SWE')
    AND Population > 200000;

SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
       OR CountryCode = 'SWE')
    AND Population > 200000
Order By Name ASC;

SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
       OR CountryCode = 'SWE')
    AND Population > 200000
Order By Name DESC;


SELECT Name, Population
FROM city
WHERE Population > 1000000
Order By Population DESC;

SELECT Name, Population
FROM city
Order By Population DESC
LIMIT 5;

-- Wildcard %
SELECT Name
FROM city
WHERE Name LIKE'O%o'

-- Wildcard __
SELECT Name
FROM city
WHERE Name LIKE'O__o'