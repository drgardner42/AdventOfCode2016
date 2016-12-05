f = open('3.dat')
inLines = f.readlines()
f.close()
count=0
loopCount=0
colOne=[]
colTwo=[]
colThr=[]

for line in inLines:
   dimensions = line.strip().split()
   dimensions = list(map(int, dimensions))
   colOne.append(dimensions[0])
   colTwo.append(dimensions[1])
   colThr.append(dimensions[2])
   loopCount+=1

   #Only check once we have all triangle dimensions
   if loopCount == 3: 
      colOne.sort()
      colTwo.sort()
      colThr.sort()

      if colOne[0] + colOne[1] > colOne[2]:
         count+=1
      if colTwo[0] + colTwo[1] > colTwo[2]:
         count+=1
      if colThr[0] + colThr[1] > colThr[2]:
         count+=1

      # Reset vars for next set of dimensions
      colOne=[]
      colTwo=[]
      colThr=[]
      loopCount=0
   

print(count)
