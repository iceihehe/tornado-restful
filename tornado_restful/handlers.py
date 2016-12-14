# -*- coding: utf-8 -*-

import tornado.web


class ApiHandler(tornado.web.RequestHandler):

    def initialize(self):

        self.set_header('Content-Type', 'application/json')
