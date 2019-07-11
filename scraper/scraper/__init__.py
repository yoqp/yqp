# -*- coding: utf-8 -*-

import json

from scraper.libs.http_client import HttpClient


class Scraper:

    def __init__(self):
        self.http = HttpClient()

    def set_cookie(self):
        self.http.get_save_cookie(
            url="https://search.metro.tokyo.lg.jp",
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
            }
        )

    def get_press_release(self):
        cookies = json.loads(self.http.fetch_cookies())
        params = {
            "filetype": "",
            "start_dt": "20190501",
            "end_dt": "20190531",
            "end_year": "2019",
            "end_month": "05",
            "CATEGORY_press_category": "募集",
            "start_year": "2019",
            "start_month": "05",
            "kw": "霊園",
            "pm_flg": "あいまい",
            "sitesearch": "www.metro.tokyo.jp/tosei/hodohappyo/press",
            "requiredfields": "",
            "temp": "JP",
            "ie": "u",
            "ord": "t"
        }

        return self.http.get(
            url='https://search.metro.tokyo.lg.jp/',
            params=params,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
            }
        )

    def close(self):
        self.http.close()
