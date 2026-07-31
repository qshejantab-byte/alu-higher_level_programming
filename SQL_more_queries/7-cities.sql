-- Creates the database hbtn_0d_usa, without failing if it exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Creates the cities table, referencing states via a foreign key,
-- without failing if the table already exists
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
