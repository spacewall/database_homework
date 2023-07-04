DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS musician CASCADE;
DROP TABLE IF EXISTS album CASCADE;
DROP TABLE IF EXISTS collection CASCADE;
DROP TABLE IF EXISTS track CASCADE;
DROP TABLE IF EXISTS genre_musician CASCADE;
DROP TABLE IF EXISTS album_musician CASCADE;
DROP TABLE IF EXISTS collection_track CASCADE;

CREATE TABLE IF NOT EXISTS genre (
	genre_id SERIAL PRIMARY KEY, 
	title VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS musician (
	musician_id SERIAL PRIMARY KEY,
	alias_or_band VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	album_id SERIAL PRIMARY KEY, 
	title VARCHAR(30) UNIQUE NOT NULL, 
	release_year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS collection (
	collection_id SERIAL PRIMARY KEY, 
	title VARCHAR(20) NOT NULL, 
	release_year INTEGER NOT NULL
);

-- создадим связь один-к-одному
CREATE TABLE IF NOT EXISTS track (
	track_id SERIAL PRIMARY KEY,
	name_of_track VARCHAR(30) NOT NULL,
	duration INTEGER,
	album_id INTEGER REFERENCES album(album_id)
);

-- создадим связи многие-ко-многим
CREATE TABLE IF NOT EXISTS genre_musician (
	genre_id INTEGER REFERENCES genre(genre_id) NOT NULL,
	musician_id INTEGER REFERENCES musician(musician_id) NOT NULL,
	CONSTRAINT genre_musician_id PRIMARY KEY (genre_id, musician_id)
);
CREATE TABLE IF NOT EXISTS album_musician (
	musician_id INTEGER REFERENCES musician(musician_id) NOT NULL,
	album_id INTEGER REFERENCES album(album_id) NOT NULL,
	CONSTRAINT album_musician_id PRIMARY KEY (album_id, musician_id)
);
CREATE TABLE IF NOT EXISTS collection_track (
	collection_id INTEGER REFERENCES collection(collection_id) NOT NULL,
	track_id INTEGER REFERENCES track(track_id) NOT NULL,
	CONSTRAINT collection_track_id PRIMARY KEY (collection_id, track_id)
);