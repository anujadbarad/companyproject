sum = 0
a=1
b=2
temp = 0
while a <= 4000000:
  if a % 2 == 0 :
    sum = sum + a
  temp = a
  a = b
  b = temp + b
print(sum)    
