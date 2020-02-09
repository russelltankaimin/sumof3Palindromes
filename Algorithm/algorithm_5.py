def algorithm_5(p1,p2,p3,base,num_string,val):
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
        n_prime=hex_int_to_lst(n_prime)
        n_prime=base_add_sub(n_prime,t_s,base,0) # output would have been "ADE000C5" form
        rekt=hex_int_to_lst(str(n_prime))
        types=check_type(rekt,base)
        k=2
    else:
        rekt=hex_int_to_lst(str(n_prime))
        types=check_type(rekt,base)
        k=1
    state=types #I copied off the top, else very lazy
    if state=="A1":
        p1,p2,p3=construct_A1(rekt,base)
    elif state=="A2":
        p1,p2,p3=construct_A2(rekt,base)
    elif state=="A3":
        p1,p2,p3=construct_A3(rekt,base)
    elif state=="A4":
        p1,p2,p3=construct_A4(rekt,base)
    elif state=="A5":
        p1,p2,p3=construct_A5(rekt,base)
    elif state=="A6":
        p1,p2,p3=construct_A6(rekt,base)
    elif state=="B1":
        p1,p2,p3=construct_B1(rekt,base)            
    elif state=="B2":
        p1,p2,p3=construct_B2(rekt,base)    
    elif state=="B3":
        p1,p2,p3=construct_B3(rekt,base) 
    elif state=="B4":
        p1,p2,p3=construct_B4(rekt,base)
    elif state=="B5":
        p1,p2,p3=construct_B5(rekt,base)
    elif state=="B6":
        p1,p2,p3=construct_B6(rekt,base)
    elif state=="B7":
        p1,p2,p3=construct_B7(rekt,base)        
    actual_length=len(rekt)
    even=(actual_length%2==0)
    if types=="A5" or types=="A6":
        length_of_p1=actual_length-1
    else:
        length_of_p1=actual_length
    if length_of_p1 %2==0:
        if types=="A1" or types=="A2" or types=="A3" or types=="A4":
            if not even:
                p1,p2,p3=algorithm_1(p1,p2,p3,base,rekt,2)
            elif is_special(rekt,types)==False:
                p1,p2,p3=algorithm_2(p1,p2,p3,base,rekt,2)
            else:
                p1,p2,p3=algorithm_5(p1,p2,p3,base,rekt,2)
        elif types=="A5" or types=="A6":
            if even:
                p1,p2,p3=algorithm_1(p1,p2,p3,base,rekt,2)
            elif is_special(rekt,types)==False:
                p1,p2,p3=algorithm_2(p1,p2,p3,base,rekt,2)
            else:
                p1,p2,p3=algorithm_5(p1,p2,p3,base,rekt,2)
        elif types=="B1" or types=="B2" or types=="B3" or types=="B4" or types=="B5" or types=="B6" or types=="B7":
            if not even:
                p1,p2,p3=algorithm_3(p1,p2,p3,base,rekt,2)
            elif is_special(rekt,types)==False:
                p1,p2,p3=algorithm_4(p1,p2,p3,base,rekt,2)
            else:
                p1,p2,p3=algorithm_5(p1,p2,p3,base,rekt,2)
    else:
        z1=d(int(rekt[-1])-int(rekt[2]),base)
        if int(rekt[0])==1 and int(rekt[1])<=2 and z1!=0:
            print("Pseudo-Type B1")
            p1=[1,int(rekt[1])]
            p2=[int(rekt[2])-1]
            p3=[z1]
        else:
            print("Pseudo-Type B2")
            p1=[1,int(rekt[1])]
            p2=[int(rekt[2])-2]
            p3=[1]
        p1,p2,p3=algorithm_4(p1,p2,p3,base,rekt,2)
    x_add=fromDeci(k*s,base)
    x_add=lst_to_hex_int(x_add)
   # p1=lst_to_hex_int(p1) [P1 is currently [10,0,0,0,0,0,0,10]. Goal==> Turn it to 
    p1=base_add_sub(p1,x_add,base,1)
    p1=hex_int_to_lst(p1)
    if val==2:
        return p1,p2,p3
    else:
        if base>10:
            return hex_display(p1,p2,p3,num_string)
        else:
            return display(p1,p2,p3,num_string)
