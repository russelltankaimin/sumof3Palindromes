def check_type(number,base):
    num=str(number)
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
