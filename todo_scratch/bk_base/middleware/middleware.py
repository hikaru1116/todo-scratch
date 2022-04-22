from abc import ABCMeta, abstractclassmethod
from typing import Dict, Tuple
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response


class MiddlewareProcess():

    def __init__(self, callback, middleware) -> None:
        self.callback = callback
        self.middleware: Middleware = middleware

    def middleware_process(self,
                           request: Request,
                           **kwargs) -> Response:

        initial_response = None
        print('kokomade')
        response, request, kwargs = self.middleware.request_chain(initial_response, request, **kwargs)

        if response is not None:
            return response

        response = self.callback(request, **kwargs)

        return self.middleware.response_chain(response)


class Middleware(metaclass=ABCMeta):
    # def __init__(self) -> None:
    #     self.next: Middleware = None

    def set_next(self, next) -> None:
        self.next = next
        return next

    def request_chain(self,
                      response: Response,
                      request: Request,
                      **kwargs) -> Tuple[Response, Request, Dict]:
        response, request, kwargs = self.request_process(response, request, **kwargs)

        if response is not None:
            return response

        if getattr(self, "next", None) is None:
            return response, request, kwargs
        else:
            return self.next.request_chain(response, request, **kwargs)

    def response_chain(self, response: Response) -> Response:

        is_break, response = self.response_process(response)

        if is_break or self.next is None:
            return response
        else:
            return self.next.response_chain(response)

    @abstractclassmethod
    def request_process(self,
                        response: Response,
                        request: Request,
                        **kwargs) -> Tuple[Response, Request, Dict]:
        return response, request, kwargs

    @abstractclassmethod
    def response_process(self,
                         response: Response) -> Tuple[bool, Response]:
        return True, response
