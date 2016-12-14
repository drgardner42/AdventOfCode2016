class Bot(object):
   def __init__(self):
      self.valueLow = 0
      self.valueHigh = 0
      self.passReady = False
   def setValues(self, value):
      if value > self.valueHigh:
         self.valueLow = self.valueHigh
         self.valueHigh = value
      else:
         self.valueLow = value
      if self.valueLow > 0 and self.valueHigh > 0:
         self.passReady = True
   def setLow(self, value):
      self.lowPass = value
   def setHigh(self, value):
      self.highPass = value

   def getLowBotValue(self):
      return self.valueLow
   def getHighBotValue(self):
      return self.valueHigh
   def getLowPass(self):
      return self.lowPass
   def getHighPass(self):
      return self.highPass
   def getPassReady(self):
      return self.passReady

f = open('10.dat')
inLines = f.readlines()
f.close()

bots = {n: Bot() for n in range(1000)}
outputs = [0 for n in range(100)]

for line in inLines:
   line = line.strip()
   if line[0] != "v":
      # Rules
      # bot X gives low to bot Y and high to bot Z 
      botInQuestion = int(line[line.find('b')+4:line.find('g')-1])
      if "output" in line:
         # bot 134 gives low to output 10 and high to bot 182
         # bot 208 gives low to output 4 and high to output 13
         #print("line.find(output): ", line.find('output') )
         botForLow = 'OUT' + line[line.find('output')+7:line.find('a')-1]      
         if line[line.find('h')+8] == 'b':
            botForHigh = line[line.find('h')+12::]
         else:
            botForHigh = 'OUT' + line[line.find('h')+15::]
      else:
         botForLow = line[line.find('l')+11:line.find('a')-1]
         botForHigh = line[line.find('h')+12::]
      bots[botInQuestion].setLow(botForLow)
      bots[botInQuestion].setHigh(botForHigh)
      #print(botInQuestion, botForLow, botForHigh)

for line in inLines:
   if line[0] == "v":
      #value X goes to bot X
      valueToBot = int(line[line.find('v')+6:line.find('g')-1])
      goesToBot = int(line[line.find('b')+4::])
      bots[goesToBot].setValues(valueToBot)
      if bots[goesToBot].getPassReady() == True:
         chainReaction = True
         stack = [goesToBot]
         while(chainReaction):
            goesToBot = stack.pop()
            botToPassHigh = bots[goesToBot].getHighPass()
            botToPassLow = bots[goesToBot].getLowPass()
            
            valueToHigh = bots[goesToBot].getHighBotValue()
            valueToLow = bots[goesToBot].getLowBotValue()

            if valueToHigh == 61 and valueToLow == 17:
               print(goesToBot)
            
            if "OUT" in botToPassHigh:
               botToPassHigh = int(botToPassHigh[3::])
               outputs[int(botToPassHigh)] = valueToHigh
            else:
               bots[int(botToPassHigh)].setValues(valueToHigh)
            if "OUT" in botToPassLow:
               botToPassLow = int(botToPassLow[3::])
               outputs[int(botToPassLow)] = valueToLow
            else:
               bots[int(botToPassLow)].setValues(valueToLow)

            bots[goesToBot] = Bot()

            if bots[int(botToPassHigh)].getPassReady() == True:
               stack.append(int(botToPassHigh))
            if bots[int(botToPassLow)].getPassReady() == True:
               stack.append(int(botToPassLow))
            
            if len(stack) == 0:
               chainReaction = False
print(outputs[0]*outputs[1]*outputs[2])
