import urllib.request
import re


hdr = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}


def get_spx_components() -> list[str]:

    url = "https://www.slickcharts.com/sp500"
    return _get_components(url)


def get_ndq_components() -> list[str]:

    url = "https://www.slickcharts.com/nasdaq100"
    return _get_components(url)


def _get_components(url: str) -> list[str]:

    req = urllib.request.Request(url, headers=hdr)

    pattern = 'symbol:"(?P<ticker>[A-Z]+)"'

    # pattern = '<span class="heatmap-symbol [-0-9a-z]+">(?P<ticker>[A-Z]+)</span>'

    with urllib.request.urlopen(req) as response:
        html_content = response.read().decode("utf-8")
        # html_content = response.readlines()

    ret = []

    exclude = ["QQQ", "SPY", "DIA"]
    for match in re.finditer(pattern, html_content):
        ticker = match.groupdict()["ticker"]
        if ticker not in exclude:
            ret.append(ticker)

    return ret


tickers = get_ndq_components()

fred = set(tickers)

print(tickers)

print(len(tickers))
tickers = get_spx_components()

fred.update(tickers)

print(tickers)

print(len(tickers))


print(len(fred))
