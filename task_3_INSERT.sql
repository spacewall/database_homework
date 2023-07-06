INSERT INTO genre(genre_id, title) VALUES (0, 'метал');
INSERT INTO genre(genre_id, title) VALUES (1, 'блюз');
INSERT INTO genre(genre_id, title) VALUES (2, 'панк');

INSERT INTO musician(musician_id, alias_or_band) VALUES (0, 'Slayer');
INSERT INTO musician(musician_id, alias_or_band) VALUES (1, 'Dethklok');
INSERT INTO musician(musician_id, alias_or_band) VALUES (2, 'Rise Against');
INSERT INTO musician(musician_id, alias_or_band) VALUES (3, 'Jean-Pierre Bertrand');

INSERT INTO album VALUES (0, 'Piano Brotherhood', 2015);
INSERT INTO album VALUES (1, 'Seasons In The Abyss', 1990);
INSERT INTO album VALUES (2, 'The Sufferer & The Witness', 2006);
INSERT INTO album VALUES (3, 'The Dethalbum', 2007);
INSERT INTO album VALUES (4, 'The UnravelingRe-Issue', 2020);
INSERT INTO album VALUES (5, 'Other', 2021);

INSERT INTO track VALUES (0, 'Thunderhorse', 165, 3);
INSERT INTO track VALUES (1, 'Seasons In The Abyss', 385, 1);
INSERT INTO track VALUES (2, 'Blues O"Clock', 213, 0);
INSERT INTO track VALUES (3, 'Worth Dying For', 200, 2);
INSERT INTO track VALUES (4, 'Awaken', 217, 3);
INSERT INTO track VALUES (5, 'Spirit In Black', 247, 1);
INSERT INTO track VALUES (6, 'My Life Inside Your Heart', 182, 4);
INSERT INTO track VALUES (7, 'myself', 217, 5);
INSERT INTO track VALUES (8, 'by myself', 217, 5);
INSERT INTO track VALUES (9, 'bymy self', 217, 5);
INSERT INTO track VALUES (10, 'myself by', 217, 5);
INSERT INTO track VALUES (11, 'by myself by', 217, 5);
INSERT INTO track VALUES (12, 'beemy', 217, 5);
INSERT INTO track VALUES (13, 'premyne', 217, 5);

INSERT INTO collection VALUES (0, 'Old Slayer Bro', 2018);
INSERT INTO collection VALUES (1, 'Dethplaylist', 2020);
INSERT INTO collection VALUES (2, 'Blues', 2017);
INSERT INTO collection VALUES (3, 'No Punky hoi', 2019);

INSERT INTO genre_musician VALUES (0, 0);
INSERT INTO genre_musician VALUES (0, 1);
INSERT INTO genre_musician VALUES (1, 3);
INSERT INTO genre_musician VALUES (2, 2);

INSERT INTO album_musician VALUES (0, 1);
INSERT INTO album_musician VALUES (1, 3);
INSERT INTO album_musician VALUES (2, 2);
INSERT INTO album_musician VALUES (3, 0);
INSERT INTO album_musician VALUES (2, 4);

INSERT INTO collection_track VALUES (0, 5);
INSERT INTO collection_track VALUES (0, 1);
INSERT INTO collection_track VALUES (1, 0);
INSERT INTO collection_track VALUES (1, 4);
INSERT INTO collection_track VALUES (1, 5);
INSERT INTO collection_track VALUES (1, 1);
INSERT INTO collection_track VALUES (2, 2);
INSERT INTO collection_track VALUES (3, 3);
INSERT INTO collection_track VALUES (3, 6);