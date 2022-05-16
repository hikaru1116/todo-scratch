import typing as t
from todo_scratch.bk_app.controllers.account_controller import AccountController
from todo_scratch.bk_app.controllers.auth_test_controller import AuthorizedController, ForbddenController
from todo_scratch.bk_app.controllers.group_controller import GroupController
from todo_scratch.bk_app.controllers.group_joined_controller import GroupJoinedController
from todo_scratch.bk_app.controllers.hello_controller import HelloController
from todo_scratch.bk_base.core.url_pattern import UrlPattern

urlpatterns: t.List[UrlPattern] = [
    UrlPattern(path='^/$', controller=HelloController()),
    UrlPattern(path='^/authorized', controller=AuthorizedController()),
    UrlPattern(path='^/forbidden', controller=ForbddenController()),
    UrlPattern(path='^/group$', controller=GroupController()),
    UrlPattern(path='/group/<int>$', controller=GroupController()),
    UrlPattern(path='/group/joined$', controller=GroupJoinedController()),
    UrlPattern(path='^/account$', controller=AccountController()),
]
