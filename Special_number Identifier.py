def is_special(p1):
  if(len(p1)%2==1):
    return False
  else:
    m = len(p1)//2
    print(m)
    if p1[-m]==0 or p1[-1-m]==0:
      return True
    else:
      return False
