#
# drop table if exists users;
#
# create table users (
# 	id serial,
# 	email varchar(255) default null,
# 	username varchar(55) default null,
# 	first_name varchar(55) default null,
# 	last_name varchar(55) default null,
# 	hashed_password varchar(255) default null,
# 	is_active boolean default null,
# 	primary key (id)
# );
#
# drop table if exists todos;
#
# create table todos (
# 	id serial,
# 	title varchar(255) default null,
# 	description varchar(255) default null,
# 	priority integer default null,
# 	complete boolean default null,
# 	owner_id integer default null,
# 	primary key (id),
# 	foreign key (owner_id) references Users(id)
# );