def construct_A1(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
        #Below we are constructing type A.1
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-1):
        p2.append(0)
    for k in range(0,len(num_string)-2):
        p3.append(0)
    p1[0]=int(num_string[0])
    p1[-1]=int(num_string[0])
    p2[0]=int(num_string[1])-1
    p2[-1]=int(num_string[1])-1
    p3[0]=d(int(num_string[-1])-int(num_string[0])-int(num_string[1])+1,base)
    p3[-1]=d(int(num_string[-1])-int(num_string[0])-int(num_string[1])+1,base)
    return p1,p2,p3

def construct_A2(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type A.2
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-1):
        p2.append(0)
    for k in range(0,len(num_string)-2):
        p3.append(0)
    p1[0]=int(num_string[0])
    p1[-1]=int(num_string[0])
    p2[0]=int(num_string[1])-2
    p2[-1]=int(num_string[1])-2
    p3[0]=1
    p3[-1]=1
    return p1,p2,p3

def construct_A3(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type A.3
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-1):
        p2.append(0)
    for k in range(0,len(num_string)-2):
        p3.append(0)
    p1[0]=int(num_string[0])-1
    p1[-1]=int(num_string[0])-1
    p2[0]=base-1
    p2[-1]=base-1
    p3[0]=d(int(num_string[-1])-int(num_string[0])+2,base)
    p3[-1]=d(int(num_string[-1])-int(num_string[0])+2,base)
    return p1,p2,p3

def construct_A4(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type A.4
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-1):
        p2.append(0)
    for k in range(0,len(num_string)-2):
        p3.append(0)
    p1[0]=int(num_string[0])-1
    p1[-1]=int(num_string[0])-1
    p2[0]=base-2
    p2[-1]=base-2
    p3[0]=1
    p3[-1]=1
    return p1,p2,p3

def construct_A5(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type A.5
    for i in range(0,len(num_string)-1):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=base-1
    p1[-1]=base-1
    p2[0]=int(num_string[2])+1
    p2[-1]=int(num_string[2])+1
    p3[0]=d(int(num_string[-1])-int(num_string[2]),base)
    p3[-1]=d(int(num_string[-1])-int(num_string[2]),base)
    return p1,p2,p3

def construct_A6(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type A.6
    for i in range(0,len(num_string)-1):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=base-1
    p1[-1]=base-1
    p2[0]=int(num_string[2])+2
    p2[-1]=int(num_string[2])+2
    p3[0]=base-1
    p3[-1]=base-1
    return p1,p2,p3

def construct_B1(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.1
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])
    p1[-2]=int(num_string[1])
    p2[0]=int(num_string[2])-1
    p2[-1]=int(num_string[2])-1
    p3[0]=d(int(num_string[-1])-int(num_string[2]),base)
    p3[-1]=d(int(num_string[-1])-int(num_string[2]),base)
    return p1,p2,p3

def construct_B2(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.2
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])
    p1[-2]=int(num_string[1])
    p2[0]=int(num_string[2])-2
    p2[-1]=int(num_string[2])-2
    p3[0]=1
    p3[-1]=1
    return p1,p2,p3

def construct_B3(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.3
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])-1
    p1[-2]=int(num_string[1])-1
    p2[0]=base-2
    p2[-1]=base-2
    p3[0]=1
    p3[-1]=1
    return p1,p2,p3

def construct_B4(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.4
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])
    p1[-2]=int(num_string[1])
    p3[0]=base-2
    p3[-1]=base-2
    p2[0]=1
    p2[-1]=1
    return p1,p2,p3

def construct_B5(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.5
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])-1
    p1[-2]=int(num_string[1])-1
    p2[0]=base-1
    p2[-1]=base-1
    p3[0]=int(num_string[-1])
    p3[-1]=int(num_string[-1])
    return p1,p2,p3

def construct_B6(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.6
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])
    p1[-2]=int(num_string[1])
    p2[0]=2
    p2[-1]=2
    p3[0]=d(int(num_string[-1])-3,base)
    p3[-1]=d(int(num_string[-1])-3,base)
    return p1,p2,p3

def construct_B7(num_string,base):
    p1=[] #Palindrome 1
    p2=[] #Palindrome 2
    p3=[] #Palindrome 3
    #Below we are constructing type B.7
    for i in range(0,len(num_string)):
        p1.append(0)
    for j in range(0,len(num_string)-2):
        p2.append(0)
    for k in range(0,len(num_string)-3):
        p3.append(0)
    p1[0]=1
    p1[-1]=1
    p1[1]=int(num_string[1])
    p1[-2]=int(num_string[1])
    p2[0]=1
    p2[-1]=1
    p3[0]=1
    p3[-1]=1
    return p1,p2,p3
