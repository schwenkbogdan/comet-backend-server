create database cometdb;




--psql
\dt --список таблиц
\c cometdb --подключится к бд
\quit
DROP TABLE users;
select * from users --
uvicorn main:app --reload --host 0.0.0.0

