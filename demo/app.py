# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop

from tornado_restful import ApiHandler, reqparse


parser = reqparse.RequestParser()
parser.add_argument('a', location='args', type_=int)
parser.add_argument('b', location='args')


class MainHandler(ApiHandler):
    def get(self, *args, **kwargs):

        req = parser.parse_args(self.request)
        self.write(req)

    def post(self, *args, **kwargs):
        print(self.request.body)
        print(self.request.arguments)
        print(self.request.query_arguments)
        print(self.request.body_arguments)
        self.write('success')


def make_app():
    return tornado.web.Application(
        handlers=[(r"/", MainHandler),],
        debug=True,
    )


if __name__ == '__main__':

    app = make_app()
    app.listen(5005)
    tornado.ioloop.IOLoop.current().start()
