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

    # there is a js data array in this page that contains the index components
    # there are also a few ETF values that we will exclude from the results
    pattern = 'symbol:"(?P<ticker>[A-Z]+)"'  # magic incantation to pull ticker from js array elem 'symbol' with re named group `ticker`
    exclude = ["QQQ", "SPY", "DIA"]  # these are index funds so exclude
    # pattern = '<span class="heatmap-symbol [-0-9a-z]+">(?P<ticker>[A-Z]+)</span>'

    with urllib.request.urlopen(req) as response:
        html_content = response.read().decode("utf-8")
        # html_content = response.readlines()

    ret = []

    for match in re.finditer(pattern, html_content):
        ticker = match.groupdict()["ticker"]  # re named group as in re above
        ret.append(ticker)

    try:
        ret.remove(exclude)
    except ValueError:
        pass

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
