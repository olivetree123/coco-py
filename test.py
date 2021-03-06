from paopao import Paopao, Resource, Route


class HomeEndpoint(Resource):
    decorators = []

    async def get(self, request):
        return {"name": "gaojian"}

    async def post(self):
        pass


class HelloEndpoint(Resource):
    async def get(self, request, name):
        return {"say": "hello " + name}


route = Route()
route.register(HomeEndpoint, "/")
# route.register(HomeEndpoint, "/home")
route.register(HelloEndpoint, "/hello/{name}/what")
app = Paopao(route=route)
