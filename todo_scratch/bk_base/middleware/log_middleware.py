

from typing import Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.middleware.middleware import Middleware


class LogMiddleware(Middleware):

    def request_process(self,
                        response: Response,
                        request: Request,
                        **kwargs) -> Tuple[Response, Request, Dict]:
        print("request log middleware")

        tmp_response = Response(body="log middleware")
        return tmp_response, request, kwargs

    def response_process(self,
                         response: Response) -> Tuple[bool, Response]:
        print("response log middleware")
        return True, response
