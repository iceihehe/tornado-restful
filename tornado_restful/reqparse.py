# -*- coding: utf-8 -*-

class Namespace(dict):
    """字典的类属性访问"""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value
