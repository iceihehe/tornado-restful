# -*- coding: utf-8 -*-

import tornado.httputil
import tornado.escape


class ApiRequest(tornado.httputil.HTTPServerRequest):

    __attributes = {'request', 'json'}

    def __init__(self, request):

        self.request = request

    def __getattr__(self, name):

        if name in self.__attributes:
            return self.__attributes[name]
        else:
            return getattr(self.request, name)

    @property
    def json(self):

        return tornado.escape.json_decode(self.request.body)

    @property
    def args(self):

        return self.request.query_arguments

