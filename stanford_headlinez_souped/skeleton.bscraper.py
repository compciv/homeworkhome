import requests
from bs4 import BeautifulSoup

OFFICIAL_URL='https://www.stanford.edu/news/'
SAMPLE_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'

def fetch_hedz(url=OFFICIAL_URL):
    """
    Extracts headline objects (with 'url' and 'title' attributes)
        from pages styled like the one found at OFFICIAL_URL

    Args:
        url (str): a URL to visit and read and parse HTML

    Returns:
        list: a sequence of dict objects, each one containing the
            'url' and 'title' data extracted from the HTML, e.g.
            [
                {
                 'url': 'https://www.stanford.edu/news/2018/etc',
                 'title': 'Stanford News Story About Things'
                }
            ]
    """
    txt = fetch_html(url)
    tags = parse_headline_tags(txt)
    # headlines is an empty list for appending things
    # return it at the end
    headlines = []

    ###
    # You do the rest!
    #
    # iterate through the `tags`
    # for each tag,
    #     do something to it (use one of the functions that you've had to write)
    #     append the result to `headlines`
    ###
    return headlines


def extract_headline_data(tag):
    """
    Extracts data of the headline from a
        BeautifulSoup Tag object and repackages it
        as a dict.

        The data elements are:
        - title (str)
        - url (str)

    Args:
        tag (bs4.element.Tag): in other words, this
            function is only used after HTML has been
            turned into soup.

    Returns:
        dict: contains only two key-value pairs: 'url', 'title'

        Example:
            {
             'url': 'https://www.stanford.edu/news/2018/etc',
             'title': 'Stanford News Story About Things'
            }
    """



def fetch_html(url):
    """
    This function performs a GET request on the given
      URL and returns the content (typically, HTML)
      as a string


    Args:
        url (str): e.g. 'http://www.example.com'

    Returns:
        str: the data at `url`, as text
    """


def parse_headline_tags(txt):
    """
    Extracts the news headlines from the HTML on the
      Stanford.edu News homepage. Uses the BeautifulSoup
      library.

    Args:
        txt (str): HTML, as plaintext

    Returns:
        list: A sequence of bs4.element.Tag-type objects
    """


##################################### Already done



def print_hedz(url=OFFICIAL_URL):
    """
    A throwback function to when all we cared about was
      printing plaintext to output
    """
    headlines = fetch_hedz(url)
    for hed in headlines:
        print(hed['title'])
