-- Creates the table id_not_null, defaulting id to 1 so it's never
-- left empty, without failing if the table already exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
