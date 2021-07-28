class Request(object):
    def __init__(self, **kwargs):
        self.path = kwargs.get("path")
        self.method = kwargs.get("method")
        self.query_string = kwargs.get("query_string")
        self.headers = {}
        for header in kwargs.get("headers"):
            self.headers[str(header[0])] = str(header[1])

    def query_params(self):
        params = {}
        for param in self.query_params.split("&"):
            key, value = param.split("=")
            params[key] = value
        return params

    def json_params(self):
        pass

    def form_params(self):
        pass
