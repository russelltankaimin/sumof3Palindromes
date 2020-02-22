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
