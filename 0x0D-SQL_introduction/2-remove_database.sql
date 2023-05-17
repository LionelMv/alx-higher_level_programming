-- delete database; shouldn't fail if non-existent
-- cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

DROP DATABASE IF EXISTS hbtn_0c_0;
