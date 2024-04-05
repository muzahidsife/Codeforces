s=input()

sl={}

count=0
for i in s:
    if i not in sl:
        sl[i]=0
    sl[i]+=1
for j in sl:
    count+=1
if count%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")