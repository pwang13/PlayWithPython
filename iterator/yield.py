def countdown(n):
   while n >= 0:
     # return  n
     yield n
     n -= 1

print("We are go for launch")
for x in countdown(10):
   print(x)
print("lift off!")