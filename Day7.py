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

   foundMatch = False
   for hypernet in hypernets:
      if not foundMatch:
         for i in range(0, len(hypernet)-3):
            testSubString = hypernet[i:i+4]
            match = re.search(r'([a-z]{1})([a-z]{1})\2\1', testSubString)
            if match:
               if match.string[0] != match.string[1]:
                  foundMatch = True

   foundGoodMatch=False
   if not foundMatch:
      for strings in regularStrings:
         if not foundGoodMatch:
            for i in range(0, len(strings)-3):
               if not foundGoodMatch:
                  testSubString = strings[i:i+4]
                  match = re.search(r'([a-z]{1})([a-z]{1})\2\1', testSubString)
                  if match:
                     if match.string[0] != match.string[1]:
                        foundGoodMatch = True
                        count+=1
print(count)
