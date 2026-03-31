import pyodbc

if __name__ == '__main__':
##### Section1  Welcome
## Lecture 1 Welcome to Python3
##### Section2 Setup
## Lecture 2  Download Python 3.5 : Python.org ;  Install Python 3.5+ : PATH 
## Lecture 3  Install Sublime Text : Rename Python.exe to python.exe : Open Sublime Text, Build System  : 
#config json config : cmd , file_regex , selector
# {
#"cmd": ["C:\\Users\\Test\\AppData\\Local\\Programs\\Python\\Python35-32\\python.exe", "-u", "$file"],
#"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*) ",
#"selector": "source.python"
#}
##### Section3 First Prog, data types, variable
    """
    ## Lecture 4  First Program in Python
        print('welcome')
    
    ## Lecture 5  Data Types
        print(type(1))
        
    ## Lecture 6  Variables
        # Reserved Memory Location with Some Value in it
        number =2
        real = 2.2
        word= "a word"
        print (word)
        a=b=c=1.5
        print(a)  # 1.5
        print(b)  # 1.5
        print(c)  # 1.5
        ##list
        one, two, three, =1, 'two' , 3.0
        print(one)        #1
        print(two)        #two
        print(three)      #3.0
        number=1
        str = 'string' # reassignment
        number = str
        print (number)

## Lecture 7 Indentation : Aesthetically Pleasing
    def test():
       print ('In test')
    
    test()

## Lecture 8 How to clear Screen
    import os
    clear = lambda: os.system('cls')
    clear()

## Lecture 9 Single Line Comments (# anything after hashtags)
    # Comments help us organize code, and tell other programmers what out code does. 
    # This is comment
    
    ## Lecture 10 Multi Line Comments (three quotations)
    ''' This is a comment 
    '''

## Lecture 11 Basic Arithmatic (Manipulating Numbers in Python)
    print(2+5)                   #  7 
    print(2+5+3.0)               #  10.0
    print (10-5.0)               #  5.0
    print(100-3-1-0.0)           #  96.0
    print(40*30)                 #  1200 
    print(40*30*0.5)             #  600.0
    print(2**5)                  #  32
        
## Lecture 12 Division Characteristics
    print(23/5)                  #  4.6
    print(23//5)                 #  4
    print(23.0%5)                #  3.0
    a=2 + 5     ;   print(a)     #  7
    b=3.3 * 3   ;   print(b)     #  9.89999999
    c=10.0  / 25;   print(c)     #  0.4
        
## Lecture 13. Operator Precedence
    a=25*15+33/2.0      ;   print (a)
    a=(25*(15+33/2.0))  ;   print (a)
    a=((25*2**2+33)/2.0);   print (a);
    pass                ;   print (((8+14/5/2)*5.0)%4)

## Lecture 14. Complex Arithmatic
    print(5.0 *(8 +(16 -2.0)/(4+1)/2) % 4) # 3.0
     
## Lecture 15. Binary Number Manipulation / Bitwise Operators
    print (32>>5)         #0000 0000 0010 0000 >>5  output: 1
    print (2>>1>>1>>1)    #0000 0000 0000 0010 >>3  output: 0
    print (5<<2<<1<<1<<2) #0000 0000 0000 0101 <<6  output: 0000 0001 0100 0000 = 320
    
    print (128|127)       #1000 0000 | 0111 1111 = 1111 1111    Output: 255  
    print (128&127)       #1000 0000 & 0111 1111 = 0000 0000    Output: 0    
    print (128^127)       #1000 0000 ^ 0111 1111 = 1111 1111    Output: 255  
    print (~0)            # -1

## Lecture 16. Basic String Manipulation
    string = 'God Bless America'
    print(string[0:9])                       # God Bless   # String Cutting
    word='Ford' 
    word= 'L' +word[1:]
    print (word)
    print (len(string))                      # 17          # Length of the String
    print(string[len(string)-7:len(string)]) # America     # String Cutting
    print(string[-1])                        # a 
    #string[0]='a' #Not allowed              # list elements accessed using index are immutable (read only)
    string='a'                               # but string itself is not 
    string2=''                               # ok
    string2=()                               # ok because string is a list of characters in Python
    string2=2 * ('New ' + 'York ')           # Concatenationa  and repeating   
    print(string2)                           # Concatenation Concatenation 
    print (type(string2))                    # prints class template name <class 'str'>
    con = 'con';cat = 'catenate';print (con +cat)
    
## Lecture 17. Using the format Method
    print ("Today I had {0}{1}{2}{3}{4}{5} cups of {6}".format( 0, 1, 2, 3, 4, 5, "cofee") )  #Position 
    str1="The {vehicle} had {0} or {1} crashes in last {2}-{3} months".format(0,1,2,3,  vehicle="car") #Position & name
    print (str1)
    print('prices: {x},{y},{z}'.format(x=1,y=2,z=3)) #its also a way to dynamically replace portions/characters inside a string
    print('{:>60}'.format(str1))     # Right aligned formatted Printing up to length of 60
    print('{:b}'.format(255))         # Binary format printing
    print('{:o}'.format(255))         # Octal format printing
    print('{:x}'.format(255))         # Hexadecimal format printing

    """
##Lecture 18. Specific Characters '
    ##Strings
    #str="I'm a \"string\" in 'Python'"; print (str)  # I'm a "string" in 'Python'
    #str='I\'m a "string" in \'Python\''; print (str) # I'm a "string" in 'Python'
    ## Multi Line Free form Text
    #str="""Hello
    #                New\
    #        World"""; print (str)    #Hello
    #                                 #                New        World
        
    """
##### Section7 Branching in Python
##Lecture 19. Logical Operators and Conditional Statements
    # < > <= >= != ==  not end or
    print (10 <6)          # False
    print (2==2)           # True
    print ('abc' == 'abc') # True
    print (not True)       # False
   
    print("")


##Lecture 20. if statement
    # To determine which part of the code will be executed next
    passerby_speech=''
    if passerby_speech == 'Hello' or passerby_speech == 'hi' :
    	print("Hi, how are you")
    else:
    	print("Howdy")          # Howdy
       
   
## Lecture 21. if else statement
    if 5<7 :
        if 5>6:
    	    print ("5>6")
        else:
            print('5<=6')		# 5<=6

## Lecture 22. ifelif Statement
    passerby_speech='Hi'
    if passerby_speech == 'Hello' or passerby_speech == 'hi' :
    	print("Hi, how are you")
    elif passerby_speech == 'Hi':
    	print("Hey")          # Hey
    
    
## Lecture 23. Ternary operator
    passerby_speech='Hello'
    my_response= "Hi" if (passerby_speech == "Hello" or passerby_speech == "Hi") else "Hey"
    print (my_response)
    

## Lecture 24. For Loop part 1
    # Loops are blocks of code which are executed a number of Times based on controlling variable/iterater
    # for, while, break, continue
    start=1
    stop=10
    step=2
    for i in range(start,stop,step):
    	if (i<=stop-step):
    		print (i, end=',')  # 1,3,5,7,
    	else:
    		print (i)           # 9
    
    
## Lecture 25. For Loop part 1
    string = "cat"
    for i in range(len(string)):
    	print(string[i])
    # c
    # a
    # t
    
    for i in string:
    	print(i)	  #same results
    
    for i in range(2):
        for j in (range(2)):
            print(i*j) 



    # Python Tutorial for Beginners 2: Strings - Working with Textual Data 
    greeting='hello, World!   '
    print(greeting.strip())
    print(greeting.lower())
    print(greeting.upper())
    print(greeting.capitalize())
    print(greeting.replace('World', 'Universe'))
    print(greeting.find('Bello'))   # -1
    
    greeting='Hello'
    name='Michael'
    message= '{}, {}. Welcome!'.format(greeting, name)
    print(message)
    message= f'{greeting}, {name.upper()}. Welcome!'
    print(message)
    #print(dir(name))  # Lists all methods
    print(help(str.capitalize))  # Gives detailed documentation of Methods
   
    # Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data
    # Arithmatic Operators
    # + - / *
    # Floor Division 7 // 2  = 3
    # Modulus Division  7 % 2  = 1
    
    # Comparison Operators => Return Boolean
    # IsEqual          3 == 2     # False
    print(3==2)
    # NotEqual         3 != 2     # True
    print(3!=2)
    # Greater than     3 >  2     # True
    # Less than        3 <  2     # False
    # Greater or Equal 3 >= 2     # True
    # Less or Equal    3 <= 2     # False

    # Python Tutorial for Beginners 4: Lists, Tuples, and Sets
    print('--Python Tutorial for Beginners 4: Lists, Tuples, and Sets')
    nums=[0,1,2,3,4,5,6,7,8,9,10]
    print(n for n in nums)                 # <generator object <genexpr> at 0x00000000036189A8>
    print(n for n in enumerate(nums))      # <generator object <genexpr> at 0x00000000036189A8>
    
    print(nums)                            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(n for n in nums))           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print([n for n in nums])               # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(map(lambda n: n,nums))           # <map object at 0x0000000003092B38>
    print(list(map(lambda n: n,nums)))     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #slicing Video# list[start_index : end+1_index : step]
    print("--slicing Video# list[start_index : end+1_index : step]")
    
    print(nums[0:11:1])                    # [0,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #                    Positive Indices:    0,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    #                    Negative Indices:  -11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1 <-LAST


    print(nums[0:])                        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[:])                         # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[-11:11])                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[-11:11:1])                  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(nums[-11:200:])                  # [0]
    print(nums[-8:8])                      # [3, 4, 5, 6, 7]
    print(nums[::-1])                      # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] reverses the list
    print(nums[7:11])

    """ 


    """
    Here's the summary:
    1. Know how to code on whiteboard/white paper.
    2. know the control flow in python like loops, if statement, switch statement etc
    3. Know the basic built-in data structure like list, tuple, dictionary also know how and when to use them.
    4. Be able to discuss how you've used python in your projects
    5. Fundamental problems in python(based on data structures and algorithms)
    6. Know how to use list comprehension, why it is fast?
    7. Know how to use generators(Why generators are efficient?)
    8. Learn basics of Object Oriented Programming.
    9. Prepare some question for the interviewer.
    10. Know some other fundamental technologies like git etc.
    """        


    a=[0, 1, 4, 5, 6, 7, 8, 9, 10]
    b=[2, 3, 4, 5, 6, 7]

    c=[i for i in a for j in b if (i==j)]

    print (c)
