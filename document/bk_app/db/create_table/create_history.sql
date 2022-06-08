CREATE TABLE todo_scratch.history (
	history_id int auto_increment PRIMARY KEY,
	task_id INT,
	history_text TEXT,
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY fk_history_task_id(task_id) REFERENCES todo_scratch.task(task_id)
    )