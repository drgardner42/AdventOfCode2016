import collections
f = open('8.dat')
inLines = f.readlines()
f.close()

screen = [['.' for x in range(50)] for y in range(6)]

for line in inLines:
   line = line.strip()
   if "rect" in line:
      wide = int(line[5:line.find('x')])
      tall = int(line[line.find('x')+1::])
      for i in range(0, tall):
         for j in range(0, wide):
            screen[i][j] = '#'
   elif "rotate" in line:
      if "row" in line:
         selectedRow = int(line[line.find('y')+2:line.find('y')+3])
         shiftAmount = int(line[line.find('by')+2::])
         tempRow = ['.' for x in range(50)]
         for i in range(0, 50):
            if screen[selectedRow][i] == "#":
               newLoc = (i+shiftAmount)%50
               tempRow[newLoc] = '#'
         screen[selectedRow] = tempRow
               
      elif "column" in line:
         selectedCol = int(line[line.find('x')+2:line.find('by')-1])
         shiftAmount = int(line[line.find('by')+2::])
         tempCol = ['.' for x in range(6)]
         for i in range(6):
            if screen[i][selectedCol] == "#":
               newLoc = (i+shiftAmount)%6
               tempCol[newLoc] = "#"
         for i in range(6):
            screen[i][selectedCol] = tempCol[i]

count=0
for i in range(6):
   counts = collections.Counter(screen[i])
   count += counts['#'] 
print(count)
