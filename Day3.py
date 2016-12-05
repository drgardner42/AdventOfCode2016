f = open('3.dat')
inLines = f.readlines()
f.close()
count=0

for line in inLines:
   dimensions = line.strip().split()
   dimensions = list(map(int, dimensions))
   dimensions.sort()

   if dimensions[0]+dimensions[1] > dimensions[2]:
      count+=1

print(count)
