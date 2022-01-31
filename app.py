from router import Router
from request import Request
from jinja2 import Environment, FileSystemLoader
import os
from response import TemplateResponse


class App:
    def __init__(self, templates=None):
        self.router = Router()
        if templates is None:
            templates = [os.path.join(os.path.abspath('.'), 'templates')]
        self.jinja2_environment = Environment(
            loader=FileSystemLoader(templates))

    def route(self, path=None, method='GET', callback=None):
        def decorator(callback_func):
            self.router.add(method, path, callback_func)
            return callback_func
        return decorator(callback) if callback else decorator

    def __call__(self, env, start_response):
        method = env['REQUEST_METHOD'].upper()
        path = env['PATH_INFO'] or '/'
        callback, kwargs = self.router.match(method, path)

        response = callback(Request(env), **kwargs)
        start_response(response.status, response.header_list)
        if isinstance(response, TemplateResponse):
            return [response.render_body(self.jinja2_environment)]
        return [response.body]
