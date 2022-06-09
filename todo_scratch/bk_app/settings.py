# デバックモード設定。
IS_DEBUG = True

# アプリケーションプロジェクト設定(必須)
# アプリケーションプロジェクトのパス設定
APP_PATH = 'todo_scratch.bk_app'
# urlルーティングファイルのファイル名
URLS_PATH = 'urls'

# DB設定 (DB操作する場合は、必須)
# 操作するDBの種類 設定値:"mysql",（他DBは順次対応)
DB_TYPE = "mysql"
DB_NAME = 'todo_scratch'
DB_CONFIG = {
    'host': '192.168.64.3',
    'port': '3306',
    'user': 'admin',
    'password': 'P@ssw0rd',
    'database': 'todo_scratch'
}

# リソースアクセスを許可するオリジン設定
ACCESS_ALLOW_ORIGIN = ["http://localhost:3000"]

# ミドルウェア設定
# ミドルウェア処理を実行するミドルウェアクラスを追加します。
MIDDLEWARES = [
    "atom_bk_frame.middleware.http_log_middleware.HttpLogMiddleware",
    "atom_bk_frame.middleware.cors_middleware.CorsMiddleware",
    "atom_bk_frame.middleware.session_middleware.SessionMiddleware"
]

# 認証・認可機能
# 認証ユーザエンティティ設定（認証ユーザとなるテーブルを定義したエンティティを設定）
AUTH_USER_ENTITY = "todo_scratch.bk_app.entities.user_entity.UserEntity"
# 認証キー
SECRET_KEY = "xxxxx"
# セッションの有効期限
SESSION_EXPIRED_DAYS = 31
# 二段階認証の設定（未実装）
IS_TWO_STEP_VERFICATION_BY_EMAIL = False
