"""
Downloads html from UCI website
TODO: cache previous result. If download fails, send warning and return html from cache.

"""

import requests


URL_CS_ALL_REQ = 'https://www.reg.uci.edu/cob/prrqcgi?dept=COMPSCI&term=201792&action=view_all'


def get_courses_html():
    """
    Returns request.Response object only if it received a 200 success code
    http://docs.python-requests.org/en/master/api/#requests.Response
    """
    r = requests.get(URL_CS_ALL_REQ)
    if r.status_code == 200:
        return r.text
    else:
        return None


if __name__ == "__main__":
    print get_courses_html()