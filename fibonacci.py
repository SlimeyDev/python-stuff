prev0 = 0
prev1 = 0
for x in range(100):
  if (prev0 == 0 and prev1 == 0):
    prev1 = 0
    prev0 = 1
  else:
    tmp = prev1
    prev1 = prev0 + prev1
    prev0 = tmp
  print(prev0 + prev1)