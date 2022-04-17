from todo_scratch.bk_base.core.wsgi_app import WsgiApp
import os

os.environ.setdefault('SETTINGS_PATH', 'todo_scratch.bk_app.settings')

app = WsgiApp()
