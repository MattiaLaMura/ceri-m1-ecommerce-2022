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