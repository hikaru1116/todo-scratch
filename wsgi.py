from todo_scratch.bk_base.core.wsgi_handler import WsgiApplication
import os

os.environ.setdefault('SETTINGS_PATH', 'todo_scratch.bk_app.settings')

app = WsgiApplication()
