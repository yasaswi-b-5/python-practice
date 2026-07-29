#1.Write a Python program to repeatedly subtract 3 from a number until the result becomes less than 0?
#Input:14
#Output:14 11 8 5 2
'''i=1
num=int(input('enter the num:,'))
while True:
 if num<0:
     
      break   
       
 print(num,end=" ")
 num=num-3 '''
    
#2.Write a Python program to repeatedly double a number until it exceeds 100?

#Input:3

#Output:3 6 12 24 48 96

#Explanation:
#Terminate the loop when the next value becomes greater than 100.
'''i=100
num=int(input('enter the num:,'))
while True:
 if num>100:
     
      break   
       
 print(num,end=" ")
 num=num*2'''
#3.Write a Python program to count how many times a number can be divided by 2 before it becomes odd?

#Input:40
#Output:3

#Explanation:
#40 → 20 → 10 → 5
#The number was divided by 2 three times.
num=int(input('enter the num:',))
while True:
    while num%2==0:
        print(num)
        if num%2!=0:
           break
        
num=num-1    
        
        
        

 
