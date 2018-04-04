# -*- coding:utf-8 -*-

__author__ = 'HeZhao'

'''
自定义Web框架
'''

import logging; logging.basicConfig(level=logging.DEBUG)
import functools


def get(path):
    '''
    Define decorator @get('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            return func(*args, **kw)
        wapper.__method__ = 'GET'
        wapper.__route__ = path
        return wapper
    return decorator

def post(path):
    '''
    Define decorator @get('/path')
    :param path:
    :return:
    '''
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            return func(*args, **kw)
        wapper.__method__ = 'GET'
        wapper.__route__ = path
        return wapper
    return decorator

class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn

    async def __call__(self, request):
        kw = request
        r = await self._func(**kw)
        return r

