-- create database; shouldn't fail if non-existent
-- cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
