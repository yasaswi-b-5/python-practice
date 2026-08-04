#find the y value in two sum division
'''import time
x=[i for i in range(1,10000000)]
start=time.time ()  
y=9999999
s=0
e=len(x)-1
while True:
   m=(s+e)//2
   if s>e:
       print("not found")
       break
   elif x[m]==y:
    print("found")
    break
   elif y<x[m]:
    e=m-1
   elif y>x[m]:
    s=m+1

end=time.time()
print("time taken =",end-start)'''



#stack example
'''

import time

brackets=input("enter the string:",)
pairs={'{':'}','[':']','(':')'}
stack=[]
start=time.time()
if brackets[0] in ")]}":
    print("invaild parathesis")
else:
    for i in brackets:
        if i in "{[(":
            stack.append(i)
        else:
            if len(stack)==0:
                print("invalid parathesis")
                break
            close_tag=pairs.get(stack.pop())
            if close_tag!=i:
                print("invalid parathesis")
                break
    else: 
             if len(stack)>0:
               print("invalid parathesis")
             else:    
        
              print("valid parathesis")         


end=time.time()
print("time:",end-start)'''






#sumof two values in list is 8
'''x=[1,2,3,4,5,6,7,8,9]
target=8
seen=set()
for i in x:
    diff=target-i
    if diff in seen:
        print((diff,i))
    else:
        seen.add(i)'''

#sliding window
x=[1,9,4,3,4,5,7,-1,4]
k=3
max_sum=sum(x[:k])#sum of x[0] to x[k]->x[0] to x[3]
current_sum=sum(x[:k])
for i in range(k,len(x)):
    current_sum=current_sum-x[i-k]+x[i]
    if current_sum>max_sum:
        max_sum=current_sum
    obj=x[i-k+1:i+1]    
print("maximum=",max_sum)
print(obj)


'''1,9,4,=14
9,4,3====16
4,3,4,=11
3,4,5,=12
4,5,7,=16
5,7,-1,=11
7,-1,4=10'''











































































