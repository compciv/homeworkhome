
## Overview

A follow up/add-on to [txdeathrow_check](../txdeathrow_check). We build upon our scraper for the [Death Row Information Homepage of the Texas Department of Criminal Justice](https://www.tdcj.state.tx.us/death_row/), specifically, the [Offenders on Death Row page](https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html), except this time, we turn it into usable data objects (a list of dictionaries)

https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html

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


### Functional requirements

There are 3 function definitions in [scraper.py](skeleton.scraper.py):


- `get_inmate_data()` - is already written for you
- `get_and_parse_inmate_rows()` - you can use the exact same thing as last assignment
- `wrangle_inmate_data_from_tag()` - this is what you have to fill out 

There are 3 function definitions in [format_helper.py](skeleton.format_helper.py) -- all of them you'll fill out

- `txdate_to_iso`
- `calc_years_diff`
- `make_absolute_url`


The [data_helper.py](data_helper.py) file is provided to you -- it basically just takes care of downloading from the webpage if needed. The only function you need to use from `data_helper` is `get_html()`, which returns the raw text of the death penalty webpage.




## Setup and getting started

### Using Python

```py
# TK
```

### Running the tests

The tests are in a file named [test_checker.py](test_checker.py). Use `pytest` at the command line to run them:

```sh
$ pytest
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









