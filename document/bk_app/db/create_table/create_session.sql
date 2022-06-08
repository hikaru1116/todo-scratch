CREATE TABLE todo_scratch.group_belongs (
	group_belongs_id int auto_increment PRIMARY KEY,
	group_id int,
	user_id int,
	auth_type int,
	user_status int,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY fk_group_belongs_group_id(group_id) REFERENCES todo_scratch.`group`(group_id),
    FOREIGN KEY fk_group_belongs_user_id(user_id) REFERENCES todo_scratch.`user`(user_id)
    )