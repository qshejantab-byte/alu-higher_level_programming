-- Creates the user user_0d_1 with all privileges, without failing
-- if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on the server to user_0d_1, including the
-- ability to grant privileges to others
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
