student = {'name': 'John', 'age': '25','courses': ['Maths','CompSci']}

print(student['age'])
print(student.get('phone','Not Found')) # prints pre-defined msg on error
# print(student['phone'])  # prints an KeyError message
student.update({'name': 'Jane', 'age': '26','phone': '555-5555'})
print(student)


print(student.keys())       # prints the keys only
print(student.values())     # prints the values only
print(student.items())      # prints both the keys and the values
