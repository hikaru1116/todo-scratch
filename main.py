from app import App
from wsgiref.simple_server import make_server
from response import Response, TemplateResponse
from static_middleware import StaticMiddleware
import os

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


if __name__ == '__main__':
    app = StaticMiddleware(app, static_root='static', static_dirs=STATIC_DIRS)
    httpd = make_server('', 8000, app)
    httpd.serve_forever()
