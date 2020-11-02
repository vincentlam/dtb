import requests
from io import StringIO


def url_to_stringio(url, **kwargs):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20200101 Firefox/82.0"
    }
    if "headers" in kwargs:
        headers.update(kwargs["headers"])
    req = requests.get(url, headers=headers)
    return StringIO(req.text)


def pd_input(uri, **kwargs):
    assert isinstance(uri, str), "uri needs to be of str type!"
    if uri.startswith("http"):
        return url_to_stringio(uri, **kwargs)
    else:
        return uri
