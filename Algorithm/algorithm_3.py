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
