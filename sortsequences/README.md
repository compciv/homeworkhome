# sortsequences - Quick exercises with the `sorted()` method

Similar to [ezsequences](../ezsequences), except the focus is on using `sorted()` to sort sequences of elements.

Besides *filtering* (which we implement with conditional statements), *sorting* is the most powerful technique we have in working with information. As with everything in programming, sorting is more complicated than we think it should be, but only because programming gives us so much control.

Sorting via programming seems overly complicated only if you've thought that there was an "obvious" way for things to be sorted in life. Consider Edward Tufte's musings on the impact of choosing the right sorting algorithm for the Vietnam Veterans Memorial (nevermind the power of a simple list): 

[Lists: design and construction, by Edward Tufte](https://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0002QF)

## Requirements

There are 3 scripts with function definitions -- fill out the function definitions so that they pass the tests/requirements. The work is split into 3 small files so that it's not as annoying to read through the files. Also, the first function in each file is done for you as an example:

- [sort_numbers.py](skeleton.sort_numbers.py)
- [sort_strings.py](skeleton.sort_strings.py)
- [sort_people.py](skeleton.sort_people.py)

These 3 files expect a file -- which I've provided for you -- named: [datastubs.py](datastubs.py). This is just to better organize things -- in practice, we want to keep code and data separated as much as possible.

This exercise also has the tests split into 3 files and put into their own subfolder, so that you can run one set of tests at time instead of being overwhelmed with `failure` messages at the very start, e.g.

```sh
$ pytest tests/test_sort_numbers.py
```


<a name="cli-setup" id="cli-setup"></a>

## Setup via the command-line

Assuming you're in your working directory, here's the `curl` commands to download the starter files:

**Mac OS/Linux**

```sh
$ curl -O https://compciv.github.io/homeworkhome/sortsequences/datastubs.py

$ curl -o sort_numbers.py \
    https://compciv.github.io/homeworkhome/sortsequences/skeleton.sort_numbers.py

$ curl -o sort_people.py \
    https://compciv.github.io/homeworkhome/sortsequences/skeleton.sort_people.py

$ curl -o sort_strings.py \
    https://compciv.github.io/homeworkhome/sortsequences/skeleton.sort_strings.py

### There's enough test files to have a subdirectory for tests
$ mkdir -p tests
$ cd tests
$ curl -O \
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_numbers.py
$ curl -O \
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_strings.py
$ curl -O \
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_people.py

### This final cd command takes us back up from the tests/ subdirectory
$ cd ..

```


**Windows** 

The same thing as above, except use `curl.exe` and use the **backtick** ``` to continue a long command into another line:


```
$ curl.exe -O https://compciv.github.io/homeworkhome/sortsequences/datastubs.py

$ curl.exe -o sort_numbers.py `
    https://compciv.github.io/homeworkhome/sortsequences/skeleton.sort_numbers.py

$ curl.exe -o sort_people.py `
    https://compciv.github.io/homeworkhome/sortsequences/skeleton.sort_people.py

$ curl.exe -o sort_strings.py `
    https://compciv.github.io/homeworkhome/sortsequences/skeleton.sort_strings.py

### There's enough test files to have a subdirectory for tests
$ mkdir -p tests
$ cd tests
$ curl.exe -O `
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_numbers.py
$ curl.exe -O `
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_strings.py
$ curl.exe -O `
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_people.py

### This final cd command takes us back up from the tests/ subdirectory
$ cd ..

```

The tests for this assignment have been put into a subfolder, [tests/](tests/), because I decided to split them into 3 separate files, allowing you to just run the tests for one set of exercises at a time. The following invocation (use your Tab key to autocomplete!) will run only the tests relevant to `sort_strings.py`:

```sh
$ pytest tests/test_sort_strings.py
```

Feel free to look at the source code for the test files. In this case, they pretty much serve as an answer key (what you *should* be seeing). However, please don't write functions that just return the literal answer, i.e.:

```py
# in sort_numbers.py
def as_absolute_value():
  theanswer_lulz = [0.77, 3, -9, 42, -1024]
  return theanswer_lulz
```


## Practice with `sorted()`

Last year I wrote a longer guide on using Python's built-in `sorted()` method:

[Sorting Python collections with the sorted method](http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/)

And here is the official Python documentation on `sorted()`:



However, for the purposes of this homework, I've tried to create a more condensed guide that shows the syntax:



```py
>>>> data = [ 'danny', 'bob', 'leland', 'alice', 'danielle']
```


### Simple sorting


Before we get into anything fancy, it's worth pointing out that `sorted()` can be used by giving it just a sequence and no other arguments. By default, `sorted()` returns things in **ascending** order -- e.g. alphabetical when it comes to letters, numerical when it comes to numbers, etc.


```py
>>>> sorted(data)
['alice', 'bob', 'danielle', 'danny', 'leland']
```

Sometimes we want things in *reverse* order, `sorted()` takes in a `reverse` argument, which we can set to `True`:

```py
>>>> sorted(data, reverse=True)
['leland', 'danny', 'danielle', 'bob', 'alice']
```

So that works well enough. But things get complicated when our sequences/lists are not just plain strings. Or when our sort conditions need to be more sophisticated than biggest/alphabetical/etc.

### The problem with complex sequences/data

For example, consider this heterogeneous list of strings and numbers:

```py
>>>> hdata = ['2', 42, 9, '100']
```

In your head, sorting that list probably seems easy. But passing it to `sorted()` throws an error:

```py
>>>> sorted(hdata)
TypeError: '<' not supported between instances of 'int' and 'str'
```

That error message isn't as intimidating as it seems: Python is telling us that the `<` operator -- i.e. the **less than** comparator, can't be used when comparing an `int` and a `str`. You can test this out manually:

```py
>>>> '9' > 99
TypeError: '<' not supported between instances of 'str' and 'int'
```

It seems annoying at first, but on closer reflection, the error makes sense -- what *should* Python *do*? There's no easy answer for all use cases.

However, for our simple use case, we may be content with: "Well, convert all of `hdata` into proper integers and *then* sort the list":


```py
hnums = []
for d in hdata:
  hnums.append(int(d))
```

(btw, the more Pythonic way to do this is to use a **list comprehension** -- try it if you feel comfortable):

```py
hnums = [int(d) for d in hdata]
```

Or maybe you want to sort `hdata` by treating all of its members as strings:

```py
htxts = [str(d) for d in hdata]
# or:
htxts = []
for d in hdata:
  htxts.append(d)
```

And now `sorted()` has no problem sorting these homogeneous sequences:

```py
>>>> sorted(hnums)
[2, 42, 9, 100]
>>>> sorted(htxts)
['100', '2', '42', '9']
```

However, *we* kind of have a problem. It's a bit subtle because we're not trying to do anything practical, but it boils down to the fact that `hnums` and `htxts` are lists that contain completely changed data from what `hdata` contains:

```py
>>>> hdata
['2', 42, 9, '100']
```


### Using the `key` argument

What if we wanted a sorted version of `hdata`, using one of the example criteria above (sort as `str` or as `int`) -- but we needed each member of `hdata` to be unaltered (other than their sorting order)?

`sorted()` has a `key` argument which accepts the *name of a function* -- this includes `str()` and `int()`, which are used to convert objects, respectively, into strings and integers.

Compare the results of sorting `hdata` with a `key` versus transforming all the elements in `hdata` and *then* sorting:


Here's the conversion to integer and *then* sorting, versus using `sorted()` with a `key` argument of `int`:

```py
>>>> sorted([int(d) for d in hdata])
[2, 9, 42, 100]

>>>> sorted(hdata, key=int)
['2', 9, 42, '100']
```

Here's the conversion to string and *then* sorting, versus using `sorted()` with a `key` argument of `str`:

```py
>>>> sorted([str(d) for d in hdata])
['100', '2', '42', '9']

>>>> sorted(hdata, key=str)
['100', '2', 42, 9]
```


### Making mini-functions for `key`

The need to sort a sequence without altering the actual data in that sequences is more obvious if we have a sequence of complex objects, such as a list of `dict` objects: 

```py
>>>> peeps = [{'age': 42, 'name': 'Bob'}, {'age': 53, 'name': 'Alice'}]
>>>> sorted(peeps)
TypeError: '<' not supported between instances of 'dict' and 'dict'
```

What if we wanted to sort `peeps` in alphabetical order of name? Extract the `name` properties and sorting gets us a list of strings, which is not great, because we probably want to be working with a list of `dict` objects, not plain strings:


```py
names = []
for p in peeps:
  names.append(p['name'])
```

```py
>>>> sorted(names)
['Alice', 'Bob']
```

But what *function name* do we pass into the `key` argument when we need to just extract an key-value from a dictionary? Well, there's nothing wrong with making our own function and naming it what we want:

```py
def sortfoo(m):
  return m['name']
```

```py
>>>> sorted(peeps, key=sortfoo)
[{'age': 53, 'name': 'Alice'}, {'age': 42, 'name': 'Bob'}]
```

It can be hard at first to wrap your head around what `sortfoo`, its argument `m`, and its `return` value represent. It's important to remember that, like variables, to remember the *names* are human-definable, so you don't need to follow my naming habits:

```py
def getname(member):
    return member['name']

sorted(peeps, key=getname)
```

`sortfoo()`, `getname()`, whatever you want to call it, is just a function like any other. It's only "special" because we pass it into the `key` argument of `sorted()`. Because we're trying to tell the `sorted()` method: *Hey dummy, this is how you should be ranking/sorting things in my list!*

What's returned by our little helper function is the thing -- for every item in our sequence/list -- that we want `sorted()` to use in sorting. 

Again, the big picture is that programming, computers, computation, etc, can't make complicated decisions without our direct input.


Here's how we would adjust `sortfoo()` to sort by age -- I'll rename it `fetch_age()` just to reemphasize how much of this is in our control:

```py
def fetch_age(item):
  return item['age']
```

Or, to sort by how *long* someone's name is:

```py
def namechars(cow):
  return len(cow['name'])
```

We can return anything we want, even something nonsensical, as long as it is a value that `sorted()` knows how to implicitly sort:

```py
def wtf(dude):
  return 9208349
```

What is the effect of the above nonsensical function? When `sorted()` uses it as its `key` function to figure out how to sort out items in a sequence, it always gets the same value: `9208349`

What happens when every item in a list has the same comparison value? 

```py
data = [9, -4, 400, 42]
def wtf(d):
  return 'whatever'
```

-- nothing gets sorted! 

Output:

```py
>>>> sorted(data, key=wtf)
[9, -4, 400, 42]
```

In other words, defining this "key" function is completely in our control, we can make it as complicated or as useless as we want.

#### Quick `sorted()` exercise on a list of lists

Given this setup, which involves a list of lists:

```py
prezdata = [['Donald', 'Trump'], ['Barack', 'Obama'], ['George', 'Bush']]
```

Can you use `sorted()` to sort this list in alphabetical order of each sublist's *second* item (i.e. the "last name" of these presidents)?


Here's how to do it using a quickie function (the `_` character is a common convention to indicate that this function is meant to have a very limited scope):

```py
def _foobar(k):
  return k[1]

mydata = sorted(prezdata, key=_foobar)
```








#### Sorting by multiple factors/values


It's also how we can specify sorting by multiple factors -- if we wanted to sort by length of name, and in case of a tie, by age:


```py
def sortfoo(m):
  return (len(m['name']), m['age'])
```

This works because `sorted()` does know how to deal with a sequence of lists/tuples, in which each individual member is sortable:


```py
>>>> xdata = [(9, 2), (1, 2), (9, -5)]
>>>> sorted(xdata)
[(1, 2), (9, -5), (9, 2)]
```


### Alternate ways to work with the `key` argument


#### Extracting key-value from dicts using operator.itemgetter()

Needing to sort by a `dict` object's key/value is so common that the standard Python library comes with a little helper.

Instead of doing this:

```py
data = [{'name': 'pat', 'age': 20}, {'name': 'dan', 'age': 12}]
def sortfoo(x):
  return x['name']

mydata = sorted(data, key=sortfoo)
```

You can do this:

```py
from operator import itemgetter
data = [{'name': 'pat', 'age': 20}, {'name': 'dan', 'age': 12}]
mydata = sorted(data, key=itemgetter('name'))
```

#### The `lambda` operator for single-line anonymous functions

These "key" functions often just have a single line of logic. Python has a syntax/construct for specifying these anonymous, one-line functions that, if you may really enjoy if are comfortable with functional programming, and enjoy conciseness.



```py
data = [{'name': 'pat', 'age': 20}, {'name': 'dan', 'age': 12}]
mydata = sorted(data, key=lambda x: x['name'])
```


#### Quick `sorted()` exercise on a list of dicts, lambda vs foo

Another exercise -- this time we'll compare the different styles of solvin git:

Given the following sequence, sort it in descending order of total pets owned. In case of a tie, the person with the most *cats* wins:

```py
thedata = [
  {'dogs': 3, 'cats': 2, 'name': 'Tom'},
  {'dogs': 1, 'cats': 2, 'name': 'Alice'},
  {'dogs': 0, 'cats': 2, 'name': 'Pat'},
  {'dogs': 1, 'cats': 4, 'name': 'Kim'},
]
```

**Defining a simple limited use function**

```py
def peteval(i):
  total = i['dogs'] + i['cats']
  cats = i['cats']
  return (total, cats)

sorted(thedata, key=peteval, reverse=True)
```

**Using lambda**

```py
sorted(thedata, reverse=True, 
       key=lambda x: [x['dogs'] + x['cats'], x['cats']])
```

### Conclusion: What's better

So What's better, what's worse? Like with everything in programming, *it depends*.

I prefer the `lambda` style because it's fun jamming things into one line, but you can see in the above example how things can be pretty unreadable when the logic involves more than one step.

If you are relatively new to programming in general, nevermind functional programming concepts -- I recommend sticking with defining a quickie function for `sorted()`. It can look inelegant, but it does exactly what's needed, and you can never have enough practice writing and designing functions, even very small ones. 
















