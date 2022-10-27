from collections import defaultdict
from typing import NamedTuple


#################
## namedtuple ##
#################
class ANamedTuple(NamedTuple):
    """a docstring"""

    foo: int
    bar: str
    baz: list


# based on: https://stackoverflow.com/a/34573457
def namedTuple_example():
    """
    It's a specific subclass of a tuple that is programmatically created to your specification, with named fields and a fixed length.
    use dict when values are constant and not going to change, for example return from function.
    """

    ant = ANamedTuple(1, "bar", [])
    print(ant.foo, ant.bar, ant.baz)
    # ant.foo = 2 # don't work as tuple is immutible

    ant.baz.append(1)
    print(ant.foo, ant.bar, ant.baz)

    # can serve as a dict key value so dict's key can have multiple items instead of one.
    # for example :
    x = {("item1", "value"): "data"}
    print([*x])  # convert keys to list
    # print([*x.values()]) # convert values to list

    # for k,v in dict.items()


namedTuple_example()


#################
## defaultdict ##
#################
def defaultdict_example():
    """
    defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown,
    a new entry is created. The type of this new entry is given by the argument of defaultdict.
    For example:
    """

    somedict = {}
    try:
        print(somedict[3])  # KeyError
    except BaseException as e:
        print(f"An exception of type {type(e).__name__} occurred. Arguments:{e}")

    print(somedict)

    someddict = defaultdict(int)
    print(someddict[3])  # print int(), thus 0
    print(someddict)

    someddict = defaultdict(list)  # default empty type
    print(someddict[3])  # print list(), thus []
    print(someddict)


# defaultdict_example()


#################################
## Collections module examples ##
#################################

# deque	        A sequence-like collection that supports efficient addition and removal of items from either end of the sequence
# defaultdict	A dictionary subclass for constructing default values for missing keys and automatically adding them to the dictionary
# namedtuple()	A factory function for creating subclasses of tuple that provides named fields that allow accessing items by name while keeping the ability to access items by index
# OrderedDict	A dictionary subclass that keeps the key-value pairs ordered according to when the keys are inserted
# Counter	    A dictionary subclass that supports convenient counting of unique items in a sequence or iterable
# ChainMap	    A dictionary-like class that allows treating a number of mappings as a single dictionary object

# Besides these specialized data types, collections also provides three base classes that facilitate the creations of custom lists, dictionaries, and strings:
#
# UserDict	    A wrapper class around a dictionary object that facilitates subclassing dict
# UserList	    A wrapper class around a list object that facilitates subclassing list
# UserString	A wrapper class around a string object that facilitates subclassing string
