# -*- coding: utf-8 -*-

"""
report_fetching
~~~~~~~~~~~~~~~~
"""
import traceback
from pprint import pprint

from scraper import Scraper
from scraper.aws.ses import Ses


if __name__ == "__main__":

    scraper_lib = Scraper()
    try:
        scraper_lib.set_cookie()
        news = scraper_lib.get_press_release()
        if '<span class="word">"霊園"</span>の検索結果は<span class="count">0</span>件です。' not in news:
            ses = Ses()
            ses.send()
            pprint('ニュースが出たよー')
        else:
            pprint('ニュースないよー')

    except:
        traceback.print_exc()

    finally:
        scraper_lib.close()
        print('end')
