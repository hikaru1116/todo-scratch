
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

DB_NAME = 'todo_scratch'

MIDDLEWARES = [
    "atom_bk_frame.middleware.http_log_middleware.HttpLogMiddleware",
    "atom_bk_frame.middleware.cors_middleware.CorsMiddleware",
    "atom_bk_frame.middleware.session_middleware.SessionMiddleware"
]

AUTH_USER_ENTITY = "todo_scratch.bk_app.entities.user_entity.UserEntity"

SECRET_KEY = "xxxxx"

IS_TWO_STEP_VERFICATION_BY_EMAIL = False

SESSION_EXPIRED_DAYS = 31
