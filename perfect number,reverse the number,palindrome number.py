#perfect number
num=int(input('enter the num:',))
div=1
sum=0
while div<=num//2:
    if num%div==0:
        sum=sum+div
    div=div+1

if sum==num:
    print('perfect')
else:
    print('not perfect')
#reverse the number
num=int(input('enter the number:',))
rev=0
while num>0:
    d=num%10
    rev=rev*10+d 
    num=num//10
print(rev) 
#palindrome number
num=int(input('enter the number:',))
rev=0
org=num
while num>0:
    d=num%10
    rev=rev*10+d 
    num=num//10
if rev==org:
   print('palindrome')
else:
   print('not a palndrome')
