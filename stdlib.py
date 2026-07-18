"""
Arrow Programming Language
Standard Library
Version 0.1.0 Genesis
"""


import os


# ======================================
# ARRAY FUNCTIONS
# ======================================


def length(value):

    return len(value)



def append(value, item=None):

    if isinstance(value,list):

        value.append(item)

    return value



def remove(value, item=None):

    if isinstance(value,list):

        if item in value:
            value.remove(item)

    return value



def insert(value, item=None):

    if isinstance(value,list):

        value.append(item)

    return value



def pop(value):

    if isinstance(value,list):

        if value:
            return value.pop()

    return None



def clear(value):

    if isinstance(value,list):

        value.clear()

    return value



def contains(value,item=None):

    try:
        return item in value

    except:

        return False



def sort(value):

    if isinstance(value,list):

        value.sort()

    return value



def reverse(value):

    if isinstance(value,list):

        value.reverse()

    return value



def first(value):

    if isinstance(value,list):

        if len(value)>0:
            return value[0]

    return None



def last(value):

    if isinstance(value,list):

        if len(value)>0:
            return value[-1]

    return None



def sum_array(value):

    if isinstance(value,list):

        return sum(value)

    return 0



def min_array(value):

    if isinstance(value,list):

        return min(value)

    return None



def max_array(value):

    if isinstance(value,list):

        return max(value)

    return None



# ======================================
# STRING FUNCTIONS
# ======================================


def upper(value):

    return str(value).upper()



def lower(value):

    return str(value).lower()



def trim(value):

    return str(value).strip()



def split(value,separator=" "):

    return str(value).split(separator)



def replace(value,data=None):

    if data:

        return str(value).replace(
            data[0],
            data[1]
        )

    return value



def startswith(value,text=None):

    return str(value).startswith(text)



def endswith(value,text=None):

    return str(value).endswith(text)



# ======================================
# FILE FUNCTIONS
# ======================================


def write_file(filename,data):

    with open(
        filename,
        "w",
        encoding="utf8"
    ) as f:

        f.write(
            str(data)
        )

    return filename



def read_file(filename):

    if os.path.exists(filename):

        with open(
            filename,
            "r",
            encoding="utf8"
        ) as f:

            return f.read()

    return ""



def append_file(filename,data):

    with open(
        filename,
        "a",
        encoding="utf8"
    ) as f:

        f.write(
            str(data)
        )

    return filename



# ======================================
# STD FUNCTIONS TABLE
# ======================================


STD_FUNCTIONS = {


    # arrays

    "length": length,
    "append": append,
    "remove": remove,
    "insert": insert,
    "pop": pop,
    "clear": clear,
    "contains": contains,
    "sort": sort,
    "reverse": reverse,
    "first": first,
    "last": last,
    "sum": sum_array,
    "min": min_array,
    "max": max_array,


    # strings

    "upper": upper,
    "lower": lower,
    "trim": trim,
    "split": split,
    "replace": replace,
    "startswith": startswith,
    "endswith": endswith,


}