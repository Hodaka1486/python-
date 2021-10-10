si=input()
a=list(si)
s=""
s1=""
for i in range(0,len(a)-1):
       for j in range(10000):
              if a[i]==a[i+1] and a[i]>="A" and a[i]<="Z":
                     del a[i+1]
                     a.append(" ")
              else:
                     break
s1="".join(a)
s1.strip()
print("this has changed:",s1)
for i in range(4,len(s1),5):
       s+=s1[i+1]
       i+=1
print(s)
