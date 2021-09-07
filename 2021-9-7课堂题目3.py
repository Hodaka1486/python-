n=int(input("please enter how many students:"))
name=[]
score=[]
name_score={}
name_score_2={}
for i in range(n):
       print("enter the name ")
       name.append(input())
       print("enter   score")
       score.append(int(input()))
       name_score[name[i]]=score[i]
print(name_score.items())
sorted(name_score.values())
print("this is sorted list")
print(name_score.items())

