f = open('12.dat')
inLines = f.readlines()
f.close()

# registers a-d (inclusive)
#day1 Registers
#registers = {"a": 0, "b": 0, "c": 0, "d": 0}
#day2 Registers
registers = {"a": 0, "b": 0, "c": 1, "d": 0}

# Instructions: inc X, dec X, 
#               cpy X Y -- copy X into Y
#               jnz X Y -- jump to instruction Y away, only if x is not zero

i=0
goAgain = True
while goAgain:
   try:
      inLines[i] = inLines[i].strip()
      if "i" in inLines[i][0]:
         #inc X
         registers[inLines[i][inLines[i].find(' ')+1::]] += 1
         i+=1
      elif "d" in inLines[i][0]:
         #dec X
         registers[inLines[i][inLines[i].find(' ')+1::]] -= 1
         i+=1
      elif "c" in inLines[i][0]:
         #cpy X Y
         X = inLines[i][inLines[i].find(' ')+1:inLines[i].rfind(' ')]
         Y = inLines[i][inLines[i].rfind(' ')+1::]
         try:
            registers[Y] = int(X)
         except ValueError:
            registers[Y] = registers[X]
         i+=1
      else:
         #jnz X Y
         X = inLines[i][inLines[i].find(' ')+1:inLines[i].rfind(' ')]
         Y = inLines[i][inLines[i].rfind(' ')+1::]
         try:
            if registers[X] != 0:
               i=i+int(Y)
            else:
               i+=1
         except KeyError:
            if int(X) != 0:
               i=i+int(Y)
            else:
               i+=1
   except IndexError:
      goAgain=False

print(registers['a'])
