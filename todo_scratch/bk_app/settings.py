
APP_PATH = 'todo_scratch.bk_app'

URLS_PATH = 'urls'

IS_DEBUG = True

DB_TYPE = "mysql"

DB_CONFIG = {
    'host': '192.168.64.3',
    'port': '3306',
    'user': 'admin',
    'password': 'P@ssw0rd',
    'database': 'todo_scratch'
}

ACCESS_ALLOW_ORIGIN = ["http://localhost:3000"]


MIDDLEWARES = [
    "todo_scratch.bk_base.middleware.http_log_middleware.HttpLogMiddleware",
    "todo_scratch.bk_base.middleware.cors_middleware.CorsMiddleware",
    "todo_scratch.bk_base.middleware.test_middleware.TestMiddleware"
]
