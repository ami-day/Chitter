1. Design the SQL table based on User Stories

As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

The SQL design will consist of 2 tables called posts and users. They will consist of the following properties:

Table name | Properties
------------------------
posts      | message, time, user_id
users      | user_name, username, user_email, user_password

The tables will be joined on user_id as users.id

2. Specify the data types

Table: posts
id: SERIAL
message: text
time: date
user_id: int

Table: users
id: SERIAL
user_name: text
username: text
user_email: email
user_password: text

3. Write the SQL to create the tables

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

