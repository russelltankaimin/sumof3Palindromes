def algorithm_5(p1,p2,p3,base,num_string):
    l=len(num_string)//2
    s=base**l + base**(l-1)
    number=int(num_string)
    n_prime=number-s
    
    lst=str_to_lst(n_prime)
    if lst[-l]==0 or lst[-1-l]==0:
        n_prime=n_prime-s
        types=check_type(n_prime,base)
        k=2
    else:
        types=check_type(n_prime,base)
        k=1
    if types=="A1" or types=="A2" or types=="A3" or types=="A4":
        p1,p2,p3=algorithm_2(p1,p2,p3,base,str(n_prime),2)
        print("algorithm_2")
    elif types=="B1" or types=="B2" or types=="B3" or types=="B4" or types=="B5" or types=="B6" or types=="B7":
        p1,p2,p3=algorithm_4(p1,p2,p3,base,str(n_prime),2)
    p1=parse_list_to_int(p1)+k*s
    p1=str_to_lst(str(p1))
    return display(p1,p2,p3,num_string)
