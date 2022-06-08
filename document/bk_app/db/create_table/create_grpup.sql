CREATE TABLE todo_scratch.`group` (
	group_id int auto_increment PRIMARY KEY,
	group_name varchar(30),
	description TEXT,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    