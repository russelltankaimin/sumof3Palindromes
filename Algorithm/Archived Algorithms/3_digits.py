def three_digit_sum(num,base):
    if base<11:
        num=str_to_lst(num)
    num=num[::-1]
    if num[2]<=num[0]:
        p1=[num[2],num[1],num[2]]
        p2=[num[0]-num[2]]
        p3=[0]
    elif num[2]>=num[0]+1:
        if num[1]!=0:
            p1=[num[2],num[1]-1,num[2]]
            p2=[base+num[0]-num[2]]
            p3=[0]
        else:
            if d(num[2]-num[0]-1,base)!=0:
                p1=[num[2]-1,base-1,num[2]-1]
                p2=[base+num[0]-num[2]+1]
                p3=[0]
            else:
                if num[2]>=3:
                    p1=[num[2]-2,base-1,num[2]-2]
                    p2=[111]
                    p3=[0]
                elif num[2]==2:
                    p1=[101]
                    p2=[base-1,base-1]
                    p3=[1]
                else:
                    p1=[base-1,base-1]
                    p2=[1]
                    p3=[0]
    num=num[::-1]
    if base>10:
        return hex_display(p1,p2,p3,num)
    else:
        return display(p1,p2,p3,num)
