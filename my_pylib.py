#my_pylib.py
#########################################################################
# Module name :  my_pylib.py
# Description :  My Python Class Library 
# Author      :  Devesh Mohnani   
# Changes     :  09/30/2018 Initial Version 
#               Developer   ~    Date    ~   Change
#                Devesh     09/26/2018     Initial Version v1.0
#########################################################################

import os
import re
from datetime import timedelta, datetime
import time
import pyodbc

#########################################################################
"""
class logger
"""
class logger:
    def __init__ (self, caller, timeflag):
        self.caller=caller
        scriptname=os.path.basename(caller)
        scriptbase = re.sub(r'\..*?$', "", scriptname)
        scriptextn = 'py'
        dttm=datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        if(timeflag==0):
            self.logfile='..' + '\\logs\\'  + scriptbase + "_" + scriptextn + ".log"
            self.handle=open(self.logfile, 'a')
            self.handle.write('--------------------------------------------------------------------' + "\n")
            self.handle.write(datetime.now().strftime('[%H:%M:%S  %Y/%m/%d]: ')+"\n")
        else:
            self.logfile='..' + '\\logs\\'  + scriptbase + "_" + scriptextn + "-" + str(dttm) + ".log"
            self.handle=open(self.logfile, 'w')
            print(datetime.now().strftime('[%H:%M:%S]: ') + "Starting Log for... " + caller)
            print(datetime.now().strftime('[%H:%M:%S]: ') + '-------------------------------------------------------------------')
            print(datetime.now().strftime('[%H:%M:%S]: ') + "Logfile:" + self.logfile)
            self.handle.write(datetime.now().strftime('[%H:%M:%S]: ') + "Starting Log for... " + caller + "\n" )
            self.handle.write(datetime.now().strftime('[%H:%M:%S]: ') + '-------------------------------------------------------------------' + "\n")
       
    """#########################################################
    # Description Message Logging in the Log
    # Function Name   : logit (Log it)
    """
    def logit (self,msg,stamp=0):
        if(stamp==1):
            self.handle.write(datetime.now().strftime('[%H:%M:%S]: ') + msg + "\n" )
        else:
            self.handle.write(msg + "\n" )
    """#########################################################
    # Description Message Logging in the Log & prints on Screen
    # Function Name   : logpit (Log and Print it)
    """
    def logpit (self,msg,stamp=0):
        if(stamp==1):    
            print (datetime.now().strftime('[%H:%M:%S]: ') + msg )
            self.handle.write(datetime.now().strftime('[%H:%M:%S]: ') + msg + "\n" )            
        else:
            print (msg)        
            self.handle.write(msg + "\n" )

    """#########################################################
    # Auto closing the Log File using handle
    """
    def __del__(self):
#        self.handle.write(datetime.now().strftime('[%H:%M:%S]: ') + '-------------------------------------------------------------------' + "\n")
        print("Logfile:" + self.logfile)
        self.handle.close()
#########################################################################
"""
class table
"""
class table:
    def __init__ (self,schema,tname):
        self.schema=schema
        self.tname=tname


    def count(self,dsn,user,pswd):
        connection = pyodbc.connect('DSN='+ dsn + ';Uid=' + user + ';Pwd=' + pswd)
        cursor = connection.cursor()
        SQLCommand = ("select '"+ self.tname + "' AS TABLE_NAME, COUNT(*) as REC_COUNT FROM " + self.schema + "." + self.tname +";")
        cursor.execute(SQLCommand)
        rs_list=cursor.fetchall()
        rs_tuple=rs_list[0]
        return(int(rs_tuple[1]))
        return(rs_list)
        
    def truncate(self,dsn,user,pswd):
        connection = pyodbc.connect('DSN='+ dsn + ';Uid=' + user + ';Pwd=' + pswd)
        cursor = connection.cursor()
        SQLCommand = ("truncate table " + self.schema + "." + self.tname +";")
        cursor.execute(SQLCommand)
        rs_list=cursor.fetchall()
        return(rs_list)


########################################################################################
"""
class master config
"""
class m_config:
    #Master Configuration initializer 
    def __init__(self,mfile):
        self.cfg='..\\configuration\\'+ mfile
        FD=open (self.cfg,'r')
        for line in FD: 
            line=line.rstrip()
            line=line.lstrip()
            if (not(re.match(r'^[\s]*#',line) or re.match(r'^[\s]*$',line))):
                val_list=line.split(':')
                i=0
                for v in val_list:
                    val_list[i]=val_list[i].lstrip()
                    val_list[i]=val_list[i].rstrip()
                    val_list[i]=re.sub(r'"|\[|\]','',val_list[i],re.IGNORECASE)
                    i=i+1
                if(re.search('Job_List', val_list[0], re.IGNORECASE)):
                    self.job_list=val_list[1]
                elif(re.search('Max_Slots', val_list[0], re.IGNORECASE)):
                    self.slots=val_list[1]

########################################################################################
"""
class job config
"""
class j_config:
    # Populates in job name & command line list based on configuration object 
    def __init__(self,c):
        FN='..\\configuration\\' + c.job_list
        FD=open (FN,'r')
        self.jnme_list=[]
        self.jcmd_list=[]
        for line in FD: 
            line=line.rstrip()
            line=line.lstrip()
            if (not(re.match(r'^[\s]*#',line) or re.match(r'^[\s]*$',line))):
                x = line.split("=")
                self.jnme_list.append(x[0].strip())
                self.jcmd_list.append(" ".join(x[1:]))
        FD.close()
########################################################################################
"""
class f_lines
"""
class f_lines:
    # loads file lines in a list
    def __init__(self,s):
        FN='..\\configuration\\' + s
        FD=open (FN,'r')
        self.line_list=[]
        for line in FD: 
            line=line.strip()
            if (not(re.match(r'^[\s]*#',line) or re.match(r'^[\s]*$',line))):
                self.line_list.append(line)
########################################################################################
def file_to_list(file_path):
    '''
    Description: places each row of text file into a python list
    Method Name: file_to_list
    Input: file name to be read
    output: text file rows in a python list
    '''    
    file_path = '..\\table_count_tracker' + file_name
    out_list = []
    time.sleep(1)
    print("Reading {}...".format(file_name))
    with open(file_path,mode='r') as txt_file:
        for line in txt_file:
            out_list.append(line.strip())
    time.sleep(1)
    print("Finished reading {}.\n".format(file_name))
    return out_list
    
#######################################################################################

