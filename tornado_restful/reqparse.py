# -*- coding: utf-8 -*-

import collections
import six

from .utils import ApiRequest


text_type = lambda x: six.text_type(x) if not isinstance(x, bytes) else six.text_type(x.decode())


class Namespace(dict):
    """字典的类属性访问"""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value


class Argument(object):

    def __init__(self, name, location='args', type_=text_type, default=None, store_missing=True):
        self.name = name
        self.location = location
        self.type = type_
        self.default = default
        self.store_missing = store_missing

    def source(self, request):
        value = getattr(request, self.location, None)
        if callable(value):
            value = value()
        if value is not None:
            return value

    def convert(self, value):

        return self.type(value)


    def parse(self, request):

        source = self.source(request)

        results = []

        _not_found = False
        _found = True

        name = self.name
        if name in source:
            values = source.get(name)
            if not isinstance(values, collections.MutableSequence):
                values = [values]

            for value in values:
                value = self.convert(value)

                results.append(value)
        if not results:
            if callable(self.default):
                return self.default(), _not_found
            else:
                return self.default, _not_found

        if len(results) == 1:
            return results[0], _found
        return results, _found


class RequestParser(object):

    def __init__(self, argument_class=Argument, namespace_class=Namespace):
        self.args = []
        self.argument_class = argument_class
        self.namespace_class = namespace_class

    def add_argument(self, *args, **kwargs):
        self.args.append(self.argument_class(*args, **kwargs))
        return self

    def parse_args(self, request):

        namespace = self.namespace_class()
        api_request = ApiRequest(request)

        for arg in self.args:
            value, found = arg.parse(api_request)
            if found or arg.store_missing:
                namespace[arg.name] = value

        return namespace
