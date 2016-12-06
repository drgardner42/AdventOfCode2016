import collections

f = open('6.dat')
inLines = f.readlines()
f.close()

cols = [[], [], [], [], [], [], [], [] ]

for line in inLines:
   index=0
   line=line.strip()
   for c in line:
      cols[index].append(c)
      index+=1

message=""
for i in range(0,len(cols)):
   counts = collections.Counter(cols[i])
   print(counts)
