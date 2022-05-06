

from typing import Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.core.middleware import Middleware


class SessionMiddleware(Middleware):

    def request_process(self,
                        response: Response,
                        request: Request,
                        **kwargs) -> Tuple[bool, Response, Request, Dict]:

        # TODO:セッションIDの有無チェック

        # TODO:セッションIDからユーザ情報を取得

        return True, response, request, kwargs

    def response_process(self,
                         response: Response) -> Tuple[bool, Response]:
        return True, response
