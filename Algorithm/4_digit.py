def four_digit_sum(num,base):
    perm=num
    [d0,d1,d2,d3]=num[::-1]
    n=perm[0]*(base**3)+perm[1]*(base**2)+perm[2]*base+perm[3]
    if n>=d3*(base**3)+d3:
        m=n-d3*(base**3)-d3
        dp=d(m,base)
        if m==2*(base**2)+1:
            if d3==1:
                return[[1,1,1,1],[base-2,base-2],[3]]
            elif d3==base-1:
                return [[base-1,1,1,base-1],[base-2,base-2],[3]]
            else:
                return [[d3-1,base-1,base-1,d3-1],[2,1,2],[0]]
        elif (1<=dp<=base-2 and m==(dp+1)*base+dp):
            if(d3+dp==d0):
                if d3!=1:
                    return [[d3-1,base-2,base-2,d3-1],[1,3,1],[dp,dp]]
                else:
                    return [[base-1,base-1,base-1],[dp+1,dp+1],[1]]
            else:
                return [[d3-1,base-2,base-2,d3-1],[1,3,1],[dp,dp]]
        elif d2==0 and d1==0 and d0<=d3-1 and d3!=1:
            return [[d3-1,base-1,base-1,d3-1],[base+d0-d3],[1]]
        elif [d0,d1,d2,d3]==[0,0,0,1]:
            return [[base-1,base-1,base-1],[1],[0]]
        else:
            m=fromDeci(m,base)
            m=[int(m[i]) for i in range(0,len(m))]
            if len(m)==2:
                extra=two_digit_sum(m,base)
            elif len(m)==3:
                extra=three_digit_sum(m,base)
            else:
                extra=four_digit_sum(m,base)
            config=[[d3,0,0,d3]]
            config.append(extra[0])
            config.append(extra[1])
            return config
    elif d0<=d3-1 and d3!=1:
        return [[d3-1,base-1,base-1,d3-1],[base+d0-d3],[1]]
    else:
        return [[base-1,base-1,base-1],[1],[0]]
