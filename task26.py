'''1)Create a variable: name = "Python"
Print: • The first character • The last character • The length of the string'''
name = "Python"
print(name[0])
print(name[-1])
print(len(name))




'''2)Take the user's first name and last name separately, then combine them into a single string with a space between them.'''
first_name=input("enter the text:",)
last_name=input("enter the text:",)
print(first_name+' '+last_name)



'''3)You are given a list of student records: students = [ ("Rahul", 85, "Python"), ("Priya", 92, "Python"), ("Arun", 78, "Java"),
("Sneha", 92, "Python"), ("Kiran", 65, "Java"), ("Priya", 88, "Java") ] Using lists, tuples, sets, and didictionaries, write a Python program that:
1.Creates a set containing all unique course names. 
2.Creates a dictionary where each course is a key and the value is a list of student names enrolled in that course. 
3.Finds the highest score in each course. 
4.Creates a set of students who scored 90 or above. 
5.Prints the final dictionary, unique courses, highest score for each course, and the students who scored 90+'''
students = [ ("Rahul", 85, "Python"), ("Priya", 92, "Python"), ("Arun", 78, "Java"),
("Sneha", 92, "Python"), ("Kiran", 65, "Java"), ("Priya", 88, "Java") ]
sets=set()
course_list={}
score_list={}
sc_90=set()
for i in students:
    j=i[2]
    if j  not in sets:
       sets.add(j)
print(sets)       
for name,score,course in students:
    if course not in course_list:
        course_list[course]=[]
    course_list[course].append(name)
print(course_list)
for name,score,course in students:
    if course not in score_list:
        score_list[course]=[]
    score_list[course].append(score)
for course,score in score_list.items():     
  print(course,max(score))
for name,score,course in students:
    if score >90:
        sc_90.add(name)
print(sc_90)        
        
  
