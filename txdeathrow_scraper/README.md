# txdeathrow_scraper

This assignment is a continuation of [txdeathrow_check](../txdeathrow_check), but instead of just counting items in a list (i.e. BS4 table row elements), we convert each table row into a Python dictionary, which can be serialized into a data format (CSV/JSON) or used by another Python program.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*


- [Overview](#overview)
- [Requirements](#requirements)
  - [Example usage](#example-usage)
  - [Functional requirements](#functional-requirements)
- [Setup and getting started](#setup-and-getting-started)
  - [Using Python](#using-python)
  - [Running the tests](#running-the-tests)
- [Walkthrough/Guide](#walkthroughguide)
  - [format_helper.py walkthrough](#format_helperpy-walkthrough)
    - [Resolving relative URLs given a source URL with `make_absolute_url()`](#resolving-relative-urls-given-a-source-url-with-make_absolute_url)
    - [Converting a datestring format to ISO format with `txdate_to_iso()`](#converting-a-datestring-format-to-iso-format-with-txdate_to_iso)
      - [Messy dates](#messy-dates)
    - [Finding the amount of time between two dates with `calc_years_diff()`](#finding-the-amount-of-time-between-two-dates-with-calc_years_diff)
  - [scraper.py walkthrough](#scraperpy-walkthrough)
    - [Extracting each inmate row with `get_and_parse_inmate_rows()`](#extracting-each-inmate-row-with-get_and_parse_inmate_rows)
    - [Extracting each "column"](#extracting-each-column)
    - [What's the deal with extra whitespace and `.strip()`?](#whats-the-deal-with-extra-whitespace-and-strip)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Overview

A follow up/add-on to [txdeathrow_check](../txdeathrow_check). We build upon our scraper for the [Death Row Information Homepage of the Texas Department of Criminal Justice](https://www.tdcj.state.tx.us/death_row/), specifically, the [Offenders on Death Row page](https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html), except this time, we turn it into usable data objects (a list of dictionaries)


Again we use this mirror:

https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html

And we use some of the code we wrote for [txdeathrow_check](../txdeathrow_check)

## Requirements

### Example usage

For `scraper.py`, if you've completed the `get_and_parse_inmate_rows()` function, then the `get_inmate_data()` function can be used like this:


```py
from scraper import get_inmate_data
inmates = get_inmate_data()
print("There are currently", len(inmates), "inmates listed on Texas's death row.")
i = inmates[0]
print(i['url'])
print(i['date_offense'])
print(i['age_at_offense'])
```

And get output that looks like this:

```
There are currently 232 inmates listed on Texas's death row.
https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/hudsonwilliam.html
2015-11-14
33
```


Or, we could even do calculations like these:

```py
from scraper import get_inmate_data
import numpy

inmates = get_inmate_data()
ages = [i['age_at_offense'] for i in inmates]
print("Stats about inmate ages when convicted:")
print("Average:", round(numpy.mean(ages), 1))
print("Median:", numpy.median(ages))
print("Youngest:", numpy.min(ages))
print("Oldest:", numpy.max(ages))
```


Expected output:

```
Stats about inmate ages when convicted:
Average: 28.1
Median: 26.0
Youngest: 18
Oldest: 52
```



### Functional requirements

There are 3 function definitions in [scraper.py](starter/scraper.py):


- `get_inmate_data()` - is already written for you
- `get_and_parse_inmate_rows()` - you can use the exact same thing as last assignment
- `wrangle_inmate_data_from_tag()` - this is what you have to fill out 

There are 3 function definitions in [format_helper.py](starter/format_helper.py) -- all of them you'll fill out

- `txdate_to_iso()`
- `calc_years_diff()`
- `make_absolute_url()`


The [data_helper.py](starter/data_helper.py) file is provided to you -- it basically just takes care of downloading from the webpage if needed. The only function you need to use from `data_helper.py` is `get_html()`, which returns the raw text of the death penalty webpage.


In the end, this is what your working directory should look like (including the tests subdirectory is optional):

```
  ├── data_helper.py
  ├── format_helper.py
  ├── scraper.py
  └── tests/
      ├── test_calc_years_diff.py
      ├── test_make_absolute_url.py
      ├── test_scraper.py
      ├── test_txdate_to_iso.py
      └── test_wrangle_inmate_data.py
```




### Running the tests

There are 5 tests in the [tests/][tests] subdirectory. As always, you can run them all like this using **pytest** from the command-line:

```sh
$ pytest
```

However, I wouldn't run all the tests at once until you've actually finished the homework -- i.e. seeing dozens of failure messages can be overwhelming. Instead, try running tests one test file, or one test at a time.

To run one test file at a time, refer to the full filename (use Tab to do autocomplete), e.g.

```sh
$ pytest tests/test_txdate_to_iso.py
```

If you know the *name* of the test, i.e. the name assertion function, e.g. 'test_conversion_to_iso_format' for the following  test function:

```py
def test_conversion_to_iso_format():
    """
    Make sure it converts something in MM/DD/YYYY
     to: YYYY-MM-DD
    """
    assert txdate_to_iso('05/11/1977') == '1977-05-11'
```

Pass in the partial name using the `-k` flag -- note how I only need a partial name, and no reference to the specific file:


```sh
$ pytest -k 'conversion_to_iso_format'
```


## Setup and getting started

<a name="cli-setup" id="cli-setup"></a>

### From the command-line


For your convenience, instead of making you copy-paste a series of `curl` commands, which are getting quite numerous, I've included in this repo a file named `setup_hw.py`, which you can view at a [browser-friendly URL here](setup_hw.py).

Or, you can access as a direct URL (which is useful for `curl`:)

https://compciv.github.io/homeworkhome/txdeathrow_scraper/setup_hw.py

e.g. for Mac OS:

```sh
$ curl -o setup_hw.py \
    https://compciv.github.io/homeworkhome/txdeathrow_scraper/setup_hw.py

```

and Windows PowerShell:

```
$ curl.exe -o setup_hw.py `
    https://compciv.github.io/homeworkhome/txdeathrow_scraper/setup_hw.py
```

And to execute that script -- you know how to do this:

```sh
$ python setup_hw.py
```

My script does what you've done before, fetch files from online and save to your current working directory, this includes [scraper.py](starter/scraper.py) and  all the tests in ther `tests` subdirectory. Except the commands to do this work is in **Python**, not Bash/Powershell, and it's all in a single script that can be downloaded with a single `curl` command and then run like any other Python script.

All together for Mac/Linux (adjust as needed for Windows):

```sh
$ curl -o setup_hw.py \
  https://compciv.github.io/homeworkhome/txdeathrow_scraper/starter/setup_hw.py

$ python setup_hw.py
```


### Moving from shell commands to Python scripts

Why move from shell scripts to Python -- or more accurately, doing everything in a Python script, and then running that script via a shell command? Because all those `curl` commands to download multiple files should have looked messy to you, nevermind the differences between Windows and Mac OS. 

Using Python let's us be platform agnostic, while putting everything in a single, easy-to-view Python file, while letting us practice Python coding in general. You can view the `setup_hw.py` on this Github repo at [starter/setup_hw.py](starter/setup_hw.py)

Read on for the details of the Python code.


#### Using curl to download a file to a specific local file path

As a reminder, here is the shell command to download a file and save it to disk (in Mac OS/Linux):

```sh
$ curl -o data_helper.py \
    https://compciv.github.io/homeworkhome/txdeathrow_scraper/data_helper.py
```

The `curl` above command does 2 things:

- Downloads the following URL: https://compciv.github.io/homeworkhome/txdeathrow_scraper/data_helper.py
- Directs the content of what's downloaded to the *relative* filename of `data_helper.py` -- "relative" to your current working directory.

#### Using many lines of Python to download a file to a specific local file path

Here's that same process in Python, using the Requests library:

```py
import requests
from pathlib import Path

src_url = 'https://compciv.github.io/homeworkhome/txdeathrow_scraper/data_helper.py'
dest_path = Path('data_helper.py')

resp = requests.get(src_url)
txt = resp.text
dest_path.write_text(txt)
```

It's a lot more *stuff* to do in Python what we did via shell commands -- just like it's a lot more *stuff* to do in shell commands what we did by point-and-click to download via the browser. 

This is because scripting in Python is "lower" level -- more granular -- than system shell commands. The advantage can be seen when we need to do more granular operations (maybe print a helpful debug message with each action), or when what we're doing is very repetitive.

For example, this assignment involves not 1 but **five** separate test files, which you can see on Github here:

https://github.com/compciv/homeworkhome/tree/master/txdeathrow_scraper/tests

Or as direct download links:

- https://compciv.github.io/homeworkhome/txdeathrow_scraper/test_calc_years_diff.py
- https://compciv.github.io/homeworkhome/txdeathrow_scraper/test_make_absolute_url.py
- https://compciv.github.io/homeworkhome/txdeathrow_scraper/test_scraper.py
- https://compciv.github.io/homeworkhome/txdeathrow_scraper/test_txdate_to_iso.py
- https://compciv.github.io/homeworkhome/txdeathrow_scraper/test_wrangle_inmate_data.py

We know how to do this in the shell using `curl`, write multiple `curl` statements for each URL. 

Here's one way to write the test-downloading code in Python. It's verbose, but we have the flexibility to do things like break up the really long URLs into separate variables/components, and to set up the filepaths that are being downloaded to, e.g. create the subdirectory `tests`:


```py
from pathlib import Path
import requests

GH_DOMAIN = 'https://compciv.github.io'
GH_PATH = 'homeworkhome/txdeathrow_scraper'
GH_BASE = GH_DOMAIN + '/' + GH_PATH

TEST_BASENAMES = ['test_calc_years_diff.py',
  'test_make_absolute_url.py',
  'test_scraper.py',
  'test_txdate_to_iso.py',
  'test_wrangle_inmate_data.py',
]

TESTS_PATH = Path('tests')
# make subdirectory, if it doesn't exist
TESTS_PATH.mkdir(exist_ok=True)

for fname in TEST_BASENAMES:
   _uparts = [GH_BASE, 'tests', fname]
   url = '/'.join(_uparts)   
   print('-----------------')
   print("Downloading from:\n", url)
   resp = requests.get(url)

   dest_path = TESTS_PATH.joinpath(fname)
   print("-- Saving to:", dest_path)
   dest_path.write_text(resp.text)
```

Take a look at [startup/setup_hw.py](startup/setup_hw.py) to see the source code. There's some fanciness I've added but you should see the core code of downloading/saving to a file and (someday) aspire to write it on your own.

For the purposes of setting up this exercise, just copy the contents of [startup/setup_hw.py](startup/setup_hw.py) into a Python script in the directory you want to be working in locally (i.e. probably not `startup/`), and then run:

```sh
$ python startup/setup_hw.py
```





## Walkthrough/Guide


### format_helper.py walkthrough

This file is filled with 3 "helper" functions -- functions that do nothing but handle little tasks like formatting URLs and date strings. Note that `format_helper.py` makes no reference to the Requests or BeautifulSoup lbirary

#### Resolving relative URLs given a source URL with `make_absolute_url()`

One of the things we want to extract from each inmate row is the URL to their "Offender Information" page. For example, here's the URL for **John Ray Falk Jr.'s** page:

https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/falkjohnjr.html

However, that's not the URL we see when we look at underlying HTML for the "Offender Information" hyperlink:

```html
<a href="dr_info/falkjohnjr.html" title="Offender Information for John Falk">Offender Information</a>
```

The anchor tag's `href` attribute points to a value of `dr_info/falkjohnjr.html`. This is a **relative URL**. By convention, web browsers know how to resolve the absolute address. But BeatifulSoup does not:


```py
>>>> from bs4 import BeautifulSoup
>>>> txt = """
<a href="dr_info/falkjohnjr.html" title="Offender Information for John Falk">Offender Information</a>"""
>>>> soup = BeautifulSoup(txt, 'lxml')
>>>> tags = soup.select('a')
>>>> a = tags[0]
>>>> a.attrs['href']
'dr_info/falkjohnjr.html'
```

That relative URL -- `dr_info/falkjohnjr.html` -- goes nowhere in your browser, because it's not a real Web address. 

It's just not BeautifulSoup's job to do anything but parse HTML text -- i.e. it has no knowledge that the HTML came from a webpage from the Internet, nevermind that webpage's absolute URL.

So how do we get from

```
'dr_info/falkjohnjr.html'
```

to:

```
'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/falkjohnjr.html'
```

We could just manually concatenate (add) the strings together:

```py
a = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/'
b = 'dr_info/falkjohnjr.html'
full_url = a + b
```

Where `a` is dervived from this original URL:

```py
'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
```

But we shouldn't like doing anything manual -- especially because we should anticipate that for some web-scraping jobs, we won't know the absolute URLs in advance. Lucky for us, there is a function called `urljoin()` which is part of the Python library, `urllib.parse`:

https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse

`urlparse()` takes two arguments: 

- an absolute URL -- i.e, the URL of the page that the relative URL was found 
- a relative path -- i.e. a partial URL

Try it in ipython:

```py
>>>> from urllib.parse import urljoin
>>>> a = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
>>>> b = 'dr_info/falkjohnjr.html'
>>>> full_url = urljoin(a, b)
>>>> full_url
'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/falkjohnjr.html'
```


Further reading: [Relative vs. absolute URLs and using urljoin()](http://www.compjour.org/warmups/govt-text-releases/extracting-absolute-wh-press-briefings-urls/#relative-vs-absolute-urls)


#### Converting a datestring format to ISO format with `txdate_to_iso()`

This is in regards to the `txdate_to_iso()` function you have to write...

ISO format dictates that dates should be in `'YYYY-MM-DD'` format. But the Texas death penalty page has them in `'MM/DD/YYYY` format.

How do we fix this? We'll learn the more complicated datetime parsing methods later, for now, let's stick to the string `.split()` method, which takes as argument a *delimiter* (i.e. the character that is used as a separator) and returns a list of strings:

https://docs.python.org/3/library/stdtypes.html#str.split

```py
>>>> dt = '01/19/2014'
>>>> mylist = dt.split('/')
>>>> mylist[0]
'01'
>>>> mylist[2]
'2014'
```

How to rearrange those parts into `YYYY-MM-DD` format? Try the `.join()` method:

https://docs.python.org/3/library/stdtypes.html#str.join

```py
>>>> x = ['2017', '01', '19']
>>>> y = '-'.join(x)
'2017-01-19'
```






##### Messy dates

Unfortunately, the Texas death penalty page is not as clean as we want. For example, some dates are in `'MM/DD/YY'` format, e.g. `'12/15/78'`, instead of `'12/15/1978'`

This is a special case that your `txdate_to_iso()` function will have to deal with...you might even call it a **special condition**. 

How would you detect this condition?

What's the difference between these two strings:

- `'12/15/1978'`
- `'12/15/78'`



#### Finding the amount of time between two dates with `calc_years_diff()`

The `calc_years_diff()` function requires you to return the number of years -- rounded to the nearest tenth of a year, between two dates *given as strings*.

You should already know that subtracting 2 strings won't work:

```py
>>>> b = '2018-02-01'
>>>> a = '2017-01-01'
>>>> b - a
```

For this solution, I recommend using Python's built-in `datetime.strptime()` function from its `datetime` library:

https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime

There's a lot to unpack, including this mini-syntax for formatting time strings:

http://strftime.org/

But here's how it looks in ipython:

```py
>>>> from datetime import datetime
>>>> b = '2018-02-01'
>>>> a = '2017-01-01'
>>>> db = datetime.strptime(b, '%Y-%m-%d')
>>>> da = datetime.strptime(a, '%Y-%m-%d')
>>>> db - da
datetime.timedelta(396)
```

How to convert that object into a "years" value? How many days in a year?

Dealing with datetimes and strings is pretty complicated, so this is just a taste of it. The bottom line is that computers don't recognize our notion of how we describe time:

Another example:

https://stackoverflow.com/questions/44596077/datetime-strptime-in-python




### scraper.py walkthrough

This part of the walkthrough deals with the HTML parsing.

#### Extracting each inmate row with `get_and_parse_inmate_rows()`

In the previous assignment, [txdeathrow_check][../txcdathrow_check], we were tasked with writing a function named `get_and_parse_inmate_rows()` to get each **inmate row**.

We used the following selector:

```py
rows = soup.select('tr')
```

(we also had to make sure we didn't select the row representing the table header, but that's as easy as leaving off the first row in the resulting list).

Because the last assignment just asked for a quick count, selecting rows was all we needed to do for `get_and_parse_inmate_rows()`. 

In other words, whatever worked for [txdeathrow_check][../txcdathrow_check] can be copy-pasted for this assignment.


#### Extracting each "column"

For this assignment, we're tasked with doing something to each row element -- extracting the data and returning it in dictionary form. This is what the `wrangle_inmate_data_from_tag()` function does. 


Here's an example of what the raw HTML looks like -- note how the `<tr>` element has a bunch of "children" tags (and they all have the same tag name):

```html
<tr>
      <td>999608 </td>
      <td align="center"><a href="dr_info/hudsonwilliam.html" title="Offender Information for William Hudson">Offender Information</a></td>
      <td>Hudson</td>
      <td>William</td>
      <td>07/03/1982</td>
      <td align="center">M</td>
      <td>White </td>
      <td>11/16/2017</td>
      <td>Anderson</td>
      <td>11/14/2015</td>
</tr>
```

Just like the object we've previously designated in the `soup` variable -- a `bs4.BeautifulSoup` object, each "child" of that `BeautifulSoup` -- a BS4 `Tag`, has a `.select()` method from which we can derive *child* tags:

```py
from bs4 import BeautifulSoup
txt = """
<html>
   <h1>
      <a href="https://www.latimes.com">Hello</a>
      <a>world</a>
    </h1>
   <h1>
      <a href="https://www.nytimes.com">Goodbye</a>
      <a>everyone</a>
    </h1>
</html>
"""

soup = BeautifulSoup(txt, 'lxml')
htags = soup.select('h1')
for h in htags:
    atags = h.select('a')
    print('0:', atags[0].text, atags[0].attrs['href'])
    print('1:', atags[1].text)
    print('\n')
```

This pattern applies to the HTML for the table rows of the TX death row inmates, except that the death row HTML has many more "children" elements.


#### What's the deal with extra whitespace and `.strip()`?

Like most real world HTML, the TX death row inmates page has eccentricities and imperfections. Namely, **extraneous whitespace** -- i.e. "leading and trailing whitespace" -- in the *text* values of each element. Compounding the problem is that HTML, unlike Python, does not care about extraneous whitespace. That is, the following HTML elements will look exactly the same when rendered in a browser:



```html
<h1>Hello world!  </h1>
<h1>  Hello world! </h1>
<h1>Hello world!</h1>
```

But they *won't* produce the same values when extracted programmatically:

```py
from bs4 import BeautifulSoup
txt = """
<h1>Hello world!  </h1>
<h1>  Hello world! </h1>
<h1>Hello world!</h1>"""
soup = BeautifulSoup(txt, 'lxml')
tags = soup.select('h1')
t0 = tags[0].text
t1 = tags[1].text
t2 = tags[2].text
```

Inspecting the contents of those variables:

```py
>>>> t0
'Hello world!  '
>>>> t1
'  Hello world! '
>>>> t2
'Hello world!'
>>>> t0 == t1 == t2
False
```

Python strings have a method named `.strip()`, which you can read about here:

https://docs.python.org/3/library/stdtypes.html#str.strip


```py
>>>> t0.strip() == t1.strip() == t2.strip()
True
```









