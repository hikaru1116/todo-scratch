CREATE TABLE todo_scratch.task (
	task_id int auto_increment PRIMARY KEY,
	group_id int,
	user_id int,
	title VARCHAR(50),
	context TEXT,
	deadline_at DATETIME NOT NULL,
	task_status_id int,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY fk_task_user_id(user_id) REFERENCES todo_scratch.`user`(user_id),
    FOREIGN KEY fk_task_group_id(group_id) REFERENCES todo_scratch.`group`(group_id),
    FOREIGN KEY fk_task_task_status_id(task_status_id) REFERENCES todo_scratch.task_status(task_status_id)
    )