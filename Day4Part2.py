import collections

def caesar(cipherText, shift):
   shift = shift%26 #lets get the real shift here...
   plainText = "" 
   for c in cipherText:
      if c is '-':
         plainText += " "
      else:
         foo = ord(c)+shift
         if foo > 122:
            plainText += chr(96 + (foo%122))
         else:
            plainText += chr(foo)
   return plainText

f = open('4.dat')
inLines = f.readlines()
f.close()

total=0
for line in inLines:
   line = line.strip()
   substrings = line.split('-')

   last = substrings[len(substrings)-1]
   checksum = last[last.find('[')+1:last.find(']')]
   sectorID = last[0:last.find('[')]

   totalString = []
   for string in substrings:
      if string[0].isdigit() == 0:
         sortedString = sorted(string)
         totalString.extend(sortedString) 
   totalString = sorted(totalString)
   counter = collections.Counter(totalString)

   decoy = False
   localMax=int(counter[checksum[0]])
   prevC = checksum[0]
   for c in checksum[1::]:
      if not decoy:
         if int(counter[c]) > 0:
            if localMax > int(counter[c]): #If the next count is lower, adjust localMax & move on
               localMax = int(counter[c])
            elif localMax == int(counter[c]):
               #Check that previousC is < currentC   
               if prevC > c:
                  decoy = True
            else:
              decoy = True
         else:
            decoy = True
         prevC = c
   if not decoy:
      temp = caesar(line[:line.rfind("-")], int(sectorID))
      if "north" in temp:
         print(temp)
         print(sectorID)

