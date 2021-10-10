strin=input()
ls=list(strin)
if ls[0]=="-":
       del ls[0]
       print("-",end='')
       ls.reverse()
       ls.remove("0")
       print("".join(ls))
else:
       ls.reverse()
       ls.remove("0")
       print("".join(ls))
       
              
