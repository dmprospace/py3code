#gtopt.py
import sys
import getopt


def get_command_line_args():
    argv=sys.argv[1:]
    start_date=None
    end_date=None
    unixOptions="s:e:cho:v"                    # String  (:) > value required after
    gnuOptions=["help", "output=", "verbose"]  # A List  (=) > value required after
    print(argv)
    if(len(argv) >=1):
        #argv[0] is either python or scriptname
        #['-s', 'x', '-e', 'y', '-c', '--help', '--output=m']

        try:
            opts,vals= getopt.getopt(argv, unixOptions, gnuOptions)
        except:
            print()
            opts=[]
            vals=[]
    
        print ("opts   : ", opts)  # List of Tuples = Ordered Pairs/Sets = Key - Value Pair
        print ("argvals: ", vals)  # List of string elements
        
        #opts   :  [('-s', 'x'), ('-e', 'y'), ('-c', ''), ('--help', ''), ('--output', 'm')]
        #argvals:  []
        # Iterate over List of Tuples
    
        for opt, val in opts:
            if opt in ['-h','--help']:
                #usage()
                print("Usage: ")
            if opt in ['-s','--start']:            
                start = val
            if opt in ['-e','--end']:
                end = val
        print(start, end)
        #x y
    else:
        print("No Arguement Provided")
        pass
    # for opt, arg 
    
get_command_line_args()