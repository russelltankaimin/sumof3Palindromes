def algorithm_3(p1,p2,p3,base,num_string):
    num=num_string[::-1]
    p1.remove(p1[0])
    length=len(num)
    m=(length-1)//2
    carry=[]
    carry.append((1+p2[0]+p3[0])//base)
    if p3[0]<=int(num[2*m-3])-1:
        p1.append(d(int(num[2*m-2])-p2[0],base))
    elif p3[0]>=int(num[2*m-3]):
        p1.append(d(int(num[2*m-2])-p2[0]-1,base))
    p2.append(d(int(num[2*m-3])-p3[0]-1,base))
    p3.append(d(int(num[1])-p1[0]-p2[1]-carry[0],base))
    carry.append((p1[0]+p2[1]+p3[1]+carry[0]-int(num[1]))//base)
    for i in range(3,m):
        if p3[i-2]<=int(num[2*m-i-1])-1:
            p1.append(1)
        elif p3[i-2]>=int(num[2*m-i-1]):
            p1.append(0)
        p2.append(d(int(num[2*m-i-1])-p3[i-2]-1,base))
        p3.append(d(int(num[i-1])-p1[i-2]-p2[i-1]-carry[i-2],base))
        carry.append((p1[i-2]+p2[i-1]+p3[i-1]+carry[i-2]-int(num[i-1]))//base)
    p1.append(0)
    p2.append(d(int(num[m-1])-carry[m-2]-p3[m-2]-p1[m-2],base))
    carry.append((p1[m-2]+p2[m-1]+p3[m-2])//base)
    p1=[1]+p1
    if carry[m-1]==1:
        print("No Adjustment Needed")
    elif carry[m-1]==0:
        print("Carry = 1")
        p1[m]=1
    elif carry[m-1]==2:
        print("Carry 2")
        if p2[m-2] !=0 and p3[m-2] != base - 1:
            p2[m-2]=p2[m-2]-1
            p2[m-1]=p2[m-1]-1
            p3[m-2]=p3[m-2]+1
        elif p2[m-2]!=0 and p3[m-2]==base - 1:
            p1[m]=1
            p2[m-2]=p2[m-2]-1
            p3[m-2]=0
        elif p2[m-2]==0 and p3[m-2] != base - 1:
            p1[m-1]=p1[m-1]-1
            p2[m-2]=base-1
            p2[m-1]=p2[m-1]-1
            p3[m-2]=p3[m-2]+1
        elif p2[m-2]==0 and p3[m-2] == base - 1:
            p1[m-1]=p1[m-1]-1
            p1[m]=1
            p2[m-2]=base-1
            p3[m-2]=0
    p3=p3+p3[::-1]
    temp_p2=p2[0:m-1]
    p2=temp_p2+p2[::-1]
    temp_p1=p1[0:m]
    p1=temp_p1+p1[::-1]
    return display(p1,p2,p3,num_string)
