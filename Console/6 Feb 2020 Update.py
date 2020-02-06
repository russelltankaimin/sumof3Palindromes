# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 21:16:40 2019

@author: RussellTan
"""
import time
# This is a console that expresses a number into 3 palindromes
start=time.time()
def construct(number,base):
    #First we have to count the number of digits
    length=len(number)
    if length<7:
        #Go to Proposition 4.1 in Section 4 to get the algorithm
        print("Digit Length less than or equal to 7. Special Algorithm Casting...")
        if length==2:
           two_digit_sum(number,base)
    else:
        #Go to general algorithm
        # Below is to identify the type of Palindrome
        state=check_type(number,base)
        if state=="A1":
            p1,p2,p3=construct_A1(number,base)
        elif state=="A2":
            p1,p2,p3=construct_A2(number,base)
        elif state=="A3":
            p1,p2,p3=construct_A3(number,base)
        elif state=="A4":
            p1,p2,p3=construct_A4(number,base)
        elif state=="A5":
            p1,p2,p3=construct_A5(number,base)
        elif state=="A6":
            p1,p2,p3=construct_A6(number,base)
        elif state=="B1":
            p1,p2,p3=construct_B1(number,base)            
        elif state=="B2":
            p1,p2,p3=construct_B2(number,base)    
        elif state=="B3":
            p1,p2,p3=construct_B3(number,base) 
        elif state=="B4":
            p1,p2,p3=construct_B4(number,base)
        elif state=="B5":
            p1,p2,p3=construct_B5(number,base)
        elif state=="B6":
            p1,p2,p3=construct_B6(number,base)
        elif state=="B7":
            p1,p2,p3=construct_B7(number,base)
        else:
            print("Unidentified type of number, unable to solve!")
            return 0
        return p1,p2,p3,state

def two_digit_sum(num_string,base):
    num=num_string
    if base!=16:
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
    if base==16:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)
    

##### Everything above this row has yet to undergo testing
##### Everything below this row has gone through at least 1 round of testing

def main():
    base=int(input("Enter its base\n"))
    if base>10:
        number=input("Enter the base"+"base"+" number ,format DEADBEEF without the 0x prefix\n")
        number=hex_int_to_lst(number)
    else:
        number=int(input("Enter your number\n"))
        number=str(number)
    length=len(number)
    #state is another word for type
    if length>=7:
        x,y,z,types=construct(number, base)
        if length%2 !=0:
            if types=="A1" or types=="A2" or types=="A3" or types=="A4":
                algorithm_1(x,y,z,base,number)
                return 0
            elif types=="B1" or types=="B2" or types=="B3" or types=="B4" or types=="B5" or types=="B6" or types=="B7":
                algorithm_3(x,y,z,base,number)
                return 0
            elif types=="A5" or types=="A6":
                algorithm_2(x,y,z,base,number,1)
                return 0
        else:
            if (is_special(number,types)):
                algorithm_5(x,y,z,base,number)
                return 0
            elif types=="A5" or types=="A6":
                algorithm_1(x,y,z,base,number)
                return 0
            elif types=="B1" or types=="B2" or types=="B3" or types=="B4" or types=="B5" or types=="B6" or types=="B7":
                algorithm_4(x,y,z,base,number,1)
                return 0
            else:
                algorithm_2(x,y,z,base,number,1)
                return 0
    else:
        construct(number,base)
                
def base_add_sub(p1,p2,base,func):
    #0 to subtract, 1 to add
    p1=int(toDeci(p1,base))
    p2=int(toDeci(p2,base))
    if func==0:#subtract p2 from p1
        p1=p1-p2
    elif func==1:
        p1=p1+p2
    return fromDeci(p1,base)                
    
def check_type(number,base):
    num=number
    if d(int(num[-1])-int(num[0])-int(num[1])+1,base) != 0 and ( int(num[1])!=0 and int(num[1])!=1 and int(num[1])!=2):
        print("This is an A1 type of number")
        types="A1"
    elif d(int(num[-1])-int(num[0])-int(num[1])+1,base)==0 and (int(num[1])!=0 and int(num[1])!=1 and int(num[1])!=2):
        print("This is an A2 type of number")
        types="A2"
    elif d(int(num[-1])-int(num[0])+2,base)!=0 and (int(num[1])==0 or int(num[1])==1 or int(num[1])==2) and int(num[0])!=1:
        print("This is an A3 type of number")
        types="A3"
    elif d(int(num[-1])-int(num[0])+2,base)==0 and (int(num[1])==0 or int(num[1])==1 or int(num[1])==2) and int(num[0])!=1:
        print("This is an A4 type of number")
        types="A4"
    elif d(int(num[-1])-int(num[2]),base)!=0 and int(num[2])<=3 and int(num[1])==0 and int(num[0])==1:
        print("This is an A5 type of number")
        types="A5"
    elif d(int(num[-1])-int(num[2]),base) ==0 and int(num[2])<=2 and int(num[1])==0 and int(num[0])==1:
        print("This is an A6 type of number")
        types="A6"
    elif d(int(num[-1])-int(num[2]),base)!=0 and int(num[2])>=4 and int(num[1])<=2 and int(num[0])==1:
        print("This is a B1 type of number")
        types="B1"
    elif d(int(num[-1])-int(num[2]),base)==0 and int(num[2])>=3 and int(num[1])<=2 and int(num[0])==1:
        print("This is a B2 type of number")
        types="B2"
    elif int(num[-1])==0 and (int(num[2])==0 or int(num[2])==1 ) and (int(num[1])==2 or int(num[1])==1 ) and int(num[0])==1:
        print("This is a B3 type of number")
        types="B3"
    elif int(num[-1])==0 and (int(num[2])==2 or int(num[2])==3 ) and (int(num[1])==2 or int(num[1])==1 ) and int(num[0])==1: 
        print("This is a B4 type of number")
        types="B4"
    elif int(num[-1])!=0 and (int(num[2])==0 or int(num[2])==1 or int(num[2])==2) and (int(num[1])==1 or int(num[1])==2) and int(num[0])==1:
        print("This is a B5 type of number")
        types="B5"
    elif d(int(num[-1])-3,base)!= 0 and int(num[2])==3 and (int(num[1])==1 or int(num[1])==2) and int(num[0])==1:
        print("This is a B6 type of number")
        types="B6"
    elif int(num[-1])==3 and int(num[2])==3 and (int(num[1])==1 or int(num[1])==2) and int(num[0])==1:
        print("This is a B7 type of number")
        types="B7"
    else:
        print("Indeterminate type")
        types=None
    return types

def d(num,base):
    return num%base

def hex_int_to_lst(num):
    hex_to_dec={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0}
    lst=[]
    reck=str(num)
    for i in reck:
        lst.append(hex_to_dec[i])
    return lst

def lst_to_hex_int(num_list):
    string_hex=''
    for integer in num_list:
        string_hex=string_hex+hex(int(integer))[2:].upper()
    return string_hex

def is_special(num_str,types):
  if types == "A5" or types == "A6":
      length_of_p1=len(num_str)-1
  else:
      length_of_p1=len(num_str)
  if length_of_p1%2!=0:
      return False
  else:
      num=num_str[::-1]
      m=length_of_p1>>1
      if int(num[m])==0 or int(num[m-1])==0:
          return True
      else:
          return False
      
def val(c): 
    if str(c) >= '0' and str(c) <= '9': 
        return ord(str(c)) - ord('0') 
    else: 
        return ord(str(c)) - ord('A') + 10
        
def toDeci(string,base): 
    llen = len(string) 
    power = 1 
    num = 0
    string=lst_to_hex_int(string)    
    for i in range(llen - 1, -1, -1): 
        if val(string[i]) >= base: 
            print('Invalid Number') 
            return -1
        num += val(string[i]) * power 
        power = power * base 
    return num
    
def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0')); 
    else: 
        return chr(num - 10 + ord('A')); 
        
def fromDeci(inputNum,base): 
    res=''
    while (inputNum > 0): 
        res+= reVal(inputNum % base); 
        inputNum = int(inputNum / base); 
    res = res[::-1]; 
  
    return res

def str_to_lst(num):
  num=str(num)
  lst=[]
  for digit in num:
    lst.append(int(digit))
  return lst  

def parse_list_to_int(lst):
    string=''
    for num in lst:
        string=string+str(num)
    return int(string)

def hex_display(p1,p2,p3,num_string):
  x,y,z='','',''
  for num in p1:
    if num<10:
      x=x+str(num)
    else:
      x=x+hex(num)[2:].upper()
  for ber in p2:
    if ber <10:
      y=y+str(ber)
    else:
      y=y+hex(ber)[2:].upper()
  for phile in p3:
    if phile<10:
      z=z+str(phile)
    else:
      z=z+hex(phile)[2:].upper()
  print(x)
  print("+"+y)
  print("+ "+z)
  print("--------------------------")
  print(lst_to_hex_int(num_string))
  
def construct_A1(num_string,base):
    p1=[int(num_string[0])] #Palindrome 1
    p2=[int(num_string[1])-1] #Palindrome 2
    p3=[d(int(num_string[-1])-int(num_string[0])-int(num_string[1])+1,base)] #Palindrome 3
    return p1,p2,p3

def construct_A2(num_string,base):
    p1=[int(num_string[0])] #Palindrome 1
    p2=[int(num_string[1])-2] #Palindrome 2
    p3=[1] #Palindrome 3
    #Below we are constructing type A.2
    return p1,p2,p3

def construct_A3(num_string,base):
    p1=[int(num_string[0])-1] #Palindrome 1
    p2=[base-1] #Palindrome 2
    p3=[d(int(num_string[-1])-int(num_string[0])+2,base)] #Palindrome 3
    #Below we are constructing type A.3
    return p1,p2,p3

def construct_A4(num_string,base):
    p1=[int(num_string[0])-1] #Palindrome 1
    p2=[base-2] #Palindrome 2
    p3=[1] #Palindrome 3
    return p1,p2,p3

def construct_A5(num_string,base):
    p1=[base-1] #Palindrome 1
    p2=[int(num_string[2])+1] #Palindrome 2
    p3=[d(int(num_string[-1])-int(num_string[2]),base)] #Palindrome 3
    return p1,p2,p3

def construct_A6(num_string,base):
    p1=[base-1] #Palindrome 1
    p2=[int(num_string[2])+2] #Palindrome 2
    p3=[base-1] #Palindrome 3
    return p1,p2,p3

def construct_B1(num_string,base):
    p1=[1,int(num_string[1])] #Palindrome 1
    p2=[int(num_string[2])-1] #Palindrome 2
    p3=[d(int(num_string[-1])-int(num_string[2]),base)] #Palindrome 3
    return p1,p2,p3

def construct_B2(num_string,base):
    p1=[1,int(num_string[1])] #Palindrome 1
    p2=[int(num_string[2])-2] #Palindrome 2
    p3=[1] #Palindrome 3
    return p1,p2,p3

def construct_B3(num_string,base):
    p1=[1,int(num_string[1])-1] #Palindrome 1
    p2=[base-2] #Palindrome 2
    p3=[1] #Palindrome 3
    return p1,p2,p3

def construct_B4(num_string,base):
    p1=[1,int(num_string[1])] #Palindrome 1
    p2=[base-2] #Palindrome 2
    p3=[1] #Palindrome 3
    return p1,p2,p3

def construct_B5(num_string,base):
    p1=[1,int(num_string[1])-1] #Palindrome 1
    p2=[base-1] #Palindrome 2
    p3=[int(num_string[-1])] #Palindrome 3
    return p1,p2,p3

def construct_B6(num_string,base):
    p1=[1,int(num_string[1])] #Palindrome 1
    p2=[2] #Palindrome 2
    p3=[d(int(num_string[-1])-3,base)] #Palindrome 3
    return p1,p2,p3

def construct_B7(num_string,base):
    p1=[1,int(num_string[1])] #Palindrome 1
    p2=[1] #Palindrome 2
    p3=[1] #Palindrome 3
    return p1,p2,p3

def display(p1,p2,p3,num_string):
    r1,r2,r3='','',''
    for i in range(0,len(p1)):
        r1=r1+str(p1[i])
    for j in range(0,len(p2)):
        r2=r2+str(p2[j])
    for k in range(0,len(p3)):
        r3=r3+str(p3[k])
    print(r1)
    print("+"+r2)
    print("+ "+r3)
    print("----------------------")
    print(num_string)
    
def algorithm_1(p1,p2,p3,base,num_string):
    print("Algorithm I")
    num=num_string[::-1]
    length=len(num_string)
    if length%2==0:
        m=(length-2)//2
    else:
        m=(length-1)//2
    carry=[]
    c1=(p1[0]+p2[0]+p3[0])//base
    carry.append(c1)
    if  p3[0]<=int(num[2*m-2])-1:
        p1.append(d(int(num[2*m-1])-p2[0],base))
    elif p3[0]>=int(num[2*m-2]):
        p1.append(d(int(num[2*m-1])-p2[0]-1,base))
    p2.append(d(int(num[2*m-2])-p3[0]-1,base))
    p3.append(d(int(num[1])-p1[1]-p2[1]-carry[0],base))
    carry.append((p1[1]+p2[1]+p3[1])//base)
    for i in range(3,m+1):
        if p3[i-2]<=int(num[2*m-i])-1:
            p1.append(1)
        elif p3[i-2]>=int(num[2*m-i]):
            p1.append(0)
        p2.append(d(int(num[2*m-i])-p3[i-2]-1,base))
        p3.append(d(int(num[i-1])-p1[i-1]-p2[i-1]-carry[i-2],base))
        carry.append((p1[i-1]+p2[i-1]+p3[i-1]+carry[i-2]-int(num[i-1]))//base)
    p1.append(0)
    vital_carry=carry[m-1]
    if vital_carry==1:
        print("No Adjustment Step needed")
    elif vital_carry==2:
        print("Adjustment needed")
        p1[m]=1
        p2[m]=p2[m]-1
        p3[m-1]=0
    elif vital_carry==0:
        print("Adjustment needed")
        p1[m]=1
    temp_p1=p1[::-1]
    temp_p3=p3[::-1]
    p1=p1+temp_p1[1:m+1]
    p2=p2+p2[::-1]
    p3=p3+temp_p3[1:m]
    if base>10:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)


def algorithm_2(p1,p2,p3,base,num_string,val=1):
    print("Algorithm II")
    num=num_string[::-1]
    length=len(num)
    if length%2==0:
        m=length//2
    else:
        m=(length-1)//2
    carry=[]
    carry.append((p1[0]+p2[0]+p3[0])//base)
    if p3[0]<=int(num[2*m-3])-1:
        p1.append(d(int(num[2*m-2])-p2[0],base))
    elif p3[0]>=int(num[2*m-3]):
        p1.append(d(int(num[2*m-2])-p2[0]-1,base))
    p2.append(d(int(num[2*m-3])-p3[0]-1,base))
    p3.append(d(int(num[1])-p1[1]-p2[1]-carry[0],base))
    carry.append((p1[1]+p2[1]+p3[1]+carry[0]-int(num[1]))//base)
    for i in range(3,m):
        if p3[i-2]<=int(num[2*m-i-1])-1:
            p1.append(1)
        elif p3[i-2]>=int(num[2*m-i-1]):
            p1.append(0)
        p2.append(d(int(num[2*m-i-1])-p3[i-2]-1,base))
        p3.append(d(int(num[i-1])-p1[i-1]-p2[i-1]-carry[i-2],base))
        carry.append((p1[i-1]+p2[i-1]+p3[i-1]+carry[i-2]-int(num[i-1]))//base)
    p1.append(0)
    p2.append(d(int(num[m-1])-p3[m-2]-carry[m-2],base))
    carry.append((p1[m-1]+p2[m-1]+p3[m-2]-carry[m-2])//base)
    vital_carry=carry[m-1]
    if vital_carry==1:
        print("No Adjustment Needed")
    elif vital_carry==0:
        if p2[m-1]!=0:
            p1[m-1]=1
            p2[m-1]=p2[m-1]-1
        else:
            if p2[m-2]!=0:
                p1[m-1]=1
                p2[m-1]=base-2
                p2[m-2]=p2[m-2]-1
                p3[m-2]=p3[m-2]+1
            elif p2[m-2]== 0 and p3[m-2]!=0:
                p2[m-2]=1
                p2[m-1]=1
                p3[m-2]=p3[m-2]-1
            elif p2[m-2]== 0 and p3[m-2]==0:
                p3[m-2]=2
                p2[m-2]=base-1
                p2[m-1]=base-4
                p1[m-1]=1
                p1[m-2]=p1[m-2]-1
    elif vital_carry==2:
        p1[m-1]=1
        p2[m-1]=base-2
        p2[m-2]=p2[m-2]-1
        p3[m-2]=0
    p1=p1+p1[::-1]
    temp_p2=p2[::-1]
    temp_p2=temp_p2[1:m+1]
    p2=p2+temp_p2
    p3=p3+p3[::-1]
    if val==2:
        return p1,p2,p3
    else:
        if base>10:
            return hex_display(p1,p2,p3,num_string)
        else:
            return display(p1,p2,p3,num_string)

def algorithm_3(p1,p2,p3,base,num_string):
    print("Algorithm III")
    num=num_string[::-1]
    p1.remove(p1[0])
    length=len(num)
    m=(length-1)//2
    carry=[]
    carry.append((1+p2[0]+p3[0])//base)
    if p3[0]<=int(num[2*m-3])-1:
        p1.append(d(int(num[2*m-2])-p2[0],base))
    elif p3[0]>=int(num[2*m-3]):
        p1.append(d(int(num[2*m-2])-p2[0]-1,base))
    p2.append(d(int(num[2*m-3])-p3[0]-1,base))
    p3.append(d(int(num[1])-p1[0]-p2[1]-carry[0],base))
    carry.append((p1[0]+p2[1]+p3[1]+carry[0]-int(num[1]))//base)
    for i in range(3,m):
        if p3[i-2]<=int(num[2*m-i-1])-1:
            p1.append(1)
        elif p3[i-2]>=int(num[2*m-i-1]):
            p1.append(0)
        p2.append(d(int(num[2*m-i-1])-p3[i-2]-1,base))
        p3.append(d(int(num[i-1])-p1[i-2]-p2[i-1]-carry[i-2],base))
        carry.append((p1[i-2]+p2[i-1]+p3[i-1]+carry[i-2]-int(num[i-1]))//base)
    p1.append(0)
    p2.append(d(int(num[m-1])-carry[m-2]-p3[m-2]-p1[m-2],base))
    carry.append((p1[m-2]+p2[m-1]+p3[m-2])//base)
    p1=[1]+p1
    if carry[m-1]==1:
        print("No Adjustment Needed")
    elif carry[m-1]==0:
        p1[m]=1
    elif carry[m-1]==2:
        if p2[m-2] !=0 and p3[m-2] != base - 1:
            p2[m-2]=p2[m-2]-1
            p2[m-1]=p2[m-1]-1
            p3[m-2]=p3[m-2]+1
        elif p2[m-2]!=0 and p3[m-2]==base - 1:
            p1[m]=1
            p2[m-2]=p2[m-2]-1
            p3[m-2]=0
        elif p2[m-2]==0 and p3[m-2] != base - 1:
            p1[m-1]=p1[m-1]-1
            p2[m-2]=base-1
            p2[m-1]=p2[m-1]-1
            p3[m-2]=p3[m-2]+1
        elif p2[m-2]==0 and p3[m-2] == base - 1:
            p1[m-1]=p1[m-1]-1
            p1[m]=1
            p2[m-2]=base-1
            p3[m-2]=0
    p3=p3+p3[::-1]
    temp_p2=p2[0:m-1]
    p2=temp_p2+p2[::-1]
    temp_p1=p1[0:m]
    p1=temp_p1+p1[::-1]
    if base>10:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)

def algorithm_4(p1,p2,p3,base,num_string,val):
    print("Algorithm IV")
    num=num_string[::-1]
    m=len(num)//2
    p2=[0]+p2
    p3=[0]+p3
    carry=[0]
    carry.append((1+p2[1]+p3[1])//base)
    if p3[1]<=int(num[2*m-4])-1:
        p1.append(d(int(num[2*m-3])-p2[1],base))
    elif p3[1]>= int(num[2*m-4]):
        p1.append(d(int(num[2*m-3])-p2[1]-1,base))
    p2.append(d(int(num[2*m-4])-p3[1]-1,base))
    p3.append(d(int(num[1])-p1[1]-p2[2]-carry[1],base))
    carry.append((p1[1]+p2[2]+p3[2]+carry[1])//base)
    for i in range(3,m-1):
        p1.append(1 if p3[i-1]<=int(num[2*m-i-2])-1 else 0)
        p2.append(d(int(num[2*m-i-2])-p3[i-1]-1,base))
        p3.append(d(int(num[i-1])-p1[i-1]-p2[i]-carry[i-1],base))
        carry.append((p1[i-1]+p2[i]+p3[i]+carry[i-1]-int(num[i-1]))//base)
    p1.append(1 if p3[m-2]<=int(num[m-1])-1 else 0)
    p2.append(d(int(num[m-1])-p3[m-2]-1,base))
    p3.append(d(int(num[m-2])-p1[m-2]-p2[m-1]-carry[m-2],base))
    carry.append((p1[m-2]+p2[m-1]+p3[m-1]+carry[m-2]-int(num[m-2]))//base)
    if p1[m-1]+carry[m-1]==1:
        print("No Adjustment needed")
    elif p1[m-1]+carry[m-1]==0 and p2[m-1]!=base - 1:
        if p3[m-1]!=0:
            p2[m-1]=p2[m-1]+1
            p3[m-1]=p3[m-1]-1
        elif p3[m-1]==0 and p2[m-2]!=0:
            if p2[m-1]!=1 and p3[m-2]!= base - 1:
                p1[m-1]=1
                p2[m-2]=p2[m-2]-1
                p2[m-1]=p2[m-1]-1
                p3[m-1]=1
                p3[m-2]=p3[m-2]+1
            elif p2[m-1]!=1 and p3[m-2]== base - 1 :
                p1[m-1]=2
                p2[m-1]=p2[m-1]-2
                p2[m-2]=p2[m-2]-1
                p3[m-2]=0
                p3[m-1]=3
            elif p2[m-1]==1:
                p1[m-1]=1
                p2[m-2]=p2[m-2]-1
                p2[m-1]=base-1
                p3[m-2]=0
                p3[m-1]=3
        elif p3[m-1]==0 and p2[m-2]==0:
            if p3[m-2]!= base - 1:
                p1[m-2]=p1[m-2]-1
                p1[m-1]=1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-1
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p3[m-2]==base -1 and p2[m-1]!=1:
                p1[m-1]=2
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=0
                p3[m-1]=3
            elif p3[m-2]==base - 1 and p2[m-1]==1:
                p1[m-2]=p1[m-2]-1
                p1[m-1]=1
                p2[m-2]=base-1
                p2[m-1]=base-1
                p3[m-2]=0
                p3[m-1]=3
    elif p1[m-1]+carry[m-1]==0 and p2[m-1]==base-1:
        p1[m-1]=1
        p2[m-2]=p2[m-2]-1
        p2[m-1]=base-2
        p3[m-2]=p3[m-2]+1
        p3[m-1]=1
    elif p1[m-1]+carry[m-1]==2 and p1[m-1]==0 and carry[m-1]==2:
        if p3[m-1]!=base-1:
            p2[m-1]=p2[m-1]-1
            p3[m-1]=p3[m-1]+1
        elif p3[m-1]==base-1 and p3[m-2]!=base-1:
            if p2[m-2]!=0:
                p1[m-1]=1
                p2[m-2]=p2[m-2]-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p2[m-2]==0:
                p1[m-2]=p1[m-2]-1
                p1[m-1]=1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
        elif p3[m-1]==p3[m-2]==base-1:
            if p2[m-1]!=base-1 and p2[m-1]!=base-2:
                if p2[m-2]!=base-1:
                    p1[m-2]=p1[m-2]-1
                    p1[m-1]=base-2
                    p2[m-2]=p2[m-2]+1
                    p2[m-1]=p2[m-1]+2
                    p3[m-2]=base-2
                    p3[m-1]=base-2
                else:
                    p1[m-1]=base-2
                    p2[m-2]=0
                    p2[m-1]=p2[m-1]+2
                    p3[m-2]=base-2
                    p3[m-1]=base-2
            elif p2[m-1]==base-1 or p2[m-1]==base-2:
                if p2[m-2]>=1:
                    p1[m-1]=2
                    p2[m-2]=p2[m-2]-1
                    p2[m-1]=p2[m-1]-3
                    p3[m-2]=0
                    p3[m-1]=3
                elif p2[m-2]==0:
                    p1[m-2]=p2[m-2]-1
                    p1[m-1]=2
                    p2[m-2]=base-1
                    p2[m-1]=p2[m-1]-3
                    p3[m-2]=0
                    p3[m-1]=3
    elif p1[m-1]+carry[m-1]==2 and p1[m-1]==1 and carry[m-1]==1:
        if p3[m-1]!=base-1 and p2[m-1]!=0:
            p2[m-1]=p2[m-1]-1
            p3[m-1]=p3[m-1]+1
        elif p3[m-1]!=base-1 and p2[m-1]==0:
            p1[m-1]=0
            p2[m-1]=base-1
            p3[m-1]=p3[m-1]+1
        elif p3[m-1]==base-1 and p3[m-2]!=0:
            if p2[m-2]!=base-1:
                print("Y")
                p1[m-1]= 0
                p2[m-2]=p2[m-2]+1
                p2[m-1]=p2[m-1]+1
                p3[m-2]=p3[m-2]-1
                p3[m-1]=base-2
            elif p2[m-2]==base-1 and p2[m-1]!=0 and p2[m-1]!=1:
                p1[m-1]=2
                p2[m-2]=base-2
                p2[m-1]=p2[m-1]-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p2[m-2]==base-1 and p2[m-1]==0:
                p2[m-2]=base-2
                p2[m-1]=base-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p2[m-2]==base-1 and p2[m-1]==1:
                p2[m-1]=base-1
                p2[m-2]=base-2
                p3[m-1]=1
                p3[m-2]=p3[m-2]+1
        elif p3[m-1]==base-1 and p3[m-2]==0 and p2[m-2]!=0:
            if p2[m-1]!=0 and p2[m-1]!=1:
                p1[m-1]=2
                p2[m-2]=p2[m-2]-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==0:
                p2[m-2]=p2[m-2]-1
                p2[m-1]=base-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==1:
                p2[m-2]=p2[m-2]-1
                p2[m-1]=base-1
                p3[m-2]=1
                p3[m-1]=1
        elif p3[m-1]==base-1 and p3[m-2]==0 and p2[m-2]==0:
            if p2[m-1]!=0 and p2[m-1]!=1:
                p1[m-1]=2
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==0:
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=base-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==1:
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=base-1
                p3[m-2]=1
                p3[m-1]=1
    elif p1[m-1]+carry[m-1]==3:
        p2[m-1]=p2[m-1]-1
        p3[m-1]=0
    p2=p2[1:m+1]
    p3=p3[1:m+1]
    p1=p1+p1[::-1]
    p2=p2+p2[::-1]
    temp=p3[::-1]
    p3=p3+temp[1:m-1]
    if val==2:
      #It is a special number
      return p1,p2,p3
    else:
        if base>10:
            return hex_display(p1,p2,p3,num_string)
        else:
            return display(p1,p2,p3,num_string)
 
def algorithm_5(p1,p2,p3,base,num_string):
    print("Algorithm V")
    l=len(num_string)//2
    s=base**l + base**(l-1)# s is an integer
    number=num_string
    #t_num=toDeci(number,base)
    t_s=fromDeci(s,base)
    n_prime=base_add_sub(number,t_s,base,0) # input for number is "ADE" form, t_s is str(some integer) output would have been "ADE000C5" form
    n_prime=str(n_prime)#str
    lst=str(n_prime)[::-1]#this line should turn hex_int_to_hex_string
    if lst[l]=='0' or lst[l-1]=='0':
        n_prime=base_add_sub(n_prime,t_s,base,0) # output would have been "ADE000C5" form
        rekt=hex_int_to_lst(n_prime)
        types=check_type(rekt,base)
        k=2
    else:
        rekt=hex_int_to_lst(str(n_prime))
        types=check_type(rekt,base)
        k=1
    if types=="A1" or types=="A2" or types=="A3" or types=="A4":
        p1,p2,p3=algorithm_2(p1,p2,p3,base,rekt,2)
    elif types=="B1" or types=="B2" or types=="B3" or types=="B4" or types=="B5" or types=="B6" or types=="B7":
        p1,p2,p3=algorithm_4(p1,p2,p3,base,rekt,2)
    x_add=fromDeci(k*s,base)
    x_add=lst_to_hex_int(x_add)
   # p1=lst_to_hex_int(p1) [P1 is currently [10,0,0,0,0,0,0,10]. Goal==> Turn it to 
    p1=base_add_sub(p1,x_add,base,1)
    p1=hex_int_to_lst(p1)
    if base>10:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)
     
end=time.time()-start
print("\n\n\n")
print("Time elapsed: "+str(end)+" seconds")   
