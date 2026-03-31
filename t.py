import os

cr=b'\x0D'.decode("iso-8859-1")
lf=b'\x0A'.decode("iso-8859-1")

fd=open('D:\\tdm_automation\\pybin\\xax','w+')
fd.write( "DEVESH"+cr)


#==========================

try:
    with open('D:\\tdm_automation\\pybin\\t.txt',mode='r', encoding="iso-8859-1") as f:
        for line1 in f:
            #line2 = f.next()
            # process line1 and line2 here
            line1=line1.replace("\r",'')
            print(line1,end="")
except StopIteration:
    print ("End") # do whatever you need to do with line1 alo