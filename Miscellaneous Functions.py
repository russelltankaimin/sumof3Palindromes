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
  num_to_hex={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
  x,y,z='','',''
  for num in p1:
    if num<10:
      x=x+str(num)
    else:
      x=x+num_to_hex[num]
  for ber in p2:
    if ber <10:
      y=y+str(ber)
    else:
      y=y+num_to_hex[ber]
  for phile in p3:
    if phile<10:
      z=z+str(phile)
    else:
      z=z+num_to_hex[phile]
  print(x)
  print("+"+y)
  print("+ "+z)
  print("--------------------------")
  print(hex(num_string))
