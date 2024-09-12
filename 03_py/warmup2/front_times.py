def front_times(str, n):
  if(len(str)) < 3:
    return str * n
  else:
    return n * str[0:3]
