import re

f = open('7.dat')
inLines = f.readlines()
f.close()

stack = []
count=0
for line in inLines:
   line = line.strip()
   hypernets = []
   hyperString = ""
   regularStrings = []
   regularString = ""
   i=0
   for c in line:
      if c == "[":
         stack.append(c)
         regularStrings.append(regularString)
         regularString = ""
      elif len(stack) > 0 and stack[0] == "[":
         if c == "]":
            stack.pop()
            hypernets.append(hyperString)
            hyperString =""
         else:
            hyperString += c
      else:
         regularString += c 
   regularStrings.append(regularString)

   abaList = []
   for strings in regularStrings:
      for i in range(0, len(strings)-2):
         testSubString = strings[i:i+3]
         match = re.search(r'([a-z]{1})[a-z]{1}\1', testSubString)
         if match:
            if match.string[0] != match.string[1]:
               abaList.append(match.string)

   foundMatch = False
   if len(abaList) > 0:
      #run through hyperStrings looking for a bab match
      for hypernet in hypernets:
         if not foundMatch:
            for i in range(0, len(hypernet)-2):
               if not foundMatch:
                  testSubString = hypernet[i:i+3]
                  match = re.search(r'([a-z]{1})[a-z]{1}\1', testSubString)
                  if match:
                     for aba in abaList:
                        if not foundMatch:
                           if aba[0] == match.string[1] and aba[1] == match.string[0]:
                              count+=1
                              foundMatch = True
   else:
      pass #nothing to do

print(count)
