#-*- coding: utf-8 -*-
u'''
Solution exercise 2: MRO: super and getattr
'''
from datetime import datetime


class Verbose(object):
    def __getattribute__(self, name):
        print "__getattribute__", name
        return super(Verbose, self).__getattribute__(name)

    def __getitem__(self, key):
        print "__getitem__", key
        return super(Verbose, self).__getitem__(key)

    def __setitem__(self, key, value):
        print "__setitem__", key, value
        return super(Verbose, self).__setitem__(key, value)

    def __getattr__(self, name):
        print "__getattr__", name
        return super(Verbose, self).__getattr__(name)

    def __setattr__(self, name, value):
        print "__setattr__", name, value
        return super(Verbose, self).__setattr__(name, value)


class Lower(object):
    def __getattribute__(self, name):
        return super(Lower, self).__getattribute__(name.lower())

    def __getitem__(self, key):
        return super(Lower, self).__getitem__(key.lower())

    def __setitem__(self, key, value):
        if isinstance(value, (str, unicode)):
            value = value.lower()
        return super(Lower, self).__setitem__(key.lower(), value)

    def __getattr__(self, name):
        return super(Lower, self).__getattr__(name.lower())

    def __setattr__(self, name, value):
        if isinstance(value, (str, unicode)):
            value = value.lower()
        return super(Lower, self).__setattr__(name.lower(), value)

    def __contains__(self, item):
        return super(Lower, self).__contains__(item.lower())


class Attr(object):
    def __getattr__(self, name):
        try:
            return super(Attr, self).__getitem__(name)
        except KeyError, e:
            raise AttributeError(e)

    def __setattr__(self, name, value):
        if name in self:
            super(Attr, self).__setitem__(name, value)
        else:
            super(Attr, self).__setattr__(name, value)


class DateStr(object):
    def __setitem__(self, key, value):
        if isinstance(value, datetime):
            value = value.isoformat()
        return super(DateStr, self).__setitem__(key, value)

    def __setattr__(self, name, value):
        if isinstance(value, datetime):
            value = value.isoformat()
        return super(DateStr, self).__setattr__(name, value)


class AmazingDict(Attr, Lower, DateStr, Verbose, dict):
    pass
