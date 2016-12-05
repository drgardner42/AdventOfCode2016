import hashlib
import codecs

key = "ugkcyxxp"
password = ""
i=0
goAgain = True
count=0
while(goAgain):
   foo = key + str(i)
   md5Foo = hashlib.md5(foo.encode()).hexdigest()

   if "00000" in md5Foo[0:5]:
      password += md5Foo[5]
      count+=1
   if count==8:
      goAgain=False
      print(password)
   i+=1
