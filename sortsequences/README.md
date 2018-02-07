# sortsequences - Quick exercises with the `sorted()` method





<a name="cli-setup"></a>

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

### There's enough test files to have a subdirectory:

$ mkdir -p tests
$ cd tests
$ curl -O \
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_numbers.py
$ curl -O \
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_strings.py
$ curl -O \
    https://compciv.github.io/homeworkhome/sortsequences/tests/test_sort_people.py



```



## Practice with `sorted()`

Last year I wrote a longer guide on using Python's built-in sorted() method:

[Sorting Python collections with the sorted method](http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/)

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

It can be hard to wrap your head around what `sortfoo` is, and why it has the argument `m`, although sometimes working through more examples will bring clarity. Basically, we're defining an arbitrary function that takes as an argument any single member of a list, i.e. the `dict` objects in `peeps`.

What is returned by our `sortfoo()` function is the value that we *want* `sorted()` to sort by. Because remember, the main problem we run into is when `sorted()` doesn't automatically know what to sort by.

Here's how we would adjust `sortfoo` to sort by age:

```py
def sortfoo(m):
  return m['age']
```

Or, to sort by how *long* someone's name is:

```py
def sortfoo(m):
  return len(m['name'])
```

We can return anything we want, even something nonsensical, as long as it is a value that `sorted()` knows how to implicitly sort:

```py
def sortfoo(m):
  return 9208349
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


### Trying to understand `sorted()` and its options

Python's motto is to preferably have one way of doing things. However, in the brief `sorted()` primer above, it may seem like there are way too many options.

But all the alternatives have the *same result* -- it all comes down to what you are comfortable with and what you can understand on your own. If you are relatively new to programming, I recommend just making little throwaway functions with whatever name you like:

```py
data = ['dan', 'DAN', 'DanNY', 'danny']
def bigfoo(m):
  return m.upper()

sorted(data, key=bigfoo)
```

I personally like using the `lambda` notation for its conciseness:

```py
data = ['dan', 'DAN', 'DanNY', 'danny']
sorted(data, key=lambda m: m.upper())
```

But I'll try to mix it up between the different styles.  As always, if you have any questions or confusions, please ask!










