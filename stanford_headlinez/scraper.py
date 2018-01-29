import requests
HEADLINE_PATTERN = '<h3><a'
OFFICAL_NEWS_URL = 'https://www.stanford.edu/news/'
SAMPLE_NEWS_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'


def print_hedz(url=OFFICAL_NEWS_URL):
    hedtags = parse_headline_tags(fetch_html(url))

    for h in hedtags:
        hedtxt = extract_headline_text(h)
        print(hedtxt)


def extract_headline_text(txt):
    a = txt.split('<')[2]
    b = a.split('>')[1]
    return b


def parse_headline_tags(txt):
    hedtags = []
    lines = txt.splitlines()
    """
    # or, if you like list comprehensions:
    return [k for k in lines if HEADLINE_PATTERN in k]
    """
    for line in lines:
        if HEADLINE_PATTERN in line:
            hedtags.append(line)
    return hedtags



def fetch_html(url):
    return requests.get(url).text

