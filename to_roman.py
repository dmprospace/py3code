class intToRoman:
    def __init__(self):
        pass;
        
    def intToRoman(self, num):
        str=""
        if(not (num>=3999 or num<1)):
            u=["I","II","III","IV","V","VI","VII","VIII","IX","X"];
            t=["X","XX","XXX","XL","L","LX","LXX","LXXX","XC","C"];
            h=["C","CC","CCC","CD","D","DC","DCC","DCCC","CM","M"];
            i=num%10
            temp=num-i
            j=temp%100
            temp=temp-j
            k=temp%1000
            temp=temp-k
            for l in range(1000, temp+1, 1000):
                str=str+'M'
            
            k=int(k/100)
            j=int(j/10)
            
            if(k!=0):
                str=str+h[k-1]
            if(j!=0):
                str=str+t[j-1]
            if(i!=0):
                str=str+u[i-1]
        return(str)


if __name__ == '__main__':
    s=intToRoman()
    #print(s.intToRoman(1)   )
    #print(s.intToRoman(2)   )
    #print(s.intToRoman(3)   )
    #print(s.intToRoman(4)   )
    #print(s.intToRoman(5)   )
    #print(s.intToRoman(10)  )
    #print(s.intToRoman(20)  )
    #print(s.intToRoman(30)  )
    #print(s.intToRoman(40)  )
    #print(s.intToRoman(50)  )
    #print(s.intToRoman(100) )
    #print(s.intToRoman(200) )
    #print(s.intToRoman(300) )
    #print(s.intToRoman(400) )
    #print(s.intToRoman(500) )
    print(s.intToRoman(1000))
    print(s.intToRoman(2221))
    print(s.intToRoman(3000))
    print(s.intToRoman(3999))
    print(s.intToRoman(5000))
        
        
