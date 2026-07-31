-- Creates the table force_name, requiring a name on every row,
-- without failing if the table already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
