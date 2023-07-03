CREATE TABLE IF NOT EXISTS Genre (genre_id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL);
CREATE TABLE IF NOT EXISTS Musician (musician_id SERIAL PRIMARY KEY, alias VARCHAR(30) NOT NULL);
CREATE TABLE IF NOT EXISTS Album (album_id SERIAL PRIMARY KEY, name VARCHAR(15) NOT NULL, release_date DATE);
CREATE TABLE IF NOT EXISTS Collection (collection_id SERIAL PRIMARY KEY, name VARCHAR(15) NOT NULL, release_date DATE);

-- создадим связь один-к-одному
CREATE TABLE IF NOT EXISTS Track (
	track_id SERIAL PRIMARY KEY,
	name VARCHAR(15) NOT NULL,
	duration INTEGER,
	album_id INTEGER REFERENCES Album(album_id)
);

-- создадим связи многие-ко-многим
CREATE TABLE IF NOT EXISTS Genre_musician (
	genre_id INTEGER REFERENCES Genre(genre_id) NOT NULL,
	musician_id INTEGER REFERENCES Musician(musician_id) NOT NULL,
	CONSTRAINT genre_musician_id PRIMARY KEY (genre_id, musician_id)
);
CREATE TABLE IF NOT EXISTS Album_musician (
	musician_id INTEGER REFERENCES Musician(musician_id) NOT NULL,
	album_id INTEGER REFERENCES Album(album_id) NOT NULL,
	CONSTRAINT album_musician_id PRIMARY KEY (album_id, musician_id)
);
CREATE TABLE IF NOT EXISTS Collection_track (
	collection_id INTEGER REFERENCES Collection(collection_id) NOT NULL,
	track_id INTEGER REFERENCES Track(track_id) NOT NULL,
	CONSTRAINT collection_track_id PRIMARY KEY (collection_id, track_id)
);