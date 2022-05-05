from typing import Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.core.middleware import Middleware
from todo_scratch.bk_base.util.settings_util import get_member_by_settings


class CorsMiddleware(Middleware):

    def request_process(self,
                        response: Response,
                        request: Request,
                        **kwargs) -> Tuple[bool, Response, Request, Dict]:

        return True, response, request, kwargs

    def response_process(self,
                         response: Response) -> Tuple[bool, Response]:
        print("Response", "CorsMiddleware")
        access_control_allo_origins = get_member_by_settings("ACCESS_ALLOW_ORIGIN")
        response.add_headers(
            {
                "Access-Control-Allow-Origin": ",".join(access_control_allo_origins),
                "Access-Control-Allow-Headers": "X-Requested-With, X-HTTP-Method-Override, Content-Type, Accept"
            }
        )
        return True, response
