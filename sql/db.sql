create database cometdb;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);


--psql
\dt --список таблиц
\c cometdb --подключится к бд
\quit
DROP TABLE users;
select * from users --
uvicorn main:app --reload --host 0.0.0.0

CREATE TABLE Users(
    user_id UUID NOT NULL primary key,
    username text,
    email text,
    password text);
