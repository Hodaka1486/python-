import random
x=str(random.randint(100,999))
print(x)
user = str(input("please enter your number："))
if (x == user): print("congratulate you have got 60,000 ") 
elif(x[1]==user[1] and x[0] == user[0]) or (x[1]==user[1] and x[2] == user[2]):
       print("congratulate you have got 10,000")
elif(x[0]==user[0] or x[1]==user[1] or x[2] == user[2]):print("congratulate you have got 300")
else :print("sorry ,no money")
