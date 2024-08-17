create database Python_Db;
create table users(
	ID int unique auto_increment,
    username varchar(255),
    Nombre varchar(255),
    password varchar(255),
    primary key (ID)
);
select * from users;