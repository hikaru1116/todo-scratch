import typing as t
from todo_scratch.bk_app.controllers.account_controller import AccountController
from todo_scratch.bk_app.controllers.auth_test_controller import AuthorizedController, ForbddenController
from todo_scratch.bk_app.controllers.group_approval_request_controller import GroupApprovalRequestController
from todo_scratch.bk_app.controllers.group_controller import GroupController
from todo_scratch.bk_app.controllers.group_joined_controller import GroupJoinedController
from todo_scratch.bk_app.controllers.group_leave_controller import GroupLeaveController
from todo_scratch.bk_app.controllers.hello_controller import HelloController
from todo_scratch.bk_app.controllers.task_change_status_controller import TaskChangeStatusController
from todo_scratch.bk_app.controllers.task_comment_controller import TaskCommentController
from todo_scratch.bk_app.controllers.task_controller import TaskController
from todo_scratch.bk_app.controllers.task_status_info_controller import TaskStatusInfoController
from todo_scratch.bk_base.core.url_pattern import UrlPattern

urlpatterns: t.List[UrlPattern] = [
    UrlPattern(path='^/$', controller=HelloController()),
    UrlPattern(path='^/authorized', controller=AuthorizedController()),
    UrlPattern(path='^/forbidden', controller=ForbddenController()),
    UrlPattern(path='^/group$', controller=GroupController()),
    UrlPattern(path='/group/<int>$', controller=GroupController()),
    UrlPattern(path='/group/joined$', controller=GroupJoinedController()),
    UrlPattern(path='^/group/approval-request$', controller=GroupApprovalRequestController()),
    UrlPattern(path='^/group/leave$', controller=GroupLeaveController()),
    UrlPattern(path='^/account$', controller=AccountController()),
    UrlPattern(path='^/group/<int>/task$', controller=TaskController()),
    UrlPattern(path='^/group/<int>/task/<int>$', controller=TaskController()),
    UrlPattern(path='^/group/<int>/task/<int>/change-status$', controller=TaskChangeStatusController()),
    UrlPattern(path='^/group/<int>/task/<int>/comment$', controller=TaskCommentController()),
    UrlPattern(path='^/group/<int>/task/status-info$', controller=TaskStatusInfoController()),
]
