# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:16:40 2019

@author: RussellTan
"""
import time
# This is a console that expresses a number into 3 palindromes
#start=time.time()
##### Everything above this row has yet to undergo testing
##### Everything below this row has gone through at least 1 round of testing
def str_to_lst():
    print("Pending")

def hex_display(res1,res2,res3,number):
    p1,p2,p3='','',''
    for i in range(0,len(res1)):
        p1=p1+hex(res1[i])[2:].upper()
    for j in range(0,len(res2)):
        p2=p2+hex(res2[j])[2:].upper()
    for k in range(0,len(res3)):
        p3=p3+hex(res3[k])[2:].upper()
    print(p1)
    print("+"+p2)
    print("+ "+p3)
    print("-"*len(p1))
    print(number)

def display():
    print("F")
        
def two_digit_sum(num_string,base):
    num=num_string
    if base<11:
        num=str_to_lst(num_string)
    num=num[::-1]
    if num[1]<=num[0]:
        p1=[num[1],num[1]]
        p2=[num[0]-num[1]]
        p3=[0]
    elif num[1]>num[0]+1:
        p1=[num[1]-1,num[1]-1]
        p2=[base+num[0]-num[1]+1]
        p3=[0]
    elif num[1]==num[0]+1:
        p1=[num[0],num[0]]
        p2=[base-1]
        p3=[1]
    if base>10:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)
    
def three_digit_sum(num,base):
    if base<11:
        num=str_to_lst(num)
    num=num[::-1]
    if num[2]<=num[0]:
        p1=[num[2],num[1],num[2]]
        p2=[num[0]-num[2]]
        p3=[0]
    elif num[2]>=num[0]+1:
        if num[1]!=0:
            p1=[num[2],num[1]-1,num[2]]
            p2=[base+num[0]-num[2]]
            p3=[0]
        else:
            if d(num[2]-num[0]-1,base)!=0:
                p1=[num[2]-1,base-1,num[2]-1]
                p2=[base+num[0]-num[2]+1]
                p3=[0]
            else:
                if num[2]>=3:
                    p1=[num[2]-2,base-1,num[2]-2]
                    p2=[111]
                    p3=[0]
                elif num[2]==2:
                    p1=[101]
                    p2=[base-1,base-1]
                    p3=[1]
                else:
                    p1=[base-1,base-1]
                    p2=[1]
                    p3=[0]
    num=num[::-1]
    if base>10:
        return hex_display(p1,p2,p3,num)
    else:
        return display(p1,p2,p3,num)

def front_display():
    print("****************************************************************")
    print("LET ME SHOW YOU SOMETHING\n\n")
    print("      THAT WILL BLOW YOUR MIND!!!\n\n")
    print("EVERY INTEGER CAN BE WRITTEN AS A SUM OF 3 PALINDROMES !!\n\n")
    print("****************************************************************")
 
def debug(message):
    print("debug "+str(message))
    
def main():
    front_display()
    base=int(input("Enter its base from 5 to 16 \n"))
    if base>10:
        perm_number=input("Enter the base-"+str(base)+" number ,format DEADBEEF without the 0x prefix\n")
        number=hex_int_to_lst(perm_number)
    else:
        perm_number=int(input("Enter your number\n"))
        number=hex_int_to_lst(perm_number)
    if number==number[::-1]:
        print("It is already a PALINDROME ! ! ! ")
    else:
        length=len(number)
        if length>6:
            res=main_algorithm(number,base)
        elif length==2:
            res=two_digit_sum(number,base)
        elif length==3:
            res=three_digit_sum(number,base)
    print(res[0])
    print(res[1])
    print(res[2])
    print("\n ---Initialising Appropriate Printing Format---\n")
    hex_display(res[0],res[1],res[2],perm_number)
    return 0
        #This will 
def main_algorithm(number,base):
    length=len(number)
    odd=(length%2!=0)
    [types,config,special]=check_type(number,base)
    #state is another word for type
    if length>=7:
        if types=="A1" or types=="A2" or types=="A3" or types=="A4":
            if odd:
                res=algorithm_1(number,config,base,types)
            elif not special:
                res=algorithm_2(number,config,base,types)
            else:
                res=algorithm_5(number,config,base)
        elif types=="A5" or types=="A6":
            if not odd:
                res=algorithm_1(number,config,base,types)
            elif not special:
                res=algorithm_2(number,config,base,types)
            else:
                res=algorithm_5(number,config,base)
        elif types=="B1" or types=="B2" or types=="B3" or types=="B4" or types=="B5" or types=="B6" or types=="B7":
            if odd:
                res=algorithm_3(number,config,base)
            elif not special:
                res=algorithm_4(number,config,base)
            else:
                res=algorithm_5(number,config,base)
    return res
    
                
def big_sub(digits,s,base):
    #digits in [13,12,1,1,0,2,4]
    #s in [1,1,0,0,0,0,]
    for i in range(0,len(digits)):
        digits[i]-=(s[i] | 0)
        while digits[i]<0:
            digits[i]+=base
            digits[i+1]-=1
    while len(digits)==0 and digits[len(digits)-1]==0:
        digits.pop()
    return digits
    
def check_type(number,base):
    num=number
    l=len(number)
    m=l>>1
    test_num=num[::-1]
    special=(test_num[m]==0 or test_num[m-1]==0)
    #number is not inverted, but in proper position
    if d(int(num[-1])-int(num[0])-int(num[1])+1,base) != 0 and ( int(num[1])!=0 and int(num[1])!=1 and int(num[1])!=2):
        print("This is an A1 type of number")
        types="A1"
        p1=[int(num[0])] #Palindrome 1
        p2=[int(num[1])-1] #Palindrome 2
        p3=[d(int(num[-1])-int(num[0])-int(num[1])+1,base)]#Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif d(int(num[-1])-int(num[0])-int(num[1])+1,base)==0 and (int(num[1])!=0 and int(num[1])!=1 and int(num[1])!=2):
        print("This is an A2 type of number")
        types="A2"
        p1=[int(num[0])] #Palindrome 1
        p2=[int(num[1])-2] #Palindrome 2
        p3=[1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif d(int(num[-1])-int(num[0])+2,base)!=0 and (int(num[1])==0 or int(num[1])==1 or int(num[1])==2) and int(num[0])!=1:
        print("This is an A3 type of number")
        types="A3"
        p1=[int(num[0])-1] #Palindrome 1
        p2=[base-1] #Palindrome 2
        p3=[d(int(num[-1])-int(num[0])+2,base)] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif d(int(num[-1])-int(num[0])+2,base)==0 and (int(num[1])==0 or int(num[1])==1 or int(num[1])==2) and int(num[0])!=1:
        print("This is an A4 type of number")
        types="A4"
        p1=[int(num[0])-1] #Palindrome 1
        p2=[base-2] #Palindrome 2
        p3=[1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif d(int(num[-1])-int(num[2]),base)!=0 and int(num[2])<=3 and int(num[1])==0 and int(num[0])==1:
        print("This is an A5 type of number")
        types="A5"
        p1=[base-1] #Palindrome 1
        p2=[int(num[2])+1] #Palindrome 2
        p3=[d(int(num[-1])-int(num[2]),base)] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==1))
        return [types,config,special]
    elif d(int(num[-1])-int(num[2]),base) ==0 and int(num[2])<=2 and int(num[1])==0 and int(num[0])==1:
        print("This is an A6 type of number")
        types="A6"
        p1=[base-1] #Palindrome 1
        p2=[int(num[2])+2] #Palindrome 2
        p3=[base-1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==1))
        return [types,config,special]
    elif d(int(num[-1])-int(num[2]),base)!=0 and int(num[2])>=4 and int(num[1])<=2 and int(num[0])==1:
        print("This is a B1 type of number")
        types="B1"
        p1=[1,int(num[1])] #Palindrome 1
        p2=[int(num[2])-1] #Palindrome 2
        p3=[d(int(num[-1])-int(num[2]),base)] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif d(int(num[-1])-int(num[2]),base)==0 and int(num[2])>=3 and int(num[1])<=2 and int(num[0])==1:
        print("This is a B2 type of number")
        types="B2"
        p1=[1,int(num[1])] #Palindrome 1
        p2=[int(num[2])-2] #Palindrome 2
        p3=[1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif int(num[-1])==0 and (int(num[2])==0 or int(num[2])==1 ) and (int(num[1])==2 or int(num[1])==1 ) and int(num[0])==1:
        print("This is a B3 type of number")
        types="B3"
        p1=[1,int(num[1])-1] #Palindrome 1
        p2=[base-2] #Palindrome 2
        p3=[1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif int(num[-1])==0 and (int(num[2])==2 or int(num[2])==3 ) and (int(num[1])==2 or int(num[1])==1 ) and int(num[0])==1: 
        print("This is a B4 type of number")
        types="B4"
        p1=[1,int(num[1])] #Palindrome 1
        p2=[base-2] #Palindrome 2
        p3=[1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif int(num[-1])!=0 and (int(num[2])==0 or int(num[2])==1 or int(num[2])==2) and (int(num[1])==1 or int(num[1])==2) and int(num[0])==1:
        print("This is a B5 type of number")
        types="B5"
        p1=[1,int(num[1])-1] #Palindrome 1
        p2=[base-1] #Palindrome 2
        p3=[int(num[-1])] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif d(int(num[-1])-3,base)!= 0 and int(num[2])==3 and (int(num[1])==1 or int(num[1])==2) and int(num[0])==1:
        print("This is a B6 type of number")
        types="B6"
        p1=[1,int(num[1])] #Palindrome 1
        p2=[2] #Palindrome 2
        p3=[d(int(num[-1])-3,base)] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    elif int(num[-1])==3 and int(num[2])==3 and (int(num[1])==1 or int(num[1])==2) and int(num[0])==1:
        print("This is a B7 type of number")
        types="B7"
        p1=[1,int(num[1])] #Palindrome 1
        p2=[1] #Palindrome 2
        p3=[1] #Palindrome 3
        config=[p1,p2,p3]
        special=(special and (l%2==0))
        return [types,config,special]
    else:
        print("Indeterminate type")
        types=None
        return [types,0,False]

def d(num,base):
    return num%base

def hex_int_to_lst(num):
    hex_to_dec={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0}
    lst=[]
    reck=str(num)
    for i in reck:
        lst.append(hex_to_dec[i])
    return lst

def lst_to_hex_int(num_list):#input=[10,13,14,0,0,0,12,5];output=ADE000C5
    string_hex=''
    for integer in num_list:
        string_hex=string_hex+hex(int(integer))[2:].upper()
    return string_hex

def algorithm_1(number,config,base,types):
    debug("Algorithm _ 1")
    if types=="A5" or types=="A6":
        number=number[1:]
    else:
        pass
    rev_num=number[::-1]
    num=number
    length=len(num)
    m=length>>1
    x,y,z=config[0],config[1],config[2]
    x=[0]+x
    y=[0]+y
    z=[0]+z
    c=[0,(x[1]+y[1]+z[1])//base]
    x.append(d(rev_num[2*m-1]-y[1],base) if z[1]<=(rev_num[2*m-2]-1) else d(rev_num[2*m-1]-y[1]-1,base))
    y.append(d(rev_num[2*m-2]-z[1]-1,base))
    z.append(d(rev_num[1]-x[2]-y[2]-c[1],base))
    c.append((x[2]+y[2]+z[2]+c[1]-rev_num[1])//base)
    for i in range(3,m+1):
        x.append(1 if z[i-1]<=rev_num[2*m-i]-1 else 0)
        y.append(d(rev_num[2*m-i]-z[i-1]-1,base))
        z.append(d(rev_num[i-1]-x[i]-y[i]-c[i-1],base))
        c.append((x[i]+y[i]+z[i]+c[i-1]-rev_num[i-1])//base)
    x.append(0)
    if c[m]==1:
        debug("No Adjustment needed")
        print("Nothing")
    elif c[m]==0:
        debug("c[m]=0")
        x[m+1]=1
    elif c[m]==2:
        debug("c[m]=2")
        if z[m]!= base - 1:
            y[m]-=1
            z[m]+=1
        else:
            x[m+1]=1
            y[m]-=1
            z[m]=0
    x=x[1:]
    y=y[1:]
    z=z[1:]
    y=y+y[::-1]
    t_x=x[::-1]
    t_z=z[::-1]
    x=x+t_x[1:]
    z=z+t_z[1:]
    config=[x,y,z]
    return config

def algorithm_2(number,config,base,types):
    debug("Algorithm_2")
    if types=="A5" or types=="A6":
        number=number[1:]
    else:
        pass
    num=number[::-1]
    length=len(num)
    m=length>>1
    x,y,z=config[0],config[1],config[2]
    x=[0]+x
    y=[0]+y
    z=[0]+z
    c=[0,(x[1]+y[1]+z[1])//base]
    x.append(d(num[2*m-2]-y[1],base) if z[1]<=num[2*m-3]-1 else d(num[2*m-2]-y[1]-1,base))
    y.append(d(num[2*m-3]-z[1]-1,base))
    z.append(d(num[1]-x[2]-y[2]-c[1],base))
    c.append((x[2]+y[2]+z[2]+c[1]-num[1])//base)
    for i in range(3,m):
        x.append(1 if z[i-1]<=num[2*m-i-1]-1 else 0)
        y.append(d(num[2*m-i-1]-z[i-1]-1,base))
        z.append(d(num[i-1]-x[i]-y[i]-c[i-1],base))
        c.append((x[i]+y[i]+z[i]+c[i-1]-num[i-1])//base)
    x.append(0)
    y.append(d(num[m-1]-z[m-1]-c[m-1],base))
    c.append((x[m]+y[m]+z[m-1]+c[m-1]-num[m-1])//base)
    if c[m]==1:
        print("do nothing")
    elif c[m]==0:
        if y[m]!=0:
            x[m]=1
            y[m]-=1
        else:
            if y[m-1]!=0:
                x[m]=1
                y[m]=base-2
                y[m-1]-=1
                z[m-1]+=1
            elif y[m-1]==0 and z[m-1]!=0:
                y[m]=1
                y[m-1]=1
                z[m-1]-=1
            elif y[m-1]==0 and z[m-1]==0:
                x[m-1]-=1
                x[m]=1
                y[m]=base-4
                y[m-1]=base-1
                z[m-1]=2
    elif c[m]==2:
        x[m]=1
        y[m-1]-=1
        y[m]=base-2
        z[m-1]=0
    x,y,z=x[1:],y[1:],z[1:]
    x,z=x+x[::-1],z+z[::-1]
    t_y=y[::-1]
    y=y+t_y[1:]
    config=[x,y,z]
    return config

def algorithm_3(number,config,base):
    debug("Algorithm_3")
    num=number[::-1]
    x,y,z=config[0],config[1],config[2]
    length=len(num)
    m=length>>1
    y=[0]+y
    z=[0]+z
    c=[0,(1+y[1]+z[1])//base]
    x.append(d(num[2*m-2]-y[1],base) if z[1]<= num[2*m-3]-1 else d(num[2*m-2]-y[1]-1,base))
    y.append(d(num[2*m-3]-z[1]-1,base))
    z.append(d(num[1]-x[1]-y[2]-c[1],base))
    c.append((x[1]+y[2]+z[2]+c[1]-num[1])//base)
    for i in range(3,m):
        x.append(1 if z[i-1]<=num[2*m-i-1]-1 else 0)
        y.append(d(num[2*m-i-1]-z[i-1]-1,base))
        z.append(d(num[i-1]-x[i-1]-y[i]-c[i-1],base))
        c.append((x[i-1]+y[i]+z[i]+c[i-1]-num[i-1])//base)
    x.append(0)
    y.append(d(num[m-1]-z[m-1]-x[m-1]-c[m-1],base))
    c.append((x[m-1]+y[m]+z[m-1]+c[m-1]-num[m-1])//base)
    if c[m]==1:
        print("do nothing")
    elif c[m]==0:
        x[m]=1
    elif c[m]==2:
        if y[m-1]!=0:
            if z[m-1]!= base-1:
                y[m-1]-=1
                y[m]-=1
                z[m-1]+=1
            else:
                x[m]=1
                y[m-1]-=1
                z[m-1]=0
        else:
            if z[m-1]!=base-1:
                x[m-1]-=1
                y[m-1]=base-1
                y[m]-=1
                z[m-1]+=1
            else:
                x[m-1]-=1
                x[m]=1
                y[m-1]=base-1
                z[m-1]=0
    y,z=y[1:],z[1:]
    t_x=x[::-1]
    t_x=t_x[1:]
    x=x+t_x
    z=z+z[::-1]
    t_y=y[::-1]
    t_y=t_y[1:]
    y=y+t_y
    config=[x,y,z]
    return config

def algorithm_4(number,config,base):
    num=number[::-1]
    x,y,z=config[0],config[1],config[2]
    length=len(num)
    m=length>>1
    y=[0]+y
    z=[0]+z
    c=[0,(1+y[1]+z[1])//base]
    x.append(d(num[2*m-3]-y[1],base) if z[1]<=num[2*m-4]-1 else d(num[2*m-3]-y[1]-1,base))
    y.append(d(num[2*m-4]-z[1]-1,base))
    z.append(d(num[1]-x[1]-y[2]-c[1],base))
    c.append((x[1]+y[2]+z[2]+c[1]-num[1])//base)
    for i in range(3,m-1):
        x.append(1 if z[i-1]<=num[2*m-i-2]-1 else 0)
        y.append(d(num[2*m-i-2]-z[i-1]-1,base))
        z.append(d(num[i-1]-x[i-1]-y[i]-c[i-1],base))
        c.append((x[i-1]+y[i]+z[i]+c[i-1]-num[i-1])//base)
    x.append(1 if z[m-2]<=num[m-1]-1 else 0)
    y.append(d(num[m-1]-z[m-2]-1,base))
    z.append(d(num[m-2]-x[m-2]-y[m-1]-c[m-2],base))
    c.append((x[m-2]+y[m-1]+z[m-1]+c[m-2]-num[m-2])//base)
    if x[m-1]+ c[m-1]==1:
        print("Do nothing")
    elif x[m-1]+c[m-1]==0 and y[m-1]!= base -1 :
        if z[m-1]!=0:
            y[m-1]+=1
            z[m-1]-=1
        elif z[m-1]==0 and y[m-2]!=0:
            if y[m-1]!=1 and z[m-2]!= base - 1:
                x[m-1]=1
                y[m-2]-=1
                y[m-1]-=1
                z[m-2]+=1
                z[m-1]+=1
            elif y[m-1]!=1 and z[m-2]==base - 1:
                x[m-1]=2
                y[m-2]-=1
                y[m-1]-=2
                z[m-2]=0
                z[m-1]=3
            elif y[m-1]==1:
                x[m-1]=1
                y[m-2]-=1
                y[m-1]=base - 1
                z[m-2]=0
                z[m-1]=3
        elif z[m-1]==0 and y[m-2]==0:
            if z[m-2]!= base - 1:
                x[m-2]-=1
                x[m-1]=1
                y[m-2]=base - 1
                y[m-1]-=1
                z[m-2]+=1
                z[m-1]=1
            elif z[m-2]== base - 1 and y[m-1]!=1:
                x[m-2]-=1
                x[m-1]=2
                y[m-2]=base-1
                y[m-1]-=2
                z[m-2]=0
                z[m-1]=3
            elif z[m-2]== base - 1 and y[m-1]==1:
                x[m-2]-=1
                x[m-1]=1
                y[m-2]=base-1
                y[m-1]=base-1
                z[m-2]=0
                z[m-1]=3
    elif x[m-1]+c[m-1]==0 and y[m-1]==base-1:
        x[m-1]=1
        y[m-2]-=1
        y[m-1]=base-2
        z[m-2]+=1
        z[m-1]=1
    elif x[m-1]+c[m-1]==2 and x[m-1]==0 and c[m-1]==2:
        if z[m-1]!=base-1:
            y[m-1]-=1
            z[m-1]+=1
        elif z[m-1]==base-1 and z[m-2]!=base-1:
            if y[m-2]!=0:
                x[m-1]=1
                y[m-2]-=1
                y[m-1]-=2
                z[m-2]+=1
                z[m-1]=1
            elif y[m-2]==0:
                x[m-2]-=1
                x[m-1]=1
                y[m-2]=base-1
                y[m-1]-=2
                z[m-2]+=1
                z[m-1]=1
        elif z[m-1]==base-1 and z[m-2]==base-1:
            if y[m-2]<base-2:
                if y[m-2]!=base-1:
                    x[m-2]-=1
                    x[m-1]=base-2
                    y[m-2]+=1
                    y[m-1]+=2
                    z[m-1]=base-2
                    z[m-2]=base-2
                else:
                    x[m-1]=base-2
                    y[m-2]=0
                    y[m-1]+=2
                    z[m-1]=base-2
                    z[m-2]=base-2
            else:
                if y[m-2]>=1:
                    x[m-1]=2
                    y[m-2]-=1
                    y[m-1]-=3
                    z[m-2]=0
                    z[m-1]=3
                else:
                    x[m-2]-=1
                    x[m-1]=2
                    y[m-2]=base-1
                    y[m-1]-=3
                    z[m-2]=0
                    z[m-1]=3
    elif x[m-1]+c[m-1]==2 and x[m-1]==1 and c[m-1]==1:
        if z[m-1]!=base-1 and y[m-1]!=0:
            y[m-1]-=1
            z[m-1]+=1
        elif z[m-1]!=base-1 and y[m-1]==0:
            x[m-1]=0
            y[m-1]=base-1
            z[m-1]+=1
        elif z[m-1]==base-1 and z[m-2]!=0:
            if y[m-2]!=base-1:
                x[m-1]=0
                y[m-2]+=1
                y[m-1]+=1
                z[m-2]-=1
                z[m-1]=base-2
            elif y[m-2]==base-1 and y[m-1]>1:
                x[m-1]=2
                y[m-2]=base-2
                y[m-1]-=2
                z[m-2]+=1
                z[m-1]=1
            elif y[m-2]==base-1 and y[m-1]==0:
                y[m-2]=base-2
                y[m-1]=base-2
                z[m-2]+=1
                z[m-1]=1
            elif y[m-2]==base-1 and y[m-1]==1:
                y[m-2]=base-2
                y[m-1]=base-1
                z[m-2]+=1
                z[m-1]=1 
        elif z[m-1]==base-1 and z[m-2]==0 and y[m-2]!=0:
            if y[m-1]>1:
                x[m-1]=2
                y[m-2]-=1
                y[m-1]-=2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==0:
                y[m-2]-=1
                y[m-1]=base-2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==1:
                y[m-2]-=1
                y[m-1]=base-1
                z[m-2]=1
                z[m-1]=1
        elif z[m-1]==base-1 and z[m-2]==0 and y[m-2]==0:
            if y[m-1]>1:
                x[m-2]-=1
                x[m-1]=2
                y[m-2]=base-1
                y[m-1]-=2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==0:
                x[m-2]-=1
                y[m-2]=base-1
                y[m-1]=base-2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==1:
                x[m-2]-=1
                y[m-2]=base-1
                y[m-1]=base-1
                z[m-2]=1
                z[m-1]=1
    elif x[m-1]+c[m-1]==3:
        y[m-1]-=1
        z[m-1]=0
    y,z=y[1:],z[1:]
    x,y=x+x[::-1],y+y[::-1]
    t_z=z[::-1]
    z=z+t_z[1:]
    config=[x,y,z]
    return config
        
def algorithm_5(number,config,base):
    debug("Algorithm 5")
    length=len(number)
    m=length>>1
    s=[0]*length
    s[m],s[m-1]=1,1
    rev_num=number[::-1]
    digits=big_sub(rev_num,s,base)
    if digits[m-1]==0 or digits[m]==0:
        s[m],s[m-1]=2,2
        rev_num=number[::-1]
        digits=big_sub(rev_num,s,base)
    res=digits[::-1]
    [t_types,t_config,t_special]=check_type(res,base)
    if t_types=="A5" or t_types=="A6":
        length_of_p1=length-1
    else:
        length_of_p1=length
    even=(length_of_p1%2==0)
    if even:
        result=main_algorithm(res,base)
    else:
        z1=d(res[-1]-res[2],base)
        if z1!=0:
            debug("Pseudo-B1")
            p1=[1,res[1]]
            p2=[res[2]-1]
            p3=[z1]
        elif z1==0:
            debug("Pseudo-B2")
            p1=[1,res[1]]
            p2=[res[2]-2]
            p3=[1]
        s_config=[p1,p2,p3]
        result=algorithm_4(res,s_config,base)
    p1=result[0]
    p1[m]+=s[m]
    p1[m-1]+=s[m-1]
    result[0]=p1
    return result


    
start2=time.time()
main()
#algorithm_2([9],[3],[8],10,"102890030",1)

end=time.time()-start2
print("\n\n\n")
print("Time elapsed: "+str(end)+" seconds") 
