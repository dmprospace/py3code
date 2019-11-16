#multithreaded_job.py
#########################################################################
# Module name :  multithreaded_job.py
# Description :  This is Master Demo Script to run number of Jobs as its child
#                  - Its a multithreaded script that iterates over a list of M jobs
#                     and at any given time runs N Jobs in Parallel, until all are done
#                   ( N = number defined SLOTS in Job Configuration )
# Author      :  Devesh Mohnani   
# Changes     : Developer  ~    Date    ~   Change  
#              Devesh Mohnani   09/26/2018   Initial Version
#########################################################################

from multiprocessing import Manager, Process, Lock, Queue
#from threading import Thread #Process, Lock, Queue
from subprocess import *
import time 
import os
import re
import random
import glob
from datetime import timedelta
from datetime import datetime
from my_pylib import m_config
from my_pylib import j_config
from my_pylib import table
from my_pylib import logger

#-------------------------------------------------
def refresh_slot(ns, action, slot, jobname, G, p, summary, rv ):
    GPREV=[]
    flag=0
    for i in G:
        GPREV.append(i)

    if(action=='A'):
        G[slot]=jobname
    elif(action=='R'):
        G[slot]=''
        FD=open('..\\logs\\live_job_run_summary.log','a')
        FD.write(summary + "\n")
        FD.close()        
        if(rv ==0):
            FD=open('..\\logs\\config_job_completed.txt','a')
            FD.write(jobname + "\n")
            FD.close()
    elif(action=='S'):
        ns.M=''
        i=0
        for i in range(ns.max_slots):
            if (i==0):
                ns.M=G[i]
            else:
                ns.M=ns.M + ',' + G[i]
    i=0
    while (i < len(G)):
        if(GPREV[i] != G[i]):
            flag=1
        i=i+1
    if (flag==1):
        FD=open('..\\logs\\' + 'slot_status_'+str(p)+'.log','a')
        FD.write(datetime.now().strftime('%Y-%m-%d  %H:%M:%S') + "  :  " + str(G) + "\n")
        FD.close()
#-------------------------------------------------
def run_job( ns, slot, jobname, cmdline, ttracker, absi, returncd, starttme, end_time, bprocess, thelog, p, lfh, L, G ):
    L.acquire()
    refresh_slot(ns, 'A', slot, jobname, G, p, '', 0)
    L.release()
    
    starttme[absi] = time.time()
    stt1=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    thelog[absi]="..\\logs\\sl_"+str(slot+1)+"_tb_"+ str(absi+1) + "_" + jobname +"_"+os.environ['USERNAME']+"_"+str(p)+"_"+datetime.now().strftime('%Y_%m_%d-%H_%M_%S')+".log"
    print("Running Job:  ["+ datetime.now().strftime('%Y-%m-%d %H:%M:%S') +"] ---> "+ jobname + "("+str(absi+1)+") @ slot("+str(slot+1)+")" )
    returncd[absi]=0
    time.sleep(1)
    try:
        dnt=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cmdline=cmdline+'   >>'+thelog[absi] +' 2>&1'
        stdout=check_output(cmdline,shell=True,stderr=STDOUT)
        time.sleep(1)
    except CalledProcessError as err:
        lfh[absi]=open(thelog[absi], 'a')
        lfh[absi].write('ERROR: ' + jobname + "\n\n" + str(err) +"\n\n")
        returncd[absi]=5555
    #finally:
        #print(returncd[absi])
        #time.sleep(1)
    if(returncd[absi] >0):
        print(" "*59+jobname+"("+str(absi+1)+") @ slot (" + str(slot+1) + ")"+" <------------ Failed:  ["+ datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]")
    else:
        print(" "*59+jobname+"("+str(absi+1)+") @ slot (" + str(slot+1) + ")"+" <------------ Success: ["+ datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"]")
    end_time[absi] = time.time()
    ett1=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ttracker[absi]=int(end_time[absi] - starttme[absi])
    if (returncd[absi]==0):
        rvline=jobname +"~XXYYZZ~" +str(absi+1)+ "~" +str(slot+1) +"~" + str(returncd[absi]) + "~" + str(ttracker[absi]) + "~" + stt1 + "~" + ett1
        cmdx="echo "+rvline+ " >>" + thelog[absi]
        os.system(cmdx)
        line=rvline.rstrip()
        val_list=line.split('~')
        summary=val_list[0] + "\t" + val_list[2] + "\t" + val_list[3].rstrip() + "\t" + val_list[4].rstrip() + "\t" + val_list[5].rstrip()+ "\t" + val_list[6] + "\t" + val_list[7]
    else:
        rvline=jobname +"~XXYYZZ~" +str(absi+1)+ "~" +str(slot+1)+ "~" + '5555' + "~" + str(ttracker[absi]) + "~" + stt1 + "~" + ett1
        lfh[absi].close()
        cmdx="echo "+rvline+ " >>" + thelog[absi]
        os.system(cmdx)
        line=rvline.rstrip()
        val_list=line.split('~')
        summary=val_list[0] + "\t" + val_list[2] + "\t" + val_list[3].rstrip() + "\t" + val_list[4].rstrip() + "\t" + val_list[5].rstrip()+ "\t" + val_list[6] + "\t" + val_list[7]
        
    time.sleep(1)
    L.acquire()
    refresh_slot(ns, 'R', slot, jobname, G, p, summary, returncd[absi])
    L.release()
    
#-------------------------------------------------

if __name__ == '__main__':
    mgr=Manager()
    ns=mgr.Namespace()
    G =mgr.list() #Global
    L =mgr.Lock()

    ns.M=''
    n=random.randint(900001,999999)
    m=random.randint(1,999)
    p=n*m
    start=time.time()
    gstarttm1=datetime.now().strftime('%Y.%m.%d  %H:%M:%S')
    os.system("cls")
    print("job_run Starting: " + gstarttm1)
    c=m_config('master_job_configuration.txt')
    print ("Configuration : "+c.job_list)
    print ("Parallel Slots in this run: " + c.slots)
    
    ns.max_slots=int(c.slots)
    jc          = j_config(c)
    jnme_list   = jc.jnme_list
    cmdline_list= jc.jcmd_list
    
    print("Tables Count in this run : " + str(len(jnme_list)))
    if (ns.max_slots >= len(jnme_list)):
        ns.max_slots=len(jnme_list)

    jobname=''
    curr_idx=0
    thelog=list(range(len(jnme_list)))
    lfh     =list(range(len(jnme_list)))
    bprocess=list(range(len(jnme_list)))
    ttracker=list(range(len(jnme_list)))
    returncd=list(range(len(jnme_list)))
    starttme=list(range(len(jnme_list)))
    end_time=list(range(len(jnme_list)))
    slot    = list(range(ns.max_slots))
    def f(x):
        return('')
    G=mgr.list(range(ns.max_slots))
    i=0
    for i in G:
        G[i]=''

    ch_list= list(range(ns.max_slots))
    run_ch_job_list=[]               
    i=0
    for elem in returncd:
        returncd[i]=1
        i=i+1
    # Initilize List of job running in parallel
    for idx in list(range(ns.max_slots)):
        run_ch_job_list.append(jnme_list[idx])
    curr_idx=idx    

    # Main
    print ("Main Process ID: "+str(os.getpid()))
    subscript=0
    
    FD=open('..\\logs\\live_job_run_summary.log','w')
    FD.write('')
    FD.write('JOBNAME' + "\t" +'ORDER' + "\t" +'SLOT' + "\t" + 'BATCH_RTN_CD' + "\t" + 'TIME_TAKEN' + "\t" + 'START_TIME' + "\t" + 'END_TIME' + "\n" )
    FD.close()  

    FD=open('..\\logs\\config_job_completed.txt','w')
    FD.write('')
    FD.close()  
    # Start Children
    for jobname in run_ch_job_list:
        ch_list[subscript]=Process(target=run_job, args=( ns, slot[subscript], jobname, cmdline_list[subscript], ttracker, subscript,returncd,starttme,end_time,bprocess,thelog,p,lfh,L, G  )) 
        ch_list[subscript].start()
        subscript=subscript+1
        time.sleep(1)
    curr_idx=subscript

    if (ns.max_slots < len(jnme_list)):    
        while (curr_idx<= len(jnme_list)-1 and ns.max_slots !=0):
            time.sleep(5)
            L.acquire()
            refresh_slot(ns, 'S', 0, '', G, p, '', 0)
            L.release()
            for idx in list(range(ns.max_slots)):
                if (G[idx] == '' and curr_idx <= len(jnme_list)-1):
                    jobname=jnme_list[curr_idx]
                    ch_list[idx]=Process(target=run_job, args=( ns, slot[idx], jobname, cmdline_list[idx], ttracker, curr_idx, returncd,starttme,end_time,bprocess,thelog,p,lfh,L, G ))
                    ch_list[idx].start()
                    time.sleep(1)
                    curr_idx=curr_idx+1
                elif(curr_idx > len(jnme_list)-1):
                    break
                else:
                    pass    
    # Wait for all children to finish
    for ch in ch_list:
       ch.join()
       

    idx=0
    # log analysis
    for t in jnme_list:
        #print (str(jnme_list[idx])  +' : ' + str(returncd[idx]) + ' : ' + str(ttracker[idx]))
        idx=idx+1
    path="..\\logs\\"
    scriptbase = re.sub(r'\..*?$', "", __file__)
    scriptbase = scriptbase + "_" +os.environ['USERNAME']+"_"+str(p)+ '.py'
    tlog=logger(scriptbase,0)
    tlog.logit("job_run Summary: " + gstarttm1)
    tlog.logit('TABLE' + "\t" +'ORDER' + "\t" +'SLOT' + "\t" + 'BATCH_RTN_CD' + "\t" + 'TIME_TAKEN' + "\t" + 'START_TIME' + "\t" + 'END_TIME')
    i=0
    for jobname in jnme_list:
        for filename in glob.glob("..\\logs\\"+'*' +"_"+os.environ['USERNAME']+"_"+str(p)+'*'):
                    FD=open (filename,'r')
                    #'JOB-XXYYZZ-9009-7' 
                    for line in FD: 
                        if (re.match(r'^'+jobname+'~XXYYZZ~',line)):
                            line=line.rstrip()
                            val_list=line.split('~')
                            ttracker[i]=int(val_list[3].rstrip())
                            tlog.logit(val_list[0] + "\t" + val_list[2] + "\t" + val_list[3].rstrip() + "\t" + val_list[4].rstrip() + "\t" + val_list[5].rstrip()+ "\t" + val_list[6] + "\t" + val_list[7] )
                    FD.close()
        i=i+1
    end=time.time()
    gendtm1=datetime.now().strftime('%Y.%m.%d  %H:%M:%S')
    wt=int(end-start)
    print ("job_run Completed:" + gendtm1)
    tlog.logit ("job_run Completed:" + gendtm1)
    print ("Total Wall Clock Time elapsed:- "+ str(wt) + " seconds")
    att=sum(t for t in ttracker)
    print ("CPU Time elapsed:- "+ str(att) + " seconds")
