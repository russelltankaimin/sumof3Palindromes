def is_special(num_str,types):
  if types == "A5" or types == "A6":
      length_of_p1=len(num_str)-1
  else:
      length_of_p1=len(num_str)
  if length_of_p1%2!=0:
      return False
  else:
      num=num_str[::-1]
      m=length_of_p1>>1
      if int(num[m])==0 or int(num[m-1])==0:
          return True
      else:
          return False
