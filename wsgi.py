# 1. WSGIのアプリケーションは、2つの引数を持った呼び出し可能なオブジェクトである。

# 2. 第2引数として渡されたオブジェクトを呼び出し、HTTPステータスコードとヘッダ情報を渡す。

# 3. レスポンスボディとしてバイト文字列をyieldするiterableなオブジェクトを返す。

import os
from static_middleware import StaticMiddleware
from response import Response, TemplateResponse
from wsgiref.simple_server import make_server
from app import App


def app(env, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    print('Hello, World!!!')
    return [b'Hello World Hikaru']


def create_app():
    app = App()

    BASE_DIR = os.path.dirname(__name__)
    STATIC_DIRS = [os.path.join(BASE_DIR, 'static')]

    @app.route('^/$', 'GET')
    def hello(request):
        return Response('Hello World')

    @app.route('^/user/$', 'POST')
    def create_user(request):
        return Response('User Created', status=201)

    @app.route('^/user/$', 'GET')
    def users(request):
        users = ['user%s' % i for i in range(10)]
        return TemplateResponse('users.html', title='User List', users=users)

    @app.route('^/user/(?P<name>\w+)$', 'GET')
    def user_detail(request, name):
        return Response('Hello {name}'.format(name=name))

    app = StaticMiddleware(app, static_root='static', static_dirs=STATIC_DIRS)

    return app
