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
    
def base_convert(inputNum,base):
    def reVal(num): 
        if (num >= 0 and num <= 9): 
            return chr(num + ord('0')); 
        else: 
            return chr(num - 10 + ord('A')); 
    res=''
    while (inputNum > 0): 
        res+= reVal(inputNum % base); 
        inputNum = int(inputNum / base); 
    res = res[::-1]; 
    return res    

def hex_display(res1,res2,res3,number):
    p1,p2,p3='','',''
    for i in range(0,len(res1)):
        p1=p1+hex(res1[i])[2:].upper()
    for j in range(0,len(res2)):
        p2=p2+hex(res2[j])[2:].upper()
    for k in range(0,len(res3)):
        p3=p3+hex(res3[k])[2:].upper()
    print("                 "+p1)
    print("                 +"+p2)
    print("                 + "+p3)
    print("                 "+"-"*len(p1))
    print("                 "+ str(number))
def one_digit_sum(num,base):
    return [num,[0],[0]]       
def two_digit_sum(num,base):
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
        if num[0]==0:
            p1=[base-1]
            p2=[1]
            p3=[0]
        else:
            p1=[num[0],num[0]]
            p2=[base-1]
            p3=[1]
    return [p1,p2,p3]
    
def three_digit_sum(num,base):
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
                    p2=[1,1,1]
                    p3=[0]
                elif num[2]==2:
                    p1=[1,0,1]
                    p2=[base-1,base-1]
                    p3=[1]
                else:
                    p1=[base-1,base-1]
                    p2=[1]
                    p3=[0]
    return [p1,p2,p3]

def four_digit_sum(num,base):
    perm=num
    [d0,d1,d2,d3]=num[::-1]
    n=perm[0]*(base**3)+perm[1]*(base**2)+perm[2]*base+perm[3]
    if n>=d3*(base**3)+d3:
        m=n-d3*(base**3)-d3
        dp=d(m,base)
        if m==2*(base**2)+1:
            if d3==1:
                return[[1,1,1,1],[base-2,base-2],[3]]
            elif d3==base-1:
                return [[base-1,1,1,base-1],[base-2,base-2],[3]]
            else:
                return [[d3-1,base-1,base-1,d3-1],[2,1,2],[0]]
        elif (1<=dp<=base-2 and m==(dp+1)*base+dp):
            if(d3+dp==d0):
                if d3!=1:
                    return [[d3-1,base-2,base-2,d3-1],[1,3,1],[dp,dp]]
                else:
                    return [[base-1,base-1,base-1],[dp+1,dp+1],[1]]
            else:
                return [[d3-1,base-2,base-2,d3-1],[1,3,1],[dp,dp]]
        elif d2==0 and d1==0 and d0<=d3-1 and d3!=1:
            return [[d3-1,base-1,base-1,d3-1],[base+d0-d3],[1]]
        elif [d0,d1,d2,d3]==[0,0,0,1]:
            return [[base-1,base-1,base-1],[1],[0]]
        else:
            m=base_convert(m,base)
            m=hex_int_to_lst(m)
            if len(m)==1:
                extra=one_digit_sum(m,base)
            elif len(m)==2:
                extra=two_digit_sum(m,base)
            elif len(m)==3:
                extra=three_digit_sum(m,base)
            else:
                extra=four_digit_sum(m,base)
            config=[[d3,0,0,d3]]
            config.append(extra[0])
            config.append(extra[1])
            return config
    elif d0<=d3-1 and d3!=1:
        return [[d3-1,base-1,base-1,d3-1],[base+d0-d3],[1]]
    else:
        return [[base-1,base-1,base-1],[1],[0]]
    
def five_digit_sum(num,base):
    #perm=num #perm is the number the shallow copy of the actual number
    if num[0]!=1:
        [types,config,special]=check_type(num,base)
        return algorithm_1(num,config,base,types)
    else:
        [d0,d1,d2,d3,d4]=num[::-1]
        i1=1*(base**4 + 1)+ d3*(base+base**3) #1d30d31
        deci_num=d0+d1*base+d2*(base**2)+d3*(base**3)+d4*(base**4)
        m=deci_num-i1
        dp=d(m,base)
        i2=1*(base**4 + 1)+ (d3-1)*(base+base**3)+(base-1)*(base**2)
        m2=deci_num-i2
        dpp=d(m2,base)
        tho=2*(base**2)+1
        if (deci_num>=i1 and m!=tho) and (dp==0 or dp==base-1 or m!=(dp+1)*base+dp):
            m=base_convert(m,base)
            m=hex_int_to_lst(m)
            if len(m)==1:
                extra=one_digit_sum(m,base)
            elif len(m)==2:
                extra=two_digit_sum(m,base)
            elif len(m)==3:
                extra=three_digit_sum(m,base)
            elif len(m)==4:
                extra=four_digit_sum(m,base)
            else:
                extra=five_digit_sum(m,base)
            config1=[[1,d3,0,d3,1]]
            config1.append(extra[0])
            config1.append(extra[1])
            return config1
        elif deci_num>=i1 and m==tho:
            return [[1,d3,1,d3,1],[1,0,1]]
        elif deci_num>=i1 and m==(dp+1)*base+dp and 1<=dp<=base-2 and d3!=0:
            if dp+1+d3<=base-1:
                return [[1,d3-1,1,d3-1,1],[base-1,dp+1,base-1],[dp+1]]
            elif d3+1+dp==base+d1:
                return [[1,d3-1,1,d3-1,1],[base-1,dp+1,base-1],[dp+1]]
        elif deci_num>=i1 and m==(dp+1)*base+dp and 1<=dp<=base-2 and d3==0:
            return [[base-1,base-1,base-1,base-1],[dp+1,dp+1],[1]]
        elif deci_num<i1 and d3==0:
            return [[base-1]*4,[1],[0]]
        elif (deci_num<i1 and d3!=0 and m2!=tho) and (dp==0 or dp==base-1 or m2!=(dpp+1)*base+dpp):
            m=base_convert(m2,base)
            m=hex_int_to_lst(m)
            if len(m)==1:
                extra=one_digit_sum(m,base)
            elif len(m)==2:
                extra=two_digit_sum(m,base)
            elif len(m)==3:
                extra=three_digit_sum(m,base)
            elif len(m)==4:
                extra=four_digit_sum(m,base)
            else:
                extra=five_digit_sum(m,base)
            config1=[[1,d3-1,base-1,d3-1,1]]
            config1.append(extra[0])
            config1.append(extra[1])
            return config1
        else:
            return [[1,d3-1,base-2,d3-1,1],[1,dp+1,1],[dp-1]]
    
def six_digit_sum(num,base):
    [d0,d1,d2,d3,d4,d5]=num[::-1]
    if d5!=1:
        num=num[::-1]
        length=6
        m=3
        [types,config,special]=check_type([d5,d4,d3,d2,d1,d0],base)
        c=[0]
        x,y,z=[0]+config[0],[0]+config[1],[0]+config[2]
        c.append((x[1]+y[1]+z[1])//base)
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
            return [[x[1],x[2],x[3],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[2],z[1]]]
        elif c[m]==0:
            if y[m]!=0:
                x[m]=1
                y[m]-=1
                return [[x[1],x[2],x[3],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[2],z[1]]]
            else:
                if y[m-1]!=0:
                    x[m]=1
                    y[m]=base-2
                    y[m-1]-=1
                    z[m-1]+=1
                    return [[x[1],x[2],x[3],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[2],z[1]]]
                else:
                    if z[m-1]!=0:
                        y[m]=1
                        y[m-1]=1
                        z[m-1]-=1
                        return [[x[1],x[2],x[3],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[2],z[1]]]
                    else:
                        if x[2]!=0:
                            x[2]-=1
                            x[3]=base-1
                            y[2]=1
                            y[3]=1
                            return [[x[1],x[2],x[3],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[2],z[1]]]
                        elif x[1]==1:
                            return [[2,0,0,0,0,2],[1,1],[base-4]]
                        elif x[1]!=1 and y[1]!=base-1:
                            return [[x[1]-1,base-1,0,0,base-1,x[1]-1],[y[1]+1,0,base-2,0,y[1]+1],[z[1],1,1,z[1]]]
                        elif x[1]!=base-1 and z[1]==base-1 and y[1]==base-1:
                            return [[x[1]+1,0,0,0,0,x[1]+1],[1,1],[base-4]]
        elif c[m]==2:
            x[m]=1
            y[m-1]-=1
            y[m]=base-2
            z[m-1]=0
            return [[x[1],x[2],x[3],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[2],z[1]]]
    else:
        x,y,z=[0],[0],[0]
        c=[0]
        if d(d0-d4+1,base)!=0 and d(d0-d4+2,base)!=0:
            x.append((base+d4-1)//2)
            y.append(base+d4-1-x[1])
            z.append(d(d0-d4+1,base))
            c.append((x[1]+y[1]+z[1]-d0)//base)
            x.append((base+d3-1)//2)
            y.append(base+d3-1-x[2])
            z.append(d(d1-x[2]-y[2]-c[1],base))
            c.append((x[2]+y[2]+z[2]+c[1]-d1)//base)
            x.append((base+d2-c[2]-z[1])//2)
            y.append(base+d2-c[2]-z[1]-x[3])
            return [[x[1],x[2],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[1]]]
        elif d(d0-d4+2,base)==0 and d2!=0:
            x.append((base+d4-1)//2)
            y.append(base+d4-1-x[1])
            z.append(base-1)
            c.append((x[1]+y[1]+z[1]-d0)//base)
            x.append((base+d3-1)//2)
            y.append(base+d3-1-x[2])
            z.append(d(d1-x[2]-y[2]-c[1],base))
            c.append((x[2]+y[2]+z[2]+c[1]-d1)//base)
            x.append((1+d2-c[2])//2)
            y.append(1+d2-c[2]-x[3])
            return [[x[1],x[2],x[3],x[2],x[1]],[y[1],y[2],y[3],y[2],y[1]],[z[1],z[2],z[1]]]
        elif d(d0-d4+2,base)==0 and d2==0:
            x.append(0)
            y.append(0)
            z.append(0)
            if d4==0:
                x2=d3//2
                y2=d3-x2
                z2=d(d1-x2-y2-1,base)
                c2=(x2+y2+z2+1-d1)//base
                x3=(base-c2-z2)//2
                y3=base-c2-z2-x3
                return [[base-2,x2,x3,x2,base-2],[1,y2,y3,y2,1],[base-1,z2,z2,base-1]]
            elif d4==1:
                x2=(d3//2)
                y2=(d3-x2)
                z2=d(d1-x2-y2-1,base)
                c2=(x2+y2+z2+1-d1)//base
                x3=(base-c2-z2)//2
                y3=base-c2-z2-x3
                return [[base-1,x2,x3,x2,base-1],[1,y2,y3,y2,1],[base-1,z2,z2,base-1]]
            elif d4==2:
                x2=d3//2
                y2=d3-x2
                z2=d(d1-x2-y2-2,base)
                c2=(x2+y2+z2+2-d1)//base
                if c2!=2:
                    x3=(base-c2-z2)//2
                    y3=base-c2-z2-x3
                    return [[base-1,x2,x3,x2,base-1],[2,y2,y3,y2,2],[base-1,z2,z2,base-1]]
                else:
                    return [[1,2,base-2,base-2,2,1],[1,base-3,1],[base-2]]
            elif d4>=3:
                c4=(d(d3-1,base)+1-d3)//base
                z1=d(d1-d3-1+c4,base)
                c2=(2-c4+d(d3-1,base)+z1-d1)//base
                return [[1,1-c4,0,0,1-c4,1],[d4-1,d(d3-1,base),2-c2,d(d3-1,base),d4-1],[base-2,z1,base-2]]
        elif d(d0-d4+1,base)==0 and d3!=0:
            if d4!=base-1:
                x1=(base+d4)//2
                y1=base+d4-x1
                z1=base-1
                c1=(x1+y1+z1-d0)//base
                x2=(d3-1)//2
                y2=d3-1-x2
                z2=d(d1-x2-y2-c1,base)
                c2=(x2+y2+z2+c1-d1)//base
                x3=(1+d2-c2)//2
                y3=1+d2-c2-x3
                return [[x1,x2,x3,x2,x1],[y1,y2,y3,y2,y1],[z1,z2,z1]]
            else:
                if d(d1-4,base)==base-1:
                    yd=3
                elif d(d1-4,base)==base-2:
                    yd=2
                else:
                    yd=1
                xd=d3+base-yd if d3<yd else d3-yd
                c1=(3+yd +d(d1-3-yd,base)-d1)//base
                mu=0
                c2=(xd+d(d2-xd-1-c1+mu,base)+c1+1-d2)//base
                if c2<=1:
                    pass
                else:
                    c2=1
                    mu=1
                c3=(xd+yd-d3)//base
                return [[1,3-c3,xd-mu,xd-mu,3-c3,1],[base-4,yd-c2+mu,d(d2-xd-1-c1+mu,base),yd-c2+mu,base-4],[1,d(d1-3-yd,base)+c2-mu+c3,1]]
        elif d(d0-d4+1,base)==0 and d3==0:
            if d4==0:
                if d2!=0:
                    n=d0+d1*base+d2*(base**2)+d3*(base**3)+d4*(base**4)+d5*(base**5)
                    s=n-1-base**5
                    m=base_convert(s,base)
                    m=hex_int_to_lst(m)
                    if len(m)==1:
                        extra=one_digit_sum(m,base)
                    elif len(m)==2:
                        extra=two_digit_sum(m,base)
                    elif len(m)==3:
                        extra=three_digit_sum(m,base)
                    elif len(m)==4:
                        extra=four_digit_sum(m,base)
                    elif len(m)==5:
                        extra=five_digit_sum(m,base)
                    else:
                        extra=six_digit_sum(m,base)
                    config1=[[1,0,0,0,0,1]]
                    config1.append(extra[0])
                    config1.append(extra[1])
                    return config1
                elif d1!=0 and d1!=base-1:
                    n=d0+d1*base+d2*(base**2)+d3*(base**3)+d4*(base**4)+d5*(base**5)
                    s=n-1-base**5
                    m=base_convert(s,base)
                    m=hex_int_to_lst(m)
                    if len(m)==1:
                        extra=one_digit_sum(m,base)
                    elif len(m)==2:
                        extra=two_digit_sum(m,base)
                    elif len(m)==3:
                        extra=three_digit_sum(m,base)
                    elif len(m)==4:
                        extra=four_digit_sum(m,base)
                    elif len(m)==5:
                        extra=five_digit_sum(m,base)
                    else:
                        extra=six_digit_sum(m,base)
                    config1=[[1,0,0,0,0,1]]
                    config1.append(extra[0])
                    config1.append(extra[1])
                    return config1
                elif d1==0:
                    return [[1,0,0,0,0,1],[base-2],[0]]
                elif d1==base-1:
                    return [[base-1,0,1,0,base-1],[base-1,base-2,base-2,base-1],[1,0,1]]
            elif d4==1:
                if d2>=2 or (d2==1 and d1>=2):
                    n=d0+d1*base+d2*(base**2)+d3*(base**3)+d4*(base**4)+d5*(base**5)
                    s=n-1-base-base**4-base**5
                    m=base_convert(s,base)
                    m=hex_int_to_lst(m)
                    if len(m)==1:
                        extra=one_digit_sum(m,base)
                    elif len(m)==2:
                        extra=two_digit_sum(m,base)
                    elif len(m)==3:
                        extra=three_digit_sum(m,base)
                    elif len(m)==4:
                        extra=four_digit_sum(m,base)
                    elif len(m)==5:
                        extra=five_digit_sum(m,base)
                    else:
                        extra=six_digit_sum(m,base)
                    config1=[[1,1,0,0,1,1]]
                    config1.append(extra[0])
                    config1.append(extra[1])
                    return config1
                elif d2==1 and d1==0:
                    return [[1,0,base-1,base-1,0,1],[1,base-1,1],[base-2]]
                elif d2==1 and d1==1:
                    return [[1,1,0,0,1,1],[base-1,base-1],[0]]
                elif d2==0 and d1>=2:
                    return [[1,1,0,0,1,1],[d1-2,d1-2],[base-d1+1]]
                elif d2==0 and d1==1:
                    return [[1,0,0,0,0,1],[1,0,0,0,1],[base-2]]
                elif d2==0 and d1==0:
                    return [[1,0,0,0,0,1],[base-1,base-1,base-1,base-1],[0]]
            elif d4==2:
                if d2>=2 or (d2==1 and d1>=2):
                    n=d0+d1*base+d2*(base**2)+d3*(base**3)+d4*(base**4)+d5*(base**5)
                    s=n-1-2*base-2*(base**4)-base**5
                    m=base_convert(s,base)
                    m=hex_int_to_lst(m)
                    if len(m)==1:
                        extra=one_digit_sum(m,base)
                    elif len(m)==2:
                        extra=two_digit_sum(m,base)
                    elif len(m)==3:
                        extra=three_digit_sum(m,base)
                    elif len(m)==4:
                        extra=four_digit_sum(m,base)
                    elif len(m)==5:
                        extra=five_digit_sum(m,base)
                    else:
                        extra=six_digit_sum(m,base)
                    config1=[[1,2,0,0,2,1]]
                    config1.append(extra[0])
                    config1.append(extra[1])
                    return config1
                elif d2==1 and d1==0:
                    return [[1,1,base-1,base-1,1,1],[1,base-2,1],[base-1]]
                elif d2==1 and d1==1:
                    return [[1,1,base-1,base-1,1,1],[1,base-1,1],[base-1]]
                elif d2==0 and d1==3:
                    return [[1,2,0,0,2,1],[base-1],[1]]
                elif d2==0 and d1>3:
                    return [[1,2,0,0,2,1],[d1-3,d1-3],[base-d1+3]]
                elif d2==0 and d1==2:
                    return [[1,1,base-1,base-1,1,1],[1,0,1],[base-1]]
                elif d2==0 and d1==1:
                    return [[1,0,0,0,0,1],[2,0,0,0,2],[base-2]]
                elif d2==0 and d1==0:
                    return [[1,1,base-1,base-1,1,1],[base-2,base-2],[2]]
            elif d4==3:
                if d(d1-2,base)==0:
                    yd=3
                elif d(d1-2,base)==base-1:
                    yd=2
                else:
                    yd=1
                c1=(2+yd+d(d1-1-yd,base)-d1)//base
                c2=(base-yd-1+d(d2+yd+2,base)+base-1-d2)//base
                return [[1,0,base-yd-1-c1,base-yd-1-c1,0,1],[2,yd-c2+1+c1,d(d2+yd+2,base),yd-c2+1+c1,2],[base-1,d(d1-1-yd,base)+c2-1-c1,base-1]]
            elif d4>=4:
                if d(d1-2,base)==0:
                    yd=3
                elif d(d1-2,base)==base-1:
                    yd=2
                else:
                    yd=1
                c1=(1+yd+d(d1-yd-1,base)-d1)//base
                c2=(base-yd+1+d(d2+yd-1,base)-d2)//base
                return [[1,2,base-yd-c1,base-yd-c1,2,1],[d4-3,yd-c2+c1,d(d2+yd-1,base),yd-c2+c1,d4-3],[1,d(d1-2-yd,base)+c2-c1,1]]
                    
                    

def front_display():
    print("       ****************************************************************")
    print("       LET ME SHOW YOU SOMETHING\n\n")
    print("             THAT WILL BLOW YOUR MIND!!!\n\n")
    print("       EVERY INTEGER CAN BE WRITTEN AS A SUM OF 3 PALINDROMES !!\n\n")
    print("****************************************************************")
 
def debug(message):
    print("debug "+str(message))
    
def main():
    front_display()
    base=int(input("       Enter its base from 5 to 16 \n"))
    if base>10:
        perm_number=input("       Enter the base-"+str(base)+" number ,format DEADBEEF without the 0x prefix\n")
        number=hex_int_to_lst(perm_number)
    else:
        perm_number=int(input("       Enter your number\n"))
        number=hex_int_to_lst(perm_number)
    if number==number[::-1]:
        print("\\n       "+str(perm_number)+" is already a PALINDROME ! ! ! ")
        return 0
    else:
        length=len(number)
        if length>6:
            res=main_algorithm(number,base)
        elif length==2:
            res=two_digit_sum(number,base)
        elif length==3:
            res=three_digit_sum(number,base)
        elif length==4:
            res=four_digit_sum(number,base)
        elif length==5:
            res=five_digit_sum(number,base)
        elif length==6:
            res=six_digit_sum(number,base)
    if len(res)==2:
        res.append([0])
    else:
        pass
    print(res[0])
    print(res[1])
    print(res[2])
    print("\n        ---Initialising Appropriate Printing Format---\n")
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
        p2=[1] #Palindrome 2
        p3=[base-2] #Palindrome 3
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
    x=x+t_x[1:]
    t_z=z[::-1]
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
    if digits[-1]==0:
        digits=digits[0:len(digits)-1]
    else:
        pass
    if digits[m-1]==0 or digits[m]==0:
        s[m],s[m-1]=2,2
        rev_num=number[::-1]
        digits=big_sub(rev_num,s,base)
        if digits[-1]==0:
            digits=digits[0:len(digits)-1]
        else:
            pass
    res=digits[::-1]
    [t_types,t_config,t_special]=check_type(res,base)
    length=len(res)
    if t_types=="A5" or t_types=="A6":
        length_of_p1=length-1
    else:
        length_of_p1=length
    even=(length_of_p1%2==0)
    if even:
        if length==6:
            result=six_digit_sum(res,base)
        else:
            result=main_algorithm(res,base)
    else:
        if length==6:
            result=six_digit_sum(res,base)
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

def lst_to_int(number):
    string=''
    for i in range(0,len(number)):
        string+=str(number[i])
    return int(string)
 
def test(start,end,base):
    for r in range(start,end+1):
        number=hex_int_to_lst(str(r))
        if number==number[::-1]:
            print( "Palindrome "+ str(lst_to_int(number))+" Passed")   
        else:
            length=len(number)
            if length>6:
                res=main_algorithm(number,base)
            elif length==2:
                res=two_digit_sum(number,base)
            elif length==3:
                res=three_digit_sum(number,base)
            elif length==4:
                res=four_digit_sum(number,base)
            elif length==5:
                res=five_digit_sum(number,base)
            elif length==6:
                res=six_digit_sum(number,base)
            if len(res)==2:
                res.append([0])
            tester=[res[0],res[1],res[2]]
            if lst_to_int(tester[0])+lst_to_int(tester[1])+lst_to_int(tester[2])!=lst_to_int(number):
                print(str(lst_to_int(number))+" Failed")
                return 0
            else:
                print(str(lst_to_int(number))+" Passed" )
    print("Test ended")
    return 0
russell_mode=input("Enter test() to test numbers, main() to run otherwise\n")
if russell_mode=="test()":
    start1=int(input("Enter a start number"))
    end1=int(input("Enter an end number"))
    base=int(input("Input base for testing"))
    start2=time.time()
    test(start1,end1,base)
    end=time.time()-start2
    print("\n\n\n")
    print("Time elapsed: "+str(end)+" seconds")
    total_operations=end1-start1+1
    avrge=end/total_operations
    print("Average time per operations = "+str(avrge)+" seconds" )
else:
    start2=time.time()
    main()
    end=time.time()-start2
    print("\n\n\n")
    print("Time elapsed: "+str(end)+" seconds")
        
    
