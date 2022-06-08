CREATE TABLE todo_scratch.comment (
	comment_id int auto_increment PRIMARY KEY,
	user_id INT,
	task_id INT,
	comment TEXT,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY fk_comment_user_id(user_id) REFERENCES todo_scratch.`user`(user_id),
    FOREIGN KEY fk_comment_task_id(task_id) REFERENCES todo_scratch.task(task_id)
    )