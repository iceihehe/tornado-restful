# -*- coding: utf-8 -*-

import tornado.web


class ApiHandler(tornado.web.RequestHandler):

    def initialize(self):

        self.set_header('Content-Type', 'application/json')

    def fail(self, msg):

        self.write({'msg': msg})
        self.finish()

    def write_error(self, status_code, **kwargs):

        def get_exc_message(exception):

            return exception.log_message if hasattr(exception, 'log_message') else str(exception)

        exception = kwargs['exc_info'][1]

        if status_code == 500:
            self.fail('System error')

        else:
            self.fail(get_exc_message(exception))
