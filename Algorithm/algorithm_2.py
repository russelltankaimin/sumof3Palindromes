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
