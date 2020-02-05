def algorithm_5(p1,p2,p3,base,num_string):
    print("Algorithm 5")
    l=len(num_string)//2
    s=base**l + base**(l-1)# s is an integer
    number=num_string
    #t_num=toDeci(number,base)
    t_s=fromDeci(s,base)
    n_prime=base_add_sub(number,t_s,base,0) # input for number is "ADE" form, t_s is str(some integer) output would have been "ADE000C5" form
    n_prime=str(n_prime)#str
    lst=str(n_prime)#this line should turn hex_int_to_hex_string
    if lst[-l]=='0' or lst[-1-l]=='0':
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
    p1=base_add_sub(p1,x_add,base,1)
    p1=hex_int_to_lst(p1)
    if base==16:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)
