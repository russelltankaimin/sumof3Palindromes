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
