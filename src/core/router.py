import re
from typing import Callable, List, Tuple


def http404(env: dict, start_response: Callable) -> List[bytes]:
    start_response(
        '404 Not Found', [
            ('Content-type', 'text/plain; charset=utf-8')])
    return [b'404 Not Found']


def http405(env: dict, start_response: Callable) -> List[bytes]:
    start_response(
        '405 Method Not Allowed', [
            ('Content-type', 'text/plain; charset=utf-8')])
    return [b'405 Method Not Allowed']


class Router:
    def __init__(self):
        self.routes = []

    def add(self, method: List[str], path: str, callback: Callable) -> None:
        self.routes.append({
            'method': method,
            'path': path,
            'path_compiled': re.compile(path),
            'callback': callback
        })

    def match(self, method: str, path: str) -> Tuple[Callable, dict]:
        error_callback = http404
        for route in self.routes:
            matched = route['path_compiled'].match(path)
            if not matched:
                continue

            error_callback = http405
            url_vars = matched.groupdict()
            if method == route['method']:
                return route['callback'], url_vars
        return error_callback, {}
