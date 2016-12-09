f = open('9.dat')
inLine = f.readline()
f.close()
#inLine = "ADVENT"
#inLine = "A(1x5)BC"
#inLine = "(3x3)XYZ"
#inLine = "A(2x2)BCD(2x2)EFG"
#inLine = "(6x1)(1x3)A"
#inLine = "X(8x2)(3x3)ABCY"

unCompressed = ""
repeating = False
captureGroup = False
captureString = ""
count=0
numChars = ""
numRepeats = ""
total=0

for i in range(len(inLine)):
   if inLine[i] != " ":
      if not repeating:
         if inLine[i]  == "(":
            captureGroup = False 
            repeating = True
            captureString = ""
         else:
            unCompressed += inLine[i]
      else:
         if not captureGroup:
            if inLine[i] != ")":
               captureString += inLine[i]
            else:
               captureGroup = True
               numChars = captureString[:captureString.find('x')]
               numRepeats = captureString[captureString.find('x')+1::]
               print(numChars, numRepeats)
               total = total+(int(numChars)*int(numRepeats))
         else:
            #we need to create the string to append numRepeats amount of times
            if count  < int(numChars):
               count+=1
               if count == int(numChars):
                  repeating = False
                  captureGroup = False
                  count=0
                  numChars = ""
                  numRepeats = ""

print(total)
