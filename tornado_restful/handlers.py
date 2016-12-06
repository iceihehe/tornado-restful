# -*- coding: utf-8 -*-

import tornado.web
from tornado.web import MissingArgumentError

from .constant import Code


class ApiHandler(tornado.web.RequestHandler):

    def initialize(self):

        self.set_header('Content-Type', 'application/json')

    def fail(self, code):

        self.write({'code': code, 'msg': Code.msg.get(code)})
        self.finish()

    def write_error(self, status_code, **kwargs):

        def get_exc_message(exception):

            return exception.log_message if hasattr(exception, 'log_message') else str(exception)

        exception = kwargs['exc_info'][1]

        if isinstance(exception, MissingArgumentError):
            self.set_status(400)
            self.fail(Code.MISSING_ARGUMENT)
