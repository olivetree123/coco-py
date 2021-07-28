# coco

coco is an asynchronous web framework for python


## Tutorial
```python
from coco import Resource, Route, Coco


class HomeEndpoint(Resource):
    async def get(self, request):
        return {"name": "olivetree123"}


class HelloEndpoint(Resource):
    async def get(self, request, name):
        return {"say": "hello " + name}


route = Route()
route.register(HomeEndpoint, "/")
route.register(HelloEndpoint, "/hello/{name}")
app = Coco(route=route)
```
