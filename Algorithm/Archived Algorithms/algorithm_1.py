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

