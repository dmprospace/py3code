import inspect
def lno():
    """Returns the current line number in our program."""
    return "Line No "+(str(inspect.currentframe().f_back.f_lineno)) +"=> " 

a=[6,2,7,4,3,5,7,9,3,1,4,6,8,2,3,4,5,7,1,2,2,2,3]
#print (a.count(2))  # frequency of the element
#print (a.count(5))
#a.append(5);        # append element at the rear end
#print (a.count(5))
#a.extend([2,5]);    # extend by adding elements from iterator at the rear end
#print (a.count(2))
#print (a.count(5))
#print(a.index(2));  # index of first occurance
#a.insert(0,'1');    # INSERT at position , element
#print(a)
#a.remove('1')       # remove first occurance
#print(a)
#print(a.pop())      # rear end of the list
#print(a)
#a.remove(5)         # Remove first occurance of element
#print(a)
#a.reverse()
#print(a)
#a.sort()
#print(a)
#############################################################################################
## Iterable and Iterator ##

## Iterable : Something that "can be looped over" and has __iter__() method
# **(Iterable is ANY python object that HAS __iter__() method)
# by calling __iter__() method on an ITERABLE object, An Iterator is returned which has __next__ method defined.

# Ex. In Python A List is an iterable
# Many Iterables : List, Tuples, Dict, Files, Generators etc.

nums="DEVESH" #[1,2,3]
nums=[1,2,3]
print (dir(nums))          # ... , __iter__() , ...
print (type(nums))         # <class 'str'> or <class 'list'> 
#print (nums)               # DEVESH or [1,2,3]
#print (repr(nums))         #'DEVESH' or [1,2,3]
#print (str(nums))          # DEVESH or [1,2,3]
#for num in nums: print(num)

######################################
## **(iterator is *ANY* python object which has __next__ method) e.g. Generator
# is an object with an state, so that it remembers its state during iteration
# by calling __iter__() method on an ITERABLE object, An Iterator is returned which has __next__ method defined (in addition to __iter__()).
# Iterators also Iterables, but calling iter on iterator returns same object.

i_nums=nums.__iter__() # same as iter(nums)

#print(dir(i_nums))         # ... , __iter__() , ... , __next__() , ...
#print (type(i_nums))       #<class 'str_iterator'>                       or  <class 'list_iterator'>
#print (i_nums)             #<str_iterator object at 0x0000000002F30C08>  or  <list_iterator object at 0x0000000002EC0FC8>

#print(next(i_nums))         # same as i_nums.__next__()
#print(next(i_nums))
#print(next(i_nums))
#print(next(i_nums))

#x=[num for num in nums]            # List Comprehension 

#print(type(num for num in nums))   # <class 'generator'>

### for loop over iterator

#for item in i_nums:    print(item, end=",")
#print("")


### Iterators can only go in one direction and no going back, 
###    hence you can not process second time in Iterator by doing over 

#for item in i_nums:    print(item, end=";")

### for loop over iterable
#for item in nums:    
#    print(item)
    
# for loop mimic => for item in nums . same result as loop over Iterator
# create new object if you need to process again
while True:
    try:
        item=next(i_nums)
        print(lno() + str(item),end=" ~ ")
    except StopIteration:
        break
print(lno())
# implementing Class that behaves as built in range function, as an Iterable
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        else:
            current = self.value
            self.value +=1
            return current

# Its an iterable object , by definition
nums = MyRange(1, 10)

for num in nums:    
    print(num,end="|")
print(lno())

#https://www.pythonmorsels.com/topics/iterator-zip/
#https://www.pythonmorsels.com/topics/iterators/
#https://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/
#https://treyhunner.com/2018/02/python-range-is-not-an-iterator/
#https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/
#https://www.youtube.com/watch?v=JYuE8ZiDPl4&feature=youtu.be
#https://www.youtube.com/watch?v=V2PkkMS2Ack

# loops and iterators 
# Python Loops sequentially assign a variable to the objects returned by an iterator
# **(iterator is *ANY* python object which has __next__ method) e.g. Generator
#    throws/signals topIteration Exception after last element in the sequence

# Comprehensions and generators. 
# Comprehensions are a "way to run a loop within a single line of code", and to collect the results of the loop in a collection, such as list, dict and set. 
# Generators are a shortcut to write functions that implement iterators. 
#  (Both are used extensively in Pythonic code) 
#
#  (A) list, dict, and set comprehensions
#  (B) Python generator expressions, and how to write Python generators.

       ### Generator Expression
       ##print(    k for k in range(5) )  # Generator Object (also uses IteratorProtocol)
       ##print(sum(k for k in range(5)))  # Sum 10 <= One Time
       ##
       ### Derived Iterators : range, enumerate, zip, reversed, sorted
       ### Python allows deriving more useful iterators from simple ones
       ###
       ##print(type(range(5)))          # prints => <class 'range'>
x=range(5)
       ##print(x)                       # prints => range(0, 5)
       ##y=list(x)                      # create a list from range() - Derived Iterator 
       ##print(y)                       # prints => [0, 1, 2, 3, 4]
       ##
       ###enumerate 
       ##print(enumerate(x))            # enumerate object
print(i for i in enumerate(x)) # Generator Object
       ##
       ##print(i for i,j in enumerate(x) if i>5) # Generator Object

########### Ned Batch-Elder ############
#Basics
# Traditional Beginner's LOOPS
# List
my_list = ['abc', 'def', 'ghi', 'jkl']
i = 0  # Index variable Initialization
while i < len(my_list):
    print (my_list[i]) # Retrieve element & print
    i += 1 # Increment Index

print("-------")

# or over python range
for i in range(len(my_list)): # say range(4) which is list of integers from 0 to len(my_list) [0,1,2,3] ; (This LIST will be used as indices) 
    print (my_list[i])  # Retrieve element & print