import random
import time
import math

def score(like,dislike,ans):
    n=0
    k=len(like)
    for i in range(k):
        f=True
        for li in like[i][1:]:
            if li in ans:
                pass
            else:
                f=False
                break
        if f:
            for di in dislike[i][1:]:
                if di in ans:
                    f=False
                    break
                else:
                    pass
        if f:
            n+=1
    return n


##dislike_giant=[]
##like_giant=[]
##like=[];dislike=[]
##number=int(input())
##for _ in range(number):
##    a=input().split()
##    b=input().split()
##    like.append(a)
##    dislike.append(b)
##    like_giant.extend(a)
##    dislike_giant.extend(b)    
##like_giant=list(set(like_giant))
##dislike_giant=list(set(dislike_giant))
##
##
##ingredients=[]
##dontadd=[]
##for ii in like_giant:
##    if ii in dislike_giant:
##        pass
##    else:
##        ingredients.append(ii)
##bit=[]
##order=[]
##number=len(like)
##for i in range(number):
##    order.append([len(dislike[i]),i])
##order.sort()
##
##f=1
##for x in range(number):
##    y=order[x][1]
##    for elem in dislike[y][1:]:
##        if elem in dontadd:
##            f=0
##            break
##    if f:
##        ingredients=list(set(ingredients+like[y][1:]))
##        dontadd=list(set(dontadd+dislike[y][1:]))
##        bit.append(1)
##    else:
##        bit.append(0)



d={}
like=[]
dislike=[]
test=int(input())
for z in range(test):
    ll=list(map(str,input().strip().split()))
    dl=list(map(str,input().strip().split()))
    like.append(ll)
    dislike.append(dl)
    for i in range(1,int(ll[0])+1):
        if ll[i] in d:
            d[ll[i]]+=1.21
        else:
            d[ll[i]]=1
    for i in range(1,int(dl[0])+1):
        if dl[i] in d:
            d[dl[i]]-=1.2
        else:
            d[dl[i]]=-1
ingredients=[];nl=[]
for i in d:
    if d[i]>=0:
        ingredients.append(i)
    else:
        nl.append(i)



ans=score(like,dislike,ingredients)
t=3
count=0
k2=ans
while t>0:

    replace=random.randint(0,test-1)
##    while not bit[replace]:
##        replace=random.randint(0,number-1)

    for notlike in dislike[replace][1:]:
        if notlike in ingredients:
            ingredients.remove(notlike)
    for likeval in like[replace][1:]:
        if likeval in ingredients:
            pass
        else:
            ingredients.append(likeval)
##    bit[replace]=1
##    woah=random.randint(0,len(ingredients)-1)
##    notwoah=random.randint(0,len(nl)-1)
##    cus=random.randint(0,1)
##    if cus:
##        del ingredients[woah]
##    else:
##        ingredients.append(notwoah)

    k=score(like,dislike,ingredients)
    delta=k-ans
    #print("delta",delta)
    if delta>0:
        ans=k
        print(k,t)
    elif ((math.e)**(delta/t))>random.random():
        ans=k
        print(k,t)

    count+=1
    if count==10:
        t-=1
        count=0

    if k>k2:
        print("woooow")
        k2=k
        lis=ingredients.copy()
##for maka in lis:
##    if maka in like_giant:
##        pass
##    else:
##        print("WTF")
##        break
print("-----------------------------")
print(score(like,dislike,lis))
with open('outputd.txt','w+') as ofp:
    ofp.write(str(len(lis))+" "+" ".join([str(listval) for listval in lis]))
ofp.close()

#lis=ingredients.copy()
#print(len(lis)," ".join([str(listval) for listval in lis]))
