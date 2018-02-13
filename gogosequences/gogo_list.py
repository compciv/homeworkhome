gglist = [1, 2, 3, '4', 5, 6, [100, 200], 'Alice', 'Bob', 'Charile'
  'Daniel', 88, '8', 22.4, [{'name': 'Stanford', 'city': 'Stanford', 'state': 'CA'},
  {'name': 'Yale', 'city': 'New Haven', 'state': 'CT'},
  {'name': 'Caltech', 'city': 'Pasadena', 'state': 'CA'}], '95', 42]


def foo_hello():
    """
    Return a list, in which the
        first item is the object type of `gglist`
        and the second item is the length of `gglist`
    """
    t = type(gglist)
    n = len(gglist)
    z = [t, z]
    return z

def foo_a():
    """
    Return the sum of the first 3 members of `gglist`

    Don't just add it in your head; either use one of
      Python's sequence functions, or iterate through
      the sequence
    """


def foo_b():
    """
    Return the sum of all top-level members of `gglist`
     that happen to be numbers. Do not add numbers that
     are inside nested sequences/lists. And of course,
     don't add items that only look like numbers but are
     actually string objects
    """


def foo_c():
    """
    Return a list of all top-level strings in `gglist`
      (i.e. not inside a nested sequence) that are
      more than 3 characters long
    """

def foo_d():
    """
    `gglist` contains one list that has exactly 3 members,
      each of which happen to be `dict` objects -- this list
      can be described as a list of universities

    Return a list of strings that consists only of the names
      of the universities that are located in California
      (i.e. 'CA')
    """

def foo_e():
    """
    Return an integer that represents the number of
     members (again, top-level only) in `ggdict` that
     have a data type of `str`
    """

def foo_f():
    """
    Return a dict object that has a count of `ggdict` members
      by type. The keys of this dict should be *strings*, and
      the corresponding values should be integers.

      Sample answer:

       {'int': 5, 'str': 3, 'list': 2}
    """




