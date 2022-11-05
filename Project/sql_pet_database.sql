CREATE DATABASE pet_database;

USE pet_database;


CREATE TABLE character_game_save (
    character_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    weather_score VARCHAR(10) NOT NULL,
    feed_pet_score VARCHAR(10) NOT NULL,
    rock_paper_scissors_score VARCHAR(10) NOT NULL,
    date_created VARCHAR(30) NOT NULL
);

SELECT 
    *
FROM
    character_game_save;