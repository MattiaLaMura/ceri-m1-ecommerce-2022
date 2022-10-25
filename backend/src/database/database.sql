CREATE TABLE IF NOT EXISTS artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS album (
    album_id INT AUTO_INCREMENT,
    artist_id INT,
    album_title VARCHAR(255) NOT NULL,
    album_year DATE NOT NULL,
    PRIMARY KEY (album_id , artist_id),
    FOREIGN KEY (artist_id)
        REFERENCES artist (artist_id)
        ON UPDATE RESTRICT ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS song (
    song_id INT AUTO_INCREMENT,
    album_id INT,
    song_title VARCHAR(255) NOT NULL,
    song_length INT NOT NULL,
    PRIMARY KEY (song_id , album_id),
    FOREIGN KEY (album_id)
        REFERENCES album (album_id)
        ON UPDATE RESTRICT ON DELETE CASCADE
);

-- INSERT INTO artist(artist_name, is_active) VALUES ("Lorenzo", true);
-- INSERT INTO artist(artist_name, is_active) VALUES ("Mattia", false);
-- INSERT INTO artist(artist_name, is_active) VALUES ("Bastien", true);

-- insert into album (artist_id, album_title, album_year) values ((select artist_id from artist where artist_name = 'Lorenzo'), 'Album de Lorenzo', "2022-10-21");
-- INSERT INTO album SET album_title = 'Album de Lorenzo', album_year = "2022-10-21"
-- INSERT INTO album(album_title, album_year) VALUES (1, "Album de Lorenzo", "2022-10-21") ;
-- INSERT INTO album(album_title, album_year) VALUES (2, "Album de Mattia", "2018-12-06");
-- INSERT INTO album(album_title, album_year) VALUES (3, "Album de Bastien", "2021-01-12");