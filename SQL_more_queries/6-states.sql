-- Creates the database hbtn_0d_usa, without failing if it exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switches to the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Creates the states table with an auto-generated primary key,
-- without failing if the table already exists
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
