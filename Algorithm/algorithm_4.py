def algorithm_4(p1,p2,p3,base,num_string):
    num=num_string[::-1]
    m=len(num)//2
    p2=[0]+p2
    p3=[0]+p3
    carry=[0]
    carry.append((1+p2[1]+p3[1])//base)
    if p3[1]<=int(num[2*m-4])-1:
        p1.append(d(int(num[2*m-3])-p2[1],base))
    elif p3[1]>= int(num[2*m-4]):
        p1.append(d(int(num[2*m-3])-p2[1]-1,base))
    p2.append(d(int(num[2*m-4])-p3[1]-1,base))
    p3.append(d(int(num[1])-p1[1]-p2[2]-carry[1],base))
    carry.append((p1[1]+p2[2]+p3[2]+carry[1])//base)
    for i in range(3,m-1):
        p1.append(1 if p3[i-1]<=int(num[2*m-i-2])-1 else 0)
        p2.append(d(int(num[2*m-i-2])-p3[i-1]-1,base))
        p3.append(d(int(num[i-1])-p1[i-1]-p2[i]-carry[i-1],base))
        carry.append((p1[i-1]+p2[i]+p3[i]+carry[i-1]-int(num[i-1]))//base)
    p1.append(1 if p3[m-2]<=int(num[m-1])-1 else 0)
    p2.append(d(int(num[m-1])-p3[m-2]-1,base))
    p3.append(d(int(num[m-2])-p1[m-2]-p2[m-1]-carry[m-2],base))
    carry.append((p1[m-2]+p2[m-1]+p3[m-1]+carry[m-2]-int(num[m-2]))//base)
    if p1[m-1]+carry[m-1]==1:
        print("No Adjustment needed")
    elif p1[m-1]+carry[m-1]==0 and p2[m-1]!=base - 1:
        if p3[m-1]!=0:
            p2[m-1]=p2[m-1]+1
            p3[m-1]=p3[m-1]-1
        elif p3[m-1]==0 and p2[m-2]!=0:
            if p2[m-1]!=1 and p3[m-2]!= base - 1:
                p1[m-1]=1
                p2[m-2]=p2[m-2]-1
                p2[m-1]=p2[m-1]-1
                p3[m-1]=1
                p3[m-2]=p3[m-2]+1
            elif p2[m-1]!=1 and p3[m-2]== base - 1 :
                p1[m-1]=2
                p2[m-1]=p2[m-1]-2
                p2[m-2]=p2[m-2]-1
                p3[m-2]=0
                p3[m-1]=3
            elif p2[m-1]==1:
                p1[m-1]=1
                p2[m-2]=p2[m-2]-1
                p2[m-1]=base-1
                p3[m-2]=0
                p3[m-1]=3
        elif p3[m-1]==0 and p2[m-2]==0:
            if p3[m-2]!= base - 1:
                p1[m-2]=p1[m-2]-1
                p1[m-1]=1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-1
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p3[m-2]==base -1 and p2[m-1]!=1:
                p1[m-1]=2
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=0
                p3[m-1]=3
            elif p3[m-2]==base - 1 and p2[m-1]==1:
                p1[m-2]=p1[m-2]-1
                p1[m-1]=1
                p2[m-2]=base-1
                p2[m-1]=base-1
                p3[m-2]=0
                p3[m-1]=3
    elif p1[m-1]+carry[m-1]==0 and p2[m-1]==base-1:
        p1[m-1]=1
        p2[m-2]=p2[m-2]-1
        p2[m-1]=base-2
        p3[m-2]=p3[m-2]+1
        p3[m-1]=1
    elif p1[m-1]+carry[m-1]==2 and p1[m-1]==0 and carry[m-1]==2:
        if p3[m-1]!=base-1:
            p2[m-1]=p2[m-1]-1
            p3[m-1]=p3[m-1]+1
        elif p3[m-1]==base-1 and p3[m-2]!=base-1:
            if p2[m-2]!=0:
                p1[m-1]=1
                p2[m-2]=p2[m-2]-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p2[m-2]==0:
                p1[m-2]=p1[m-2]-1
                p1[m-1]=1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
        elif p3[m-1]==p3[m-2]==base-1:
            if p2[m-1]!=base-1 and p2[m-1]!=base-2:
                if p2[m-2]!=base-1:
                    p1[m-2]=p1[m-2]-1
                    p1[m-1]=base-2
                    p2[m-2]=p2[m-2]+1
                    p2[m-1]=p2[m-1]+2
                    p3[m-2]=base-2
                    p3[m-1]=base-2
                else:
                    p1[m-1]=base-2
                    p2[m-2]=0
                    p2[m-1]=p2[m-1]+2
                    p3[m-2]=base-2
                    p3[m-1]=base-2
            elif p2[m-1]==base-1 or p2[m-1]==base-2:
                if p2[m-2]>=1:
                    p1[m-1]=2
                    p2[m-2]=p2[m-2]-1
                    p2[m-1]=p2[m-1]-3
                    p3[m-2]=0
                    p3[m-1]=3
                elif p2[m-2]==0:
                    p1[m-2]=p2[m-2]-1
                    p1[m-1]=2
                    p2[m-2]=base-1
                    p2[m-1]=p2[m-1]-3
                    p3[m-2]=0
                    p3[m-1]=3
    elif p1[m-1]+carry[m-1]==2 and p1[m-1]==1 and carry[m-1]==1:
        if p3[m-1]!=base-1 and p2[m-1]!=0:
            p2[m-1]=p2[m-1]-1
            p3[m-1]=p3[m-1]+1
        elif p3[m-1]!=base-1 and p2[m-1]==0:
            p1[m-1]=0
            p2[m-1]=base-1
            p3[m-1]=p3[m-1]+1
        elif p3[m-1]==base-1 and p3[m-2]!=0:
            if p2[m-2]!=base-1:
                p1[m-1]=0
                p2[m-2]=p2[m-2]+1
                p2[m-1]=p2[m-1]+1
                p3[m-2]=p3[m-2]-1
                p3[m-1]=base-2
            elif p2[m-2]==base-1 and p2[m-1]!=0 and p2[m-1]!=1:
                p1[m-1]=2
                p2[m-2]=base-2
                p2[m-1]=p2[m-1]-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p2[m-2]==base-1 and p2[m-1]==0:
                p2[m-2]=base-2
                p2[m-1]=base-2
                p3[m-2]=p3[m-2]+1
                p3[m-1]=1
            elif p2[m-2]==base-1 and p2[m-1]==1:
                p2[m-1]=base-1
                p2[m-2]=base-2
                p3[m-1]=1
                p3[m-2]=p3[m-2]+1
        elif p3[m-1]==base-1 and p3[m-2]==0 and p2[m-2]!=0:
            if p2[m-1]!=0 and p2[m-1]!=1:
                p1[m-1]=2
                p2[m-2]=p2[m-2]-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==0:
                p2[m-2]=p2[m-2]-1
                p2[m-1]=base-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==1:
                p2[m-2]=p2[m-2]-1
                p2[m-1]=base-1
                p3[m-2]=1
                p3[m-1]=1
        elif p3[m-1]==base-1 and p3[m-2]==0 and p2[m-2]==0:
            if p2[m-1]!=0 and p2[m-1]!=1:
                p1[m-1]=2
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=p2[m-1]-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==0:
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=base-2
                p3[m-2]=1
                p3[m-1]=1
            elif p2[m-1]==1:
                p1[m-2]=p1[m-2]-1
                p2[m-2]=base-1
                p2[m-1]=base-1
                p3[m-2]=1
                p3[m-1]=1
    elif p1[m-1]+carry[m-1]==3:
        p2[m-1]=p2[m-1]-1
        p3[m-1]=0
    p2=p2[1:m+1]
    p3=p3[1:m+1]
    p1=p1+p1[::-1]
    
