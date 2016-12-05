f = open('1.dat')
inData = f.readline().split(",")
f.close()

heading = "N"
position = [0,0]
visitedSet = list()
for i in inData:
   i = i.strip()
   if "N" in heading:
      if "L" in i:
         for j in range(0, int(i[1::])):
            position[0] -= 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "W"
      elif "R" in i:
         for j in range(0, int(i[1::])):
            position[0] += 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "E"
   elif "E" in heading:
      if "L" in i:
         for j in range(0, int(i[1::])):
            position[1] += 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "N"
      elif "R" in i:
         for j in range(0, int(i[1::])):
            position[1] -= 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "S"
   elif "S" in heading:
      if "L" in i:
         for j in range(0, int(i[1::])):
            position[0] += 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "E"
      elif "R" in i:
         for j in range(0, int(i[1::])):
            position[0] -= 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "W"
   elif "W" in heading:
      if "L" in i:
         for j in range(0, int(i[1::])):
            position[1] -= 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "S"
      elif "R" in i:
         for j in range(0, int(i[1::])):
            position[1] += 1
            if position in visitedSet:
               print(abs(position[0])+abs(position[1]))
            else:
               visitedSet.append((position[:]))
         heading = "N"

print(abs(position[0])+abs(position[1]))
