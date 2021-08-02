# paopao

paopao is an asynchronous web framework for python


## Tutorial
```python
from paopao import Paopao, Resource, Route


class HomeEndpoint(Resource):
    async def get(self, request):
        return {"name": "olivetree123"}


class HelloEndpoint(Resource):
    async def get(self, request, name):
        return {"say": "hello " + name}


route = Route()
route.register(HomeEndpoint, "/")
route.register(HelloEndpoint, "/hello/{name}")
app = Paopao(route=route)
```

## Run
```shell
uvicorn main:app
```
