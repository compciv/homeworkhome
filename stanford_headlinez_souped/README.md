# stanford_headlinez_souped: Scraping web news with Beautiful Soup


If you the [stanford_headlinez](../stanford_headlinez) assignment's notion of "web scraping" to be absurd and asinine, then good news, we'll never be parsing HTML like that again.


This assignment covers the same target -- extracting headlines from the Stanford news page. However, instead of using string `split()` methods to extract the headline text, it uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library.


<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

  - [Overview](#overview)
    - [Example usage](#example-usage)
  - [Requirements](#requirements)
    - [Functional requirements](#functional-requirements)
  - [Setup and getting started](#setup-and-getting-started)
    - [Setting up your working folder via the command-line](#setting-up-your-working-folder-via-the-command-line)
    - [Dependencies](#dependencies)
    - [Test suite](#test-suite)
  - [Background information](#background-information)
    - [Getting started with BeautifulSoup](#getting-started-with-beautifulsoup)
      - [Making our own simple HTML string](#making-our-own-simple-html-string)
      - [Importing the BeautifulSoup() class/init function](#importing-the-beautifulsoup-classinit-function)
      - [Inspecting the `soup` object](#inspecting-the-soup-object)
      - [Using the `select()` method](#using-the-select-method)
      - [How to extract the text content of a HTML tag](#how-to-extract-the-text-content-of-a-html-tag)
      - [Extracting attributes from HTML elements](#extracting-attributes-from-html-elements)
      - [Dealing with nested tags](#dealing-with-nested-tags)
      - [What's the point of `extract_headline_data()`?](#whats-the-point-of-extract_headline_data)
- [Conclusion](#conclusion)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Overview


### Example usage

Assuming `bscraper.py` is in your current working directory:

```py
from bscraper import fetch_hedz
url = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'

headlines = fetch_hedz(url)
for hed in headlines:
  print("News headline:", hed['title'])
  print("URL:", hed['url'])
  print("----")
```

Output:

```
News headline: A window into long-range planning
URL: https://news.stanford.edu/2018/01/16/window-long-range-planning/
----
News headline: 3-D images of artifacts enrich experience for students, faculty
URL: https://news.stanford.edu/2018/01/12/3-d-images-artifacts-enrich-experience-students-faculty/
----
```


## Requirements

Your program should have a file named `bscraper.py`. 

You can download a skeleton/draft of that file, with the function names/documentation filled out, here:

[skeleton.bscraper.py](skeleton.bscraper.py)

Copy its contents and save to your working directory as `bscraper.py`.

When it is finished, you should be able to run `pytest` and pass all assertions in the [test_bscraper.py](test_bscraper.py) file.


### Functional requirements

Like [the stanford_headlinez assignment](../stanford_headlinez), this one is split up into several functions to make it more digestible. The [skeleton.bscraper.py](skeleton.bscraper.py) file has the function names written out with their full definitions in the comments. 

Here's the suggested order of completion:

- `fetch_html()`: This is exactly the same as before -- given a URL, return its contents as text.
- `parse_headline_tags()`: Like before, given a `str` as argument (the HTML of a webpage), it returns a list. However, instead of a list of string objects, it returns a list of `bs4.element.Tag` objects using the **BeautifulSoup** library.
- `extract_headline_data()`: Takes a `bs4.element.Tag` object (ostensibly, one that encapsulates the HTML for a Stanford news headline) and converts it to a `dict` object.
- `fetch_hedz()`: This one is partially written for you. Complete the subfunctions so that this one returns a `list` of `dict` objects
- `print_hedz()`: This one's already written for you and should work like before, when all the other functions have been written.

## Setup and getting started

<a name="cli-setup" id="cli-setup"></a>

### From the command-line

Assuming that you are in your system shell (Terminal/PowerShell), here's how to use the command-line to download and copy the skeleton and test files quickly to your current working directory (i.e. make sure you've used `cd` to get to where you want):

**Mac OS/Linux:**

```sh
$ curl -o bscraper.py \
      https://compciv.github.io/homeworkhome/stanford_headlinez_souped/skeleton.bscraper.py

$ curl -O \
    https://compciv.github.io/homeworkhome/stanford_headlinez_souped/test_bscraper.py
```

**Windows:**

```sh
$ curl.exe -o bscraper.py `
      https://compciv.github.io/homeworkhome/stanford_headlinez_souped/skeleton.bscraper.py

$ curl.exe -O `
    https://compciv.github.io/homeworkhome/stanford_headlinez_souped/test_bscraper.py
```

Note that I've written these commands to span across a couple of lines so that they're easier to read. In Mac OS/Linux, the character to indicate a **line continuation** is the **backslash**: `\`

In Windows, it is the **backtick**: ```




### Dependencies

This assignment requires the use of two external (but popular) libraries:

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - for parsing HTML
- [Requests](http://docs.python-requests.org/en/master/) - for using HTTP
- [pytest](https://pytest.org/) - for running the optional test suite

These libraries come as part of the [Anaconda distribution package](https://conda.io/docs/user-guide/install/index.html) -- i.e. if you installed Python via Anaconda, you should be good to go.

If you run into any `ModuleNotFoundError` errors, it likely means that the libraries aren't yet installed on your system. You can fix it with this system shell command:

(use `conda` instead of `pip` if you *are* using Anaconda...)

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


- [A brief primer to HTML](http://www.compjour.org/tutorials/elements-of-a-webpage/#a-brief-primer-to-html) - you're not expected to master all the subtleties of HTML, just to understand that it is just text with a certain structure (e.g. HTML tags, open vs. closing tags, nested elements).
- [Using BeautifulSoup to parse HTML and extract press briefings URLs](http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/)



### Getting started with BeautifulSoup

As with any new library, you should test it out using *interactive Python*.


#### Making our own simple HTML string

First, we need some HTML to parse. You may think we have to download from a webpage to get some HTML. But HTML is *just text*. Which means we can construct it ourselves as any old string. Here's some legitimate HTML:

```py
>>>> htmltxt = '<h1>Hello world!</h1>'
```

Let's make it our goal to extract just the **text content** of that HTML, i.e.

```
Hello world!
```

We could do it with the string `split()` method, like we did in the [stanford_headlinez](../stanford_headlinez) assignment, e.g.  


```py
>>>> txt = htmltxt.split('>')[1].split('<')[0]
>>>> print(txt)
Hello world!
```


-- but that is **very bad practice** and you should never ever resort to such methods when dealing with HTML. HTML is a language with *specifications*, i.e. it was intended for programs, like web browsers and the **BeautifulSoup** library, to sanely parse and process, not to be hacked with string methods.

#### Importing the BeautifulSoup() class/init function

> **Note:** (I'm deliberately ignoring the definition of what a "class" or "constructor function" is because this is not meant to be a lesson about object-oriented programming...)

The popular convention for using Beautiful Soup is to import the `BeautifulSoup` class from the `bs4` namespace:

```py
>>>> from bs4 import BeautifulSoup
```

The main argument for the `BeautifulSoup()` init function is `markup` -- the text string of raw HTML to parse. However, in practice, you should be prepared to supply a second argument -- a string for the name of your system's HTML parser. Don't know what that means? Just pass in `'lxml'` as a string -- no other explanation needed other [insert shrug emoji here].

I like using `soup` as a variable name for the BeautifulSoup object:


```py
>>>> soup = BeautifulSoup(htmltxt, 'lxml')
```

Again, to reaffirm that the first argument is just a `str`, this would work too:

```py
>>>> soup = BeautifulSoup('<h1>Hello world!</h1>', 'lxml')
```


#### Inspecting the `soup` object

Use `type()` to see what kind of object it is:

```py
>>>> type(soup)
bs4.BeautifulSoup
```

If you try to inspect the contents of the `soup` object, you'll get something a bit strange:

```py
>>>> soup
<html><body><h1>Hello world!</h1></body></html>
```

For starters, that's not a `str` object, *per se*, it's just what that `bs4.BeautifulSoup` object has been designed to output when you inspect it (i.e. interactively). (this is a technicality, nothing to obsess about)...

But the big confusing thing is those extra tags that have been added to the original HTML of `<h1>Hello world!</h1>`, e.g. `<html><body>`. The short answer is that the BeautifulSoup library wants its HTML to be proper webpage HTML -- that is, inside a `<html>` and `<body>` tag, not just some disembodied `<h1>` tag all by its lonesome. For our purposes, it doesn't affect our results so we'll just live with what BeautifulSoup insists on doing...


#### Using the `select()` method



The **BeautifulSoup** object has a large variety of [parsing/searching/traversal methods](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), for getting to the element we want and to extract its properties -- in this case, the `<h1>` tag, and its *text*, i.e. `'Hello world!`.

But for the most part, the only method you need is `.select()`, which you can read about here:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors

The `.select()` method requires one argument: a `str` that describes the elements we want to capture. In this example, we want to capture all the `<h1>` elements (even though there is only one such element in our contrived simple example). 

So we pass in `h1` as the argument (i.e. *don't* include the angle-brackets):


```py
>>>> tags = soup.select('h1')
```

Even though there is just a single `<h1>` element in the example HTML we wrote, the `.select()` method always returns a list. And that list may contain just a single element, or even be completely empty, but it is still a list:

```py
>>>> type(tags)
list
>>>> tags
[<h1>Hello world!</h1>]
>>>> t = tags[0]
>>>> type(t)
bs4.element.Tag
```

#### How to extract the text content of a HTML tag

You can read about the `bs4.element.Tag` object [in the official documentation here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag). For our purposes, extracting the text is as easy as referring to the `Tag` object's `text` attribute:

```py
>>>> t.text
'Hello world!'
```

#### Extracting attributes from HTML elements

The other thing you'll need to know about HTML and tags/elements is that they can have **attributes** (again, check [out this brief primer for the basics](http://www.compjour.org/tutorials/elements-of-a-webpage/#a-brief-primer-to-html)).

The following HTML text string represents an `a` tag -- also known as an "anchor" tag, but more popularly known as a **hyperlink**:

```html
<a href="http://www.example.com" target="_blank">Hello there!</a>
```

The **text content** of this tag -- i.e. what's between `<a>` and `</a>` -- is: 

```
Hello there!
```

However, there are two **attributes**: `href`, which has a value of `"http://www.example.com`. And `target`, which has a value of `"_blank"`. Let's parse this with BS4 in Python:

(from scratch)

```py
from bs4 import BeautifulSoup
the_html = """
<a href="http://www.example.com" target="_blank">Hello there!</a>
"""

soup = BeautifulSoup(the_html, 'lxml')
tags = soup.select('a')
thetag = tags[0]
```

The `Tag` object (variable `t`) has a property named `attrs`, which returns a dictionary:

```py
>>>> type(thetag.attrs)
dict
>>>> thetag.attrs
{'href': 'http://www.example.com', 'target': '_blank'}
```

In HTML, the convention is that the `href` attribute of an `<a>` tag is the **destination** of that link, i.e. where you go when you click the link. That's all we need to complete part of this assignment -- namely the `extract_headline_data()` function, which, given a `Tag` object representing a headline nes link, returns a `dict`:

```py
>>>> d = {}
>>>> d['url'] = thetag.attrs['href']
>>>> d['title'] = thetag.text
>>>> d
{'title': 'Hello there!', 'url': 'http://www.example.com'}
```


What about that `target` attribute in the `<a>` tag? Who cares? It's not important to this assignment, but more importantly, HTML tags can have whatever attributes and values that authors want to arbitrarily add that have no (predictable) impact to us as regular browser users:

```html
<a href="http://www.example.com" dan="is cool" apples="oranges">Whatsup dude</a>
```

#### Dealing with nested tags

OK, so the HTML that we're dealing with for this assignment is not as simple as single `<a>` tags.

Take a look at the HTML in this sample snapshot of the Stanford News page:

https://wgetsnaps.github.io/stanford-edu-news/news/simple.html


Try this out in ipython:

```py
import requests
from bs4 import BeautifulSoup
url = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
```

Your first instinct to select the headline links may be this:

```py
tags = soup.select('a')
```

But you'll see that you'll collect way more HTML tags than you want (there are only **2** headlines on this sample page). So what you need to do is pick a more specific selector.

Warning: this is getting into intermediate-level HTML/Web understanding, specifically, CSS selectors, which you can read more about here:

https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors

However, to keep things simple, this is where your ability to manually inspect the HTML of a page -- i.e. the text code that makes up a "headline" -- is needed. 

Here is the HTML for *just* the anchor tag of a headline:

```html
<a href="https://news.stanford.edu/2018/01/16/window-long-range-planning/">A window into long-range planning</a>
```

But selecting for just anchor tags returns too many. How do we make our selection more specific? HTML is a language that allows for nested tags, i.e. a tag within another tag. So we look at the source code of the page to see if this `<a>` tag is itself within another HTML tag:

```html
<h3><a href="https://news.stanford.edu/2018/01/16/window-long-range-planning/">A window into long-range planning</a></h3>
```

In English, we might describe the above structure as:

> There is an `<a>` tag within a `<h3>` tag

Or:

> The `<h3>` tag has a child tag: `<a>`

How do we express that using an argument for BeautifulSoup's `.select()` method (again, here's a [primer from the BS4 docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors))?

The following notation is one way to express that we are only interested in `<a>` tags that are within `<h3>` tags:

```py
tags = soup.select('h3 a')
```

That is basically the entire functionality required of the `parse_headline_tags()` method.


#### What's the point of `extract_headline_data()`?

If you aren't too intimidated by this assignment, you might notice that the `extract_headline_data()` function seems kind of pointless, or at least extraneous. All it does is take a perfectly good `Tag` object and turn it into a `dict`.

For example, given this setup:

```py
from bs4 import BeautifulSoup
the_html = """
<h3><a href="http://www.example.com/1">Hello One</a></h3>
<h3><a href="http://www.example.com/2">Hello Two</a></h3>
"""

soup = BeautifulSoup(the_html)
tags = soup.select('h3 a')  
```

`extract_headline_data()` allows us to do this:

```py
for t in tags:
  mydict = extract_headline_data(t)
  print(mydict['url'])
  print(mydict['title'])
```

But why even make that a function? Why not just do this:


```py
for t in tags:
  print(t.attrs['href'])
  print(t.text)
```

The short answer is: *Because I said so* (as maker of this assignment). It's practice writing a function that takes in an argument and returns something. And getting used to that pattern is an important part of programming.

The big picture/real-world answer is: Because things are complicated. 

This homework assignment is relatively trivial, so it's hard to imagine why there'd be any confusion. But in a larger project, the parsing/extracting of data from HTML can be its own **module** (i.e. script file) that's being called by some other part of the program (i.e. another script file)

The other part of the program may *have no knowledge  or access to BeautifulSoup* -- pretend it was written by a totally different person who never learned about that library. That means they don't know what this means, because it requires knowing how the BeautifulSoup library works:

```py
for t in tags:
  print(t.attrs['href'])
  print(t.text)
```

However, if they are a Python programmer, they *do* know what a `dict` is. They do know to access its key/value pairs:

```py
for t in tags:
  mydict = extract_headline_data(t)
  print(mydict['url'])
  print(mydict['title'])
```

`extract_headline_data()` is a mini-example of *abstraction* and *encapsulation*, turning a library-specific object -- i.e. a **BeautifulSoup** tag -- into something more general -- e.g. a `dict`. You won't appreciate the work now, because you're writing everything in this assignment. But this strategy is important for bigger things down the road.


To put it another way, you are by now fairly familiar with the [Requests library](http://docs.python-requests.org/en/master/), and how to use it to get the text content of a page at a given URL:

```py
import requests
resp = requests.get('http://www.example.com')
print(resp.text)
```

What if the `.text` property of that `resp` object didn't return a string, but return some other complicated object? You'd have to spend time going through the [Request library's documentation](http://docs.python-requests.org/en/master/) to figure it out. But why Requests is such a popular library is that its author knew that users of his library -- i.e. me and you -- would want an easy way to get a plain ol Python string representing the contents of a page. Hence, the `.text` property.

The `extract_headline_data()` is my way of forcing you to write something that, for some hypothetical user, makes their life easier. When your `bscraper.py` is complete, that user doesn't have to know anything about HTML parsing or Beautiful Soup or whatever to get headline data.

They just call the functions in `bscraper`:

```py
from bscraper import fetch_html, parse_headline_tags, extract_headline_data 

url = 'http://web.archive.org/web/20180125102637/https://www.stanforddaily.com/'
txt = fetch_html(url)
tags = parse_headline_tags(txt)
for t in tags:
  headline = extract_headline_data(t)
  print(headline['title'], headline['url'])
```

Note: the snippet above only works because the Stanford Daily page, as archived at the [given URL](http://web.archive.org/web/20180125102637/https://www.stanforddaily.com/),  **coincidentally** has the same HTML pattern as the page at https://www.stanford.edu/news, i.e. 

```html
<h3><a href="http://url.com">Some story headline</a></h3>
```


# Conclusion

Here's a quick recap of the syntax:

```py
from bs4 import BeautifulSoup
txt = """
<h1><a href="https://google.com">Search site</a></h1>
<h1><a href="https://nytimes.com">News site</a></h1>
"""
soup = BeautifulSoup(txt, 'lxml')
for tag in soup.select('h1 a'):
    print("Link text:", tag.text)
    print("URL:", tag.attrs['href'])
    print("\n")
```

Try it out yourself to get this output:

```
Link text: Search site
URL: https://google.com


Link text: News site
URL: https://nytimes.com
```

There are many different ways to define the *selector* -- consider this variation of the above snippet: 

```py
from bs4 import BeautifulSoup
txt = """
<h1><a href="https://google.com">Search site</a></h1>
<h1><a href="https://nytimes.com">News site</a></h1>
"""
soup = BeautifulSoup(txt, 'lxml')
for tag in soup.select('h1'):
    link = tag.select_one('a')
    if link:
        print("Link text:", link.text)
        print("URL:", link.attrs['href'])
        print("\n")
```



HTML, being its own language, is enough of a topic for its own course, and web-scraping is easier when you have web development experience. But assuming you are *not* (yet) a web-developer, it's enough to understand that HTML has a hierarchal structure, and that we need to understand (at a glance) the nested structure of information when we try to *select* the parts we need.

So that's the "hard" part of web-scraping, figuring out the HTML that represents the info that we *need* for our purposes. But the good news is that, once we've done that, then a library like **BeautifulSoup** makes it easy to deal with a big ol' HTML string as a data structure.




