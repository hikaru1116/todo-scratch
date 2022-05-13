from todo_scratch.bk_app.handlers.group_handler import GroupHandler
from todo_scratch.bk_app.validators.request_body_validators.create_group_validator import CreateGroupValidator
from todo_scratch.bk_base.controller.controller import Controller
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.http_error_response import Response404
from todo_scratch.bk_base.http.response.response import Response


class GroupController(Controller):

    def post(self, request: Request, **kwargs) -> Response:
        body = request.json

        validator = CreateGroupValidator(body)
        if not validator.validate():
            return Response404()

        request_body = validator.result
        print(request_body)
        return Response()

    def get_handler(self):
        return GroupHandler()
