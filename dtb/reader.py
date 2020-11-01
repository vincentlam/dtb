import requests
from io import StringIO


def pd_input(uri, **kwargs):
    assert isinstance(uri, str), "uri needs to be of str type!"
    if uri.startswith("http"):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"
        }
        if "headers" in kwargs:
            headers.update(kwargs["headers"])
        req = requests.get(uri, headers=headers)
        return StringIO(req.text)
    else:
        return uri
