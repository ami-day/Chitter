DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq CASCADE;

CREATE TABLE users (
id SERIAL PRIMARY KEY,
user_name text,
username text,
user_email text,
user_password text);

CREATE TABLE posts (
id SERIAL PRIMARY KEY,
message text,
time date,
user_id int,
constraint fk_userid foreign key(user_id)
references users(id)
on delete cascade
);

INSERT INTO users (user_name, username, user_email, user_password) VALUES ('Sam Morgan','sjmog','samm@makersacademy.com','password123');

INSERT INTO POSTS (message, time, user_id) VALUES ('Hello World','2022-03-10',1);