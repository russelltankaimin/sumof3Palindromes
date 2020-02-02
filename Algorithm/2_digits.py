def two_digit_sum(num_string,base):
    num=num_string
    if base!=16:
        num=str_to_lst(num_string)
    num=num[::-1]
    if num[1]<=num[0]:
        p1=[num[1],num[1]]
        p2=[num[0]-num[1]]
        p3=[0]
    elif num[1]>num[0]+1:
        p1=[num[1]-1,num[1]-1]
        p2=[base+num[0]-num[1]+1]
        p3=[0]
    elif num[1]==num[0]+1:
        p1=[num[0],num[0]]
        p2=[base-1]
        p3=[1]
    if base==16:
        return hex_display(p1,p2,p3,num_string)
    else:
        return display(p1,p2,p3,num_string)
