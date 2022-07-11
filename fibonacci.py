prst = 0
prev1 = 0
for x in range(100):
  if (prst == 0 and prev1 == 0):
    prev1 = 0
    prst = 1
  else:
    tmp = prev1
    prev1 = prst + prev1
    prst = tmp
  print(prst + prev1)