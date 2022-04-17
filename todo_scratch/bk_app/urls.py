import typing as t
from todo_scratch.bk_app.hello_controller import HelloController

from todo_scratch.bk_base.core.url_pattern import UrlPattern

urlpatterns: t.List[UrlPattern] = [
    UrlPattern(path='^/$', controller=HelloController())
]
