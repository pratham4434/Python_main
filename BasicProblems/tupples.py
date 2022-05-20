courses = ["History", "Math", "Physics", "CompSci"]
courses_2 = ["Art", "Education"]

print(courses)
print(len(courses))     # length of the array
print(courses[0])       # first item
print(courses[-1])      # starts frm the end of the list
print(courses[0 : 2])   # all the way upto bt not including the last one


courses.append('Art')
print(courses)          # inserts an item at the last

courses.insert(0,'English') # inserts at the exact place
print(courses)

courses.insert(0, courses_2) # inserts the whole array
print(courses)

courses.extend(courses_2) # inserts the contents of the whole array
print(courses)

courses.remove()   # removes the exact item
courses.pop()      # removes the last item
courses.reverse()  # reverses the array
courses.sort()     # sorts in either ascending order or alphabetical order