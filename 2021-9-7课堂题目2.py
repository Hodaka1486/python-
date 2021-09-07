x={"A":10 ,"B":9,"C":7,"D":4}
level=input("please enter your level:")
sum=0
print(x[level[0]])
for i in range(10):
       number =x[level[i]]
       sum+=number
print("this is your score:",end='')
print(sum)
