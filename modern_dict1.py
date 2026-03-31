# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:34:28 2020

@author: z093920
"""

#http://web.archive.org/web/20161209120412/https://dl.dropboxusercontent.com/u/3967849/sfmu2/_build/html/goal.html

#Our Journey: The Beginning and the End
#Python is built around dictionaries. The various namespaces include globals, locals, module dictionaries, class dictionaries, instance dictionaries.
#
#Of these, instance dictionaries are among the most prolific.
#
#Instance Dictionaries
#Create a class to track user assignments with in a property category.

#from __future__ import division, print_function
#import sys
#
#class UserProperty:
#    def __init__(self, v0, v1, v2, v3, v4):
#        self.guido = v0
#        self.sarah = v1
#        self.barry = v2
#        self.rachel = v3
#        self.tim = v4
#
#    def __repr__(self):
#        return 'UserProperty(%r, %r, %r, %r, %r)' \
#               % (self.guido, self.sarah, self.barry, self.rachel, self.tim)
#
#colors = UserProperty('blue', 'orange', 'green', 'yellow', 'red')
#cities = UserProperty('austin', 'dallas', 'tuscon', 'reno', 'portland')
#fruits = UserProperty('apple', 'banana', 'orange', 'pear', 'peach')
#
#for user in [colors, cities, fruits]:
#    print(dir(user))
#
#print(list(map(sys.getsizeof, map(vars, [colors, cities, fruits]))))


#Evolution: A Half Dozen Good Ideas
#In the beginning, there were databases.
#
#Now, we have come full circle. With all our progress on dictionaries, we’ve reinvented what was done with databases long ago.
#
#Setup
#Here is our sample data to store in our dictionaries.


from __future__ import division, print_function
from pprint import pprint

keys = 'guido sarah barry rachel tim'.split()
values1 = 'blue orange green yellow red'.split()
values2 = 'austin dallas tuscon reno portland'.split()
values3 = 'apple banana orange pear peach'.split()
hashes = list(map(abs, map(hash, keys)))
entries = list(zip(hashes, keys, values1))
comb_entries = list(zip(hashes, keys, values1, values2, values3))


#How a Database Would Do It
#The data is dense (no holes or over-allocations). And without an index, the search is linear.

def database_linear_search():
    pprint(list(zip(keys, values1, values2, values3)))

# Array of Tuples

#[('guido', 'blue', 'austin', 'apple'),
# ('sarah', 'orange', 'dallas', 'banana'),
# ('barry', 'green', 'tuscon', 'orange'),
# ('rachel', 'yellow', 'reno', 'pear'),
# ('tim', 'red', 'portland', 'peach')]
#
    
#How LISP Would Do It
#Store lists of pairs.

#def association_lists():
#    pprint([
#        list(zip(keys, values1)),
#        list(zip(keys, values2)),
#        list(zip(keys, values3)),
#    ])    







