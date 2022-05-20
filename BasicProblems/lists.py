courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]

print(courses)
print(len(courses))     # length of the array
print(courses[0])       # first item of the array
print(courses[-1])      # starts frm the end of the list
print(courses[0 : 2])   # all the way upto bt not including the last one


courses.append('Art')
print(courses)                      # inserts an item at the last

courses.insert(0,'English')         # inserts at the exact place
print(courses)

courses.insert(0, courses_2)        # inserts the whole array
print(courses)

courses.extend(courses_2)           # inserts the contents of the whole array
print(courses)

# courses.remove()   # removes the exact item
# courses.pop()      # removes the last item
# courses.reverse()  # reverses the array
# courses.sort()     # sorts in either ascending order or alphabetical order

sorted_courses = sorted(courses)  # makes a separate copy and do not alters with the actual list
print(sorted_courses)

for course in courses:  # prints each of the items 
    print (course) 

for index, course in enumerate (courses, start = 1):  # prints the value along with their item no. in the list 
    print(index, course)

courses = ["History", "Math", "Physics", "CompSci"]
course_str = ' _ '.join(courses)
print(course_str)

new_list = course_str.split(" _ ")
