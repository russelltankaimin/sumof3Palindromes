def algorithm_4(number,config,base):
    num=number[::-1]
    x,y,z=config[0],config[1],config[2]
    length=len(num)
    m=length>>1
    y=[0]+y
    z=[0]+z
    c=[0,(1+y[1]+z[1])//base]
    x.append(d(num[2*m-3]-y[1],base) if z[1]<=num[2*m-4]-1 else d(num[2*m-3]-y[1]-1,base))
    y.append(d(num[2*m-4]-z[1]-1,base))
    z.append(d(num[1]-x[1]-y[2]-c[1],base))
    c.append((x[1]+y[2]+z[2]+c[1]-num[1])//base)
    for i in range(3,m-1):
        x.append(1 if z[i-1]<=num[2*m-i-2]-1 else 0)
        y.append(d(num[2*m-i-2]-z[i-1]-1,base))
        z.append(d(num[i-1]-x[i-1]-y[i]-c[i-1],base))
        c.append((x[i-1]+y[i]+z[i]+c[i-1]-num[i-1])//base)
    x.append(1 if z[m-2]<=num[m-1]-1 else 0)
    y.append(d(num[m-1]-z[m-2]-1,base))
    z.append(d(num[m-2]-x[m-2]-y[m-1]-c[m-2],base))
    c.append((x[m-2]+y[m-1]+z[m-1]+c[m-2]-num[m-2])//base)
    if x[m-1]+ c[m-1]==1:
        print("Do nothing")
    elif x[m-1]+c[m-1]==0 and y[m-1]!= base -1 :
        if z[m-1]!=0:
            y[m-1]+=1
            z[m-1]-=1
        elif z[m-1]==0 and y[m-2]!=0:
            if y[m-1]!=1 and z[m-2]!= base - 1:
                x[m-1]=1
                y[m-2]-=1
                y[m-1]-=1
                z[m-2]+=1
                z[m-1]+=1
            elif y[m-1]!=1 and z[m-2]==base - 1:
                x[m-1]=2
                y[m-2]-=1
                y[m-1]-=2
                z[m-2]=0
                z[m-1]=3
            elif y[m-1]==1:
                x[m-1]=1
                y[m-2]-=1
                y[m-1]=base - 1
                z[m-2]=0
                z[m-1]=3
        elif z[m-1]==0 and y[m-2]==0:
            if z[m-2]!= base - 1:
                x[m-2]-=1
                x[m-1]=1
                y[m-2]=base - 1
                y[m-1]-=1
                z[m-2]+=1
                z[m-1]=1
            elif z[m-2]== base - 1 and y[m-1]!=1:
                x[m-2]-=1
                x[m-1]=2
                y[m-2]=base-1
                y[m-1]-=2
                z[m-2]=0
                z[m-1]=3
            elif z[m-2]== base - 1 and y[m-1]==1:
                x[m-2]-=1
                x[m-1]=1
                y[m-2]=base-1
                y[m-1]=base-1
                z[m-2]=0
                z[m-1]=3
    elif x[m-1]+c[m-1]==0 and y[m-1]==base-1:
        x[m-1]=1
        y[m-2]-=1
        y[m-1]=base-2
        z[m-2]+=1
        z[m-1]=1
    elif x[m-1]+c[m-1]==2 and x[m-1]==0 and c[m-1]==2:
        if z[m-1]!=base-1:
            y[m-1]-=1
            z[m-1]+=1
        elif z[m-1]==base-1 and z[m-2]!=base-1:
            if y[m-2]!=0:
                x[m-1]=1
                y[m-2]-=1
                y[m-1]-=2
                z[m-2]+=1
                z[m-1]=1
            elif y[m-2]==0:
                x[m-2]-=1
                x[m-1]=1
                y[m-2]=base-1
                y[m-1]-=2
                z[m-2]+=1
                z[m-1]=1
        elif z[m-1]==base-1 and z[m-2]==base-1:
            if y[m-2]<base-2:
                if y[m-2]!=base-1:
                    x[m-2]-=1
                    x[m-1]=base-2
                    y[m-2]+=1
                    y[m-1]+=2
                    z[m-1]=base-2
                    z[m-2]=base-2
                else:
                    x[m-1]=base-2
                    y[m-2]=0
                    y[m-1]+=2
                    z[m-1]=base-2
                    z[m-2]=base-2
            else:
                if y[m-2]>=1:
                    x[m-1]=2
                    y[m-2]-=1
                    y[m-1]-=3
                    z[m-2]=0
                    z[m-1]=3
                else:
                    x[m-2]-=1
                    x[m-1]=2
                    y[m-2]=base-1
                    y[m-1]-=3
                    z[m-2]=0
                    z[m-1]=3
    elif x[m-1]+c[m-1]==2 and x[m-1]==1 and c[m-1]==1:
        if z[m-1]!=base-1 and y[m-1]!=0:
            y[m-1]-=1
            z[m-1]+=1
        elif z[m-1]!=base-1 and y[m-1]==0:
            x[m-1]=0
            y[m-1]=base-1
            z[m-1]+=1
        elif z[m-1]==base-1 and z[m-2]!=0:
            if y[m-2]!=base-1:
                x[m-1]=0
                y[m-2]+=1
                y[m-1]+=1
                z[m-2]-=1
                z[m-1]=base-2
            elif y[m-2]==base-1 and y[m-1]>1:
                x[m-1]=2
                y[m-2]=base-2
                y[m-1]-=2
                z[m-2]+=1
                z[m-1]=1
            elif y[m-2]==base-1 and y[m-1]==0:
                y[m-2]=base-2
                y[m-1]=base-2
                z[m-2]+=1
                z[m-1]=1
            elif y[m-2]==base-1 and y[m-1]==1:
                y[m-2]=base-2
                y[m-1]=base-1
                z[m-2]+=1
                z[m-1]=1 
        elif z[m-1]==base-1 and z[m-2]==0 and y[m-2]!=0:
            if y[m-1]>1:
                x[m-1]=2
                y[m-2]-=1
                y[m-1]-=2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==0:
                y[m-2]-=1
                y[m-1]=base-2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==1:
                y[m-2]-=1
                y[m-1]=base-1
                z[m-2]=1
                z[m-1]=1
        elif z[m-1]==base-1 and z[m-2]==0 and y[m-2]==0:
            if y[m-1]>1:
                x[m-2]-=1
                x[m-1]=2
                y[m-2]=base-1
                y[m-1]-=2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==0:
                x[m-2]-=1
                y[m-2]=base-1
                y[m-1]=base-2
                z[m-2]=1
                z[m-1]=1
            elif y[m-1]==1:
                x[m-2]-=1
                y[m-2]=base-1
                y[m-1]=base-1
                z[m-2]=1
                z[m-1]=1
    elif x[m-1]+c[m-1]==3:
        y[m-1]-=1
        z[m-1]=0
    y,z=y[1:],z[1:]
    x,y=x+x[::-1],y+y[::-1]
    t_z=z[::-1]
    z=z+t_z[1:]
    config=[x,y,z]
    return config
    
