keyPad = [['0', '0', '1', '0', '0'], 
          ['0', '2', '3', '4', '0'], 
          ['5', '6', '7',' 8', '9'],
          ['0', 'A', 'B', 'C', '0'],
          ['0', '0', 'D', '0', '0']]

f = open('2.dat')
inData = f.readlines()
f.close()

"""curY = 1
curX = 1
for line in inData:
   line = line.strip('\n')
   for char in line:
      if "U" in char:
         if curY%3!=0:
            curY-=1
      elif "D" in char:
         if curY%3!=2:
            curY+=1
      elif "R" in char:
         if curX%3!=2:
            curX+=1
      elif "L" in char:
         if curX%3!=0:
            curX-=1
   print(keyPad[curY][curX])"""

curY=2
curX=0

for line in inData:
   line = line.strip('\n')
   for char in line:
      if "U" in char:
         if curY%5!=0:      #Cant decrement if in top row
            if curX%4!=0:   #Cant decrement if on 5 or 9
               if (curX==1 or curX==3) and curY==1:
                  pass
               else:
                  curY-=1
      elif "D" in char:
         if curY%5!=4:
            if curX%4!=0:
               if(curX==1 or curX==3) and curY==3:
                  pass
               else:
                  curY+=1
      elif "R" in char:
         if curX%5!=4:
            if curY%4!=0:
               if(curY==1 or curY==3) and curX==3:
                  pass
               else:
                  curX+=1
      elif "L" in char:
         if curX%5!=0:
            if curY%4!=0:
               if (curY==1 or curY==3) and curX==1:
                  pass
               else:
                  curX-=1
   print(keyPad[curY][curX])
