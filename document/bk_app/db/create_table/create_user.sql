CREATE TABLE todo_scratch.`user` (
	user_id int auto_increment PRIMARY KEY,
	user_name varchar(30),
	email varchar(50),
	password varchar(100),
	is_admin BOOLEAN DEFAULT FALSE,
	icon TEXT,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )