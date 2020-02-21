def five_digit_sum(num,base):
    #perm=num #perm is the number the shallow copy of the actual number
    if num[0]!=1:
        [types,config,special]=check_type(num,base)
        return algorithm_1(num,config,base,types)
    else:
        [d0,d1,d2,d3,d4]=num[::-1]
        i1=1*(base**4 + 1)+ d3*(base+base**3) #1d30d31
        deci_num=d0+d1*base+d2*(base**2)+d3*(base**3)+d4*(base**4)
        m=deci_num-i1
        dp=d(m,base)
        i2=1*(base**4 + 1)+ (d3-1)*(base+base**3)+(base-1)*(base**2)
        m2=deci_num-i2
        dpp=d(m2,base)
        tho=2*(base**2)+1
        if (deci_num>=i1 and m!=tho) and (dp==0 or dp==base-1 or m!=(dp+1)*base+dp):
            m=fromDeci(m,base)
            m=hex_int_to_lst(m)
            if len(m)==2:
                extra=two_digit_sum(m,base)
            elif len(m)==3:
                extra=three_digit_sum(m,base)
            elif len(m)==4:
                extra=four_digit_sum(m,base)
            else:
                extra=five_digit_sum(m,base)
            config1=[[1,d3,0,d3,1]]
            config1.append(extra[0])
            config1.append(extra[1])
            return config1
        elif deci_num>=i1 and m==tho:
            return [[1,d3,1,d3,1],[1,0,1]]
        elif deci_num>=i1 and m==(dp+1)*base+dp and 1<=dp<=base-2 and d3!=0:
            if dp+1+d3<=base-1:
                return [[1,d3-1,1,d3-1,1],[base-1,dp+1,base-1],[dp+1]]
            elif d3+1+dp==base+d1:
                return [[1,d3-1,1,d3-1,1],[base-1,dp+1,base-1],[dp+1]]
        elif deci_num>=i1 and m==(dp+1)*base+dp and 1<=dp<=base-2 and d3==0:
            return [[base-1,base-1,base-1,base-1],[dp+1,dp+1],[1]]
        elif deci_num<i1 and d3==0:
            return [[base-1]*4,[1],[0]]
        elif (deci_num<i1 and d3!=0 and m2!=tho) and (dp==0 or dp==base-1 or m2!=(dpp+1)*base+dpp):
            m=fromDeci(m,base)
            m=hex_int_to_lst(m)
            if len(m)==2:
                extra=two_digit_sum(m,base)
            elif len(m)==3:
                extra=three_digit_sum(m,base)
            elif len(m)==4:
                extra=four_digit_sum(m,base)
            else:
                extra=five_digit_sum(m,base)
            config1=[[1,d3-1,base,d3-1,1]]
            config1.append(extra[0])
            config1.append(extra[1])
            return config
        else:
            return [[1,d3-1,base-2,d3-1,1],[1,dp+1,1],[dp-1]]
