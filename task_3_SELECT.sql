SELECT name_of_track, duration FROM track
WHERE duration = (SELECT MAX(duration) FROM track);

SELECT name_of_track, duration FROM track
WHERE duration >= 3.5;

SELECT title, release_year FROM collection
WHERE release_year BETWEEN 2018 AND 2020;

SELECT alias_or_band FROM musician
WHERE alias_or_band NOT LIKE '% %';

SELECT name_of_track FROM track
WHERE UPPER(name_of_track) LIKE '%MY%' OR UPPER(name_of_track) LIKE '%МОЙ%';

SELECT * FROM (SELECT genre_id, COUNT(musician_id) FROM genre_musician
GROUP BY genre_id) t JOIN genre g ON g.genre_id = t.genre_id;

SELECT COUNT(a.title) FROM album a
JOIN track t ON t.album_id = a.album_id
WHERE a.release_year BETWEEN 2019 AND 2020
GROUP BY a.title;

SELECT * FROM (SELECT t.album_id, AVG(t.duration) FROM track t
JOIN album a ON a.album_id = t.album_id
GROUP BY t.album_id) t JOIN album a ON a.album_id = t.album_id;

SELECT m.alias_or_band FROM musician m
JOIN (SELECT * FROM album_musician am 
JOIN album a ON a.album_id = am.album_id
WHERE a.release_year != 2020) t ON m.musician_id = t.musician_id;

SELECT c.title FROM collection c
JOIN (SELECT DISTINCT ct.collection_id FROM collection_track ct
JOIN (SELECT t.track_id FROM track t
JOIN (SELECT am.album_id FROM album_musician am 
JOIN musician m ON m.musician_id = am.musician_id
WHERE m.alias_or_band = 'Slayer') al ON al.album_id = t.album_id) tr
ON tr.track_id = ct.track_id) cll ON c.collection_id = cll.collection_id;