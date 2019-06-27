#!/usr/bin/env python
import falcon
import threading
import time

class VarResource:
    def on_get(self, req, resp):
        try:
            with open('/etc/config/magic', 'r') as f:
                magic = f.readline().strip()
        except FileNotFoundError:
            magic = '#ERROR'
        obj = {'todays_magic_word': magic}
        resp.media = obj


class ConstResource:
    def on_get(self, req, resp):
        try:
            with open('/etc/config/const', 'r') as f:
                magic = f.readline().strip()
        except FileNotFoundError:
            magic = '#ERROR'
        resp.media = magic


class TimeResource:
    def on_get(self, req, resp):
        try:
            with open('/etc/config/time', 'r') as f:
                magic = f.readline().strip()
        except FileNotFoundError:
            magic = '#ERROR'
        resp.media = magic

api = falcon.API()
api.add_route('/magic', VarResource())
api.add_route('/const', ConstResource())
api.add_route('/time', TimeResource())
