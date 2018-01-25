# stanford_headlinez_souped: Scraping web news with Beautiful Soup

If you the [stanford_headlinez](../stanford_headlinez) assignment's notion of "web scraping" to be absurd and asinine, then good news, we'll never be parsing HTML like that again.


This assignment covers the same target -- extracting headlines from the Stanford news page. However, instead of using string `split()` methods to extract the headline text, it uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library.

## Overview


### Example usage

Assuming `bscraper.py` is in your current working directory:

```py
from answer_bscraper import fetch_hedz
url = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'

headlines = fetch_hedz(url)
for h in headlines:
  txt = '{t}\n -via {u}'.format(t=h['title'].upper(), 
                                  u=h['url'])
  print(txt)
```

Output:

```
A WINDOW INTO LONG-RANGE PLANNING
 -via https://news.stanford.edu/2018/01/16/window-long-range-planning/
3-D IMAGES OF ARTIFACTS ENRICH EXPERIENCE FOR STUDENTS, FACULTY
 -via https://news.stanford.edu/2018/01/12/3-d-images-artifacts-enrich-experience-students-faculty/
```


## Technical requirements

Your program should have a file named `bscraper.py`. 

You can download a skeleton/draft of that file, with the function names/documentation filled out, here:

[skeleton.bscraper.py](skeleton.bscraper.py)

Copy its contents and save to your working directory as `bscraper.py`.

### Dependencies

This assignment requires the use of two external (but popular) libraries:

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - for parsing HTML
- [Requests](http://docs.python-requests.org/en/master/) - for using HTTP
- [pytest](https://pytest.org/) - for running the optional test suite

These libraries come as part of the [Anaconda distribution package](https://conda.io/docs/user-guide/install/index.html) -- i.e. if you installed Python via Anaconda, you should be good to go.

If you run into any `ModuleNotFoundError` errors, it likely means that the libraries aren't yet installed on your system. You can fix it with this system shell command:


```sh
$ pip install beautifulsoup4
$ pip install requests
$ pip install pytest
```



### Test suite

The test suite for this assignment can be found in the file:

[test_bscraper.py](test_bscraper.py)

You can read the assertions and get an idea of what's expected from each function.

If you want to run it yourself locally, copy the contents of the file and save it as `test_bscraper.py`, in the same working directory as your `bscraper.py` file.

To run the test suite, simply type the following command at your system shell:

```sh
$  pytest
```


## Background information

A short primer on how to use Beautiful Soup for HTML parsing can be found here:

[CompCiv: Beautiful Soup - HTML and XML parsing](http://2017.compciv.org/guide/topics/python-nonstandard-libraries/beautifulsoup.html)

Some use-cases:

- [Using BeautifulSoup to parse HTML and extract press briefings URLs](http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/)
- [A walkthrough of HTML scraping and regexes](http://www.compjour.org/lessons/lectures/2016-04-20-basic-scrape/)

### Getting started

The popular convention for using Beautiful Soup is to import the `BeautifulSoup` class from the `bs4` namespace:

```py
from bs4 import BeautifulSoup
```

The main argument for the `BeautifulSoup()` init function is `markup` -- the text string of raw HTML to parse. However, in practice, you should be prepared to supply a second argument -- a string for the name of your system's HTML parser. Don't know what that means? Just pass in `'lxml'`.

I like using `soup` to label the BeautifulSoup object:


```py
soup = BeautifulSoup('<h1>Hello</h1><h2>world!</h2>', 'lxml')
```

`BeautifulSoup` has a large variety of [parsing/searching/traversal methods](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), but you should expect to stick to just one for the vast majority of your work: `.select()`

Some documentation here: [BS4: CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)










