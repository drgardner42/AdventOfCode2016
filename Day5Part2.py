import hashlib
import codecs

key = "ugkcyxxp"
password = ['0', '0', '0', '0', '0', '0', '0', '0']
alreadyUsed = [False, False, False, False, False, False, False, False]
i=0
goAgain = True
count=0
while(goAgain):
   foo = key + str(i)
   md5Foo = hashlib.md5(foo.encode()).hexdigest()

   if "00000" in md5Foo[0:5]:
      if md5Foo[5].isnumeric():
         position = int(md5Foo[5])
         if position < 8 and not alreadyUsed[position]:
            password[int(position)] = md5Foo[6]
            alreadyUsed[position] = True
            count+=1
   if count==8:
      goAgain=False
      print(password)
   i+=1
