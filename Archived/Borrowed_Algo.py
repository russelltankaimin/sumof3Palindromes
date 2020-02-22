def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10
        
def toDeci(string,base): 
    llen = len(string) 
    power = 1 
    num = 0    
    for i in range(llen - 1, -1, -1): 
        if val(string[i]) >= base: 
            print('Invalid Number') 
            return -1
        num += val(string[i]) * power 
        power = power * base 
    return num
    
def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0')); 
    else: 
        return chr(num - 10 + ord('A')); 
        
def fromDeci(inputNum,base): 
    res=''
    index = 0
    while (inputNum > 0): 
        res+= reVal(inputNum % base); 
        inputNum = int(inputNum / base); 
    res = res[::-1]; 
  
    return res
 Credits: https://www.geeksforgeeks.org/convert-base-decimal-vice-versa/
