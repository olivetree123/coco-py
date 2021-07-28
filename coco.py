import json
from typing import List
from route import Route
from request import Request


class Resource(object):
    def __init__(self):
        pass


class Coco(object):
    def __init__(self, route: Route = None):
        self.route = route

    async def init(self, **kwargs):
        if kwargs.get("route"):
            route = kwargs.get("route")
            if not isinstance(route, Route):
                raise TypeError("route should be type of Route")
            self.route = route

    async def _dispatch(self, path, method):
        handler_class, params = self.route.find(path)
        if not handler_class:
            return None, params
        handler_obj = handler_class()
        return getattr(handler_obj, method.lower()), params

    async def __call__(self, scope, receive, send):
        assert scope['type'] == 'http'
        request = Request(**scope)
        handler, params = await self._dispatch(
            path=request.path,
            method=request.method,
        )
        if not handler:
            await self.response_error(send, 404)
            return
        response = await handler(request=request, **params)
        await self.response_ok(send,
                               bytes(json.dumps(response), encoding="utf8"))

    async def response_error(self, send, code):
        body = b"404 Not Found"
        await send({
            'type': 'http.response.start',
            'status': code,
            'headers': [
                [b'content-type', b'text/html'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': body,
        })

    async def response_ok(self, send, response):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'application/json'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': response,
        })
