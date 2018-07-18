#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
import requests


class EthJsonRpc(object):

    def __init__(self, url):
        self.url = url
        self.id = 1
        self.session = requests.session()

    def call(self, method, params=None):

        params = params or []
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': self.id,
        }
        headers = {'Content-Type': 'application/json'}
        resp = self.session.post(self.url, headers=headers, json=data)

        self.id += 1
        return resp.json()
