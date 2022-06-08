CREATE TABLE todo_scratch.task_status (
	task_status_id int auto_increment PRIMARY KEY,
	group_id int,
	task_status_name VARCHAR(20),
	status_color VARCHAR(30),
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY fk_task_status_group_id(group_id) REFERENCES todo_scratch.`group`(group_id)
    )