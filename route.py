from typing import List


class RulePart(object):
    def __init__(self, val):
        self.val = val
        self.param_name = None
        if self.is_param():
            self.param_name = self.val[1:-1]

    def is_param(self):
        if self.val[0] == "{" and self.val[-1] == "}":
            return True
        return False

    def match(self, part):
        if self.val == part.val:
            return True
        return False


def path_to_parts(path) -> RulePart:
    return [RulePart(p) for p in path.split("/") if p]


class Rule(object):
    def __init__(self, handler, path):
        self.path = path
        self.parts: List[RulePart] = path_to_parts(path)
        self.handler = handler

    def match(self, path):
        params = {}
        ps = path_to_parts(path)
        if not len(ps) == len(self.parts):
            return False, params
        for i in range(len(ps)):
            if self.parts[i].is_param():
                name = self.parts[i].param_name
                params[name] = ps[i].val
                continue
            if not self.parts[i].match(ps[i]):
                return False, params
        return True, params


class Route(object):
    def __init__(self):
        self.rules: List[Rule] = []

    def register(self, handler, url):
        rule = Rule(handler, url)
        self.rules.append(rule)

    def find(self, path):
        for rule in self.rules:
            is_match, params = rule.match(path)
            if is_match:
                return rule.handler, params
        return None, None
