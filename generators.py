from sys import getsizeof
from si_prefix import si_format
import psutil

# generator allow you to read / calculate data without the need to load it up to list before, just yield the next value while needed.

def get_used_memory():
    return psutil.virtual_memory().used

###############
## Example 1 ##
###############

# option 1 #
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
#print(next(PowTwoGen(50)))
#for item in PowTwoGen(50): print(item)

# option 2 -  generator comprehesion # the benefit is numbers are not stored in memory
def test():
    data = (2**n for n in range(50))

    print(list(data)) # generator already finished next() stastments, and need to be reset, just run the above line again or store the data to have it again

    data = (2**n for n in range(50))
    for d in data: 
        print(next(data))

# list #




###############
## Example 2 ##
###############

my_list = [1, 3, 6, 10]
lst = [x*2 for x in my_list]
generator = (x*2 for x in my_list)
#print(sum(x**2 for x in my_list))
#print(max(x**2 for x in my_list))
#print(lst)
#print(generator)
#print(next(generator))


###############
## Example 3 ##
###############

def multiply_by_two(num):
    while True:
        yield num *2
#for x in range(10): print(next(multiply_by_two(x))) 







#########################################
## very basic manual use of generators ##
#########################################

def get_values():
    yield "hello"
    yield "world"
    yield 123

def simple_accsses():

    # simple accsses , each one at a time
    out = get_values()
    print(out)
    print(next(out))
    print(next(out))
    print(next(out))

    # for loop acssess
    out = get_values()
    for x in out:
        print(x)

    # output to list
    lst = list(get_values())
    print(lst)

######################################################################################################################
## Comprasion of several ways (list & generator) to read and find specifc text in a text file with memory efficancy ##
######################################################################################################################

def create_dummy_data():

    # create the file (if needed)#
    with open('dummy_data.txt', 'w') as f:
        for i in range(100_000): f.write(f"{i+50}\n")

def get_int_from_item(item):
    #can add try except and more...
    return int(item.rstrip())

def get_data_with_generator():
    start = get_used_memory()
    # read data with list - find index of number 9900
    with open('dummy_data.txt','r') as f:
        for index,line in enumerate(f, start = 1):
            if line == '99000\n':
                yield index
    delta = get_used_memory()- start
    print(si_format(delta, precision= 4))

def get_data_with_list_memory_efficiant():

    start = get_used_memory()
    # read data with list - find index of number 9900
    with open('dummy_data.txt','r') as f:
        for index,line in enumerate(f, start = 1): # start placeholder do iterate all list by act as a bias so start of 1 will start with index 1 instead of 0
            if line == '99000\n':
                data = index
                break

    #print(data)
    delta = get_used_memory()- start
    print(si_format(delta, precision= 10))

def get_data_with_list_memory_consumption():

    start = get_used_memory()
    # read data with list - find index of number 9900
    with open('dummy_data.txt','r') as f:

        # load data from file (list is memory not efficient if you read all lines)
        data = f.readlines()
        #print(len(data))
        #print(si_format(getsizeof(data),precision=4))

        # make each element as int instead of string and remove end line termination
        new_list = [get_int_from_item(item) for item in data]

        if 99000 in new_list:
            pass
            #print(new_list.index(9900))

        #not required
        #index_needed = list(filter(lambda val: val == 9900 ,new_list))
    delta = get_used_memory()- start
    print(si_format(delta, precision= 4))

def sub_main():
    
    #create_dummy_data()
    #
    #get_data_with_list_memory_efficiant()
    #
    #get_data_with_list_memory_consumption()
    #
    #res = [match for match in get_data_with_generator()]
    #print(res)
    pass


