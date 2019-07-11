# -*- coding: utf-8 -*-

import requests
import tempfile
import json


class HttpClient:

    TEMPSACK = None

    def __init__(self):
        self.TEMPSACK = tempfile.NamedTemporaryFile(delete=False)

    def post_save_cookie(self, **params):
        session = self._create_session()
        response = session.post(**params)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        self._store_cookies(cookiejar=requests.utils.dict_from_cookiejar(session.cookies))
        return response.text

    def post(self, **params):
        session = self._create_session()
        response = session.post(**params)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return response.text

    def get_save_cookie(self, **params):
        session = self._create_session()
        response = session.get(**params)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        self._store_cookies(cookiejar=requests.utils.dict_from_cookiejar(session.cookies))
        return response.text

    def get(self, **params):
        session = self._create_session()
        response = session.get(**params)
        response.encoding = response.apparent_encoding
        response.raise_for_status()
        return response.text

    def _store_cookies(self, cookiejar):
        tfpath = self.TEMPSACK.name
        fp = open(tfpath, 'w')
        fp.write(json.dumps(cookiejar))
        fp.seek(0)
        self.TEMPSACK.close()

    def fetch_cookies(self):
        tfpath = self.TEMPSACK.name
        fp = open(tfpath, 'r')
        cookies = fp.read()
        self.TEMPSACK.close()
        return cookies

    def _create_session(self):
        session = requests.sessions.Session()
        return session

    def close(self):
        self.TEMPSACK.close()
