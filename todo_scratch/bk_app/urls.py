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
from todo_scratch.bk_app.controllers.task_detail_conttroller import TaskDetailController
from todo_scratch.bk_app.controllers.task_divide_by_status_controller import TaskDivideByStatusController
from todo_scratch.bk_app.controllers.task_status_info_controller import TaskStatusInfoController
from atom_bk_frame.core.url_pattern import UrlPattern

urlpatterns: t.List[UrlPattern] = [
    UrlPattern(path='/api/$', controller=HelloController()),
    UrlPattern(path='/api/authorized', controller=AuthorizedController()),
    UrlPattern(path='/api/forbidden', controller=ForbddenController()),
    UrlPattern(path='/api/group$', controller=GroupController()),
    UrlPattern(path='/api/group/<int>$', controller=GroupController()),
    UrlPattern(path='/api/group/joined$', controller=GroupJoinedController()),
    UrlPattern(path='/api/group/approval-request$', controller=GroupApprovalRequestController()),
    UrlPattern(path='/api/group/leave$', controller=GroupLeaveController()),
    UrlPattern(path='/api/account$', controller=AccountController()),
    UrlPattern(path='/api/group/<int>/task$', controller=TaskController()),
    UrlPattern(path='/api/group/<int>/task/<int>$', controller=TaskController()),
    UrlPattern(path='/api/group/<int>/task/divide-by-status', controller=TaskDivideByStatusController()),
    UrlPattern(path='/api/group/<int>/task/<int>/detail$', controller=TaskDetailController()),
    UrlPattern(path='/api/group/<int>/task/<int>/change-status$', controller=TaskChangeStatusController()),
    UrlPattern(path='/api/group/<int>/task/<int>/comment$', controller=TaskCommentController()),
    UrlPattern(path='/api/group/<int>/task/status-info$', controller=TaskStatusInfoController()),
]
