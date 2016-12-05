f = open('3.dat')
inLines = f.readlines()
f.close()
count=0

for line in inLines:
   dimensions = line.strip().split()
   dimensions = list(map(int, dimensions))
   dimensions.sort()

   if int(dimensions[0])+int(dimensions[1]) > int(dimensions[2]):
      count+=1

print(count)
