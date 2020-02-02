def algorithm_1(p1,p2,p3,base,num_string):
    num=num_string[::-1]
    length=len(num_string)
    if length%2==0:
        m=(length-2)//2
    else:
        m=(length-1)//2
    carry=[]
    c1=(p1[0]+p2[0]+p3[0])//base
    carry.append(c1)
    if  p3[0]<=int(num[2*m-2])-1:
        p1.append(d(int(num[2*m-1])-p2[0],base))
    elif p3[0]>=int(num[2*m-2]):
        p1.append(d(int(num[2*m-1])-p2[0]-1,base))
    p2.append(d(int(num[2*m-2])-p3[0]-1,base))
    p3.append(d(int(num[1])-p1[1]-p2[1]-carry[0],base))
    carry.append((p1[1]+p2[1]+p3[1])//base)
    for i in range(3,m+1):
        if p3[i-2]<=int(num[2*m-i])-1:
            p1.append(1)
        elif p3[i-2]>=int(num[2*m-i]):
            p1.append(0)
        p2.append(d(int(num[2*m-i])-p3[i-2]-1,base))
        p3.append(d(int(num[i-1])-p1[i-1]-p2[i-1]-carry[i-2],base))
        carry.append((p1[i-1]+p2[i-1]+p3[i-1]+carry[i-2]-int(num[i-1]))//base)
    p1.append(0)
    vital_carry=carry[m-1]
    if vital_carry==1:
        print("No Adjustment Step needed")
    elif vital_carry==2:
        print("Adjustment needed")
        p1[m]=1
        p2[m]=p2[m]-1
        p3[m-1]=0
    elif vital_carry==0:
        print("Adjustment needed")
        p1[m]=1
    temp_p1=p1[::-1]
    temp_p3=p3[::-1]
    p1=p1+temp_p1[1:m+1]
    p2=p2+p2[::-1]
    p3=p3+temp_p3[1:m]
    if base==16:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)
