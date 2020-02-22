def d(num,base):
    return num%base
  
def str_to_lst(num):
  num=str(num)
  lst=[]
  for digit in num:
    lst.append(int(digit))
  return lst  

def parse_list_to_int(lst):
    string=''
    for num in lst:
        string=string+str(num)
    return int(string)

def display(p1,p2,p3,num_string):
    r1,r2,r3='','',''
    for i in range(0,len(p1)):
        r1=r1+str(p1[i])
    for j in range(0,len(p2)):
        r2=r2+str(p2[j])
    for k in range(0,len(p3)):
        r3=r3+str(p3[k])
    print(r1)
    print("+"+r2)
    print("+ "+r3)
    print("----------------------")
    print(num_string)

def hex_display(p1,p2,p3,num_string):
  x,y,z='','',''
  for num in p1:
    if num<10:
      x=x+str(num)
    else:
      x=x+hex(num)[2:].upper()
  for ber in p2:
    if ber <10:
      y=y+str(ber)
    else:
      y=y+hex(ber)[2:].upper()
  for phile in p3:
    if phile<10:
      z=z+str(phile)
    else:
      z=z+hex(phile)[2:].upper()
  print(x)
  print("+"+y)
  print("+ "+z)
  print("--------------------------")
  print(hex(num_string)[2:].upper())

def hex_int_to_lst(num):
    hex_to_dec={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1,"0":0}
    lst=[]
    reck=str(num)
    for i in reck:
        lst.append(hex_to_dec[i])
    return lst

def lst_to_hex_int(num_list):
    string_hex=''
    for integer in num_list:
        string_hex=string_hex+hex(integer)[2:].upper()
    return string_hex
