# coding=utf-8

_global_dict = {}


class GlobalVar(object):
    def __init__(self):
        global _global_dict
        _global_dict = {}

    @staticmethod
    def set_value(name, value):
        _global_dict[name] = value

    @staticmethod
    def get_value(name):
        try:
            return _global_dict[name]
        except KeyError:
            return None
