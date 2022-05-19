# to escape the character ('), we can use a backslash right before it
message2 = 'Yash\'s world!'

# to find the length of our message
print(len(message))

# prints the index of a message
print(message[10])

# prints the interval of the starting and ending indices
print(message[0:5]) # all the way upto bt not including 5th index
print(message[:5]) # frm beginning
print(message[6:]) # to end 

# lower and uppercase
print(message.lower())
print(message.upper())

# to count
print(message.count("Hello")) # no. of hello
print(message.count("l")) # no. of l

# to find
print(message.find("World")) # prints the actual index
print(message.find("Universe")) # prints -1

# to replace
new_message = print(message.replace("World","Universe"))
print(new_message)
  
# concatenate

greeting = "Hello"
name = "Michael"

# message = greeting + ", " + name + ". Welcome!"
# message = '{}, {}. Welcome!'.format(greeting,name)
message = f'{greeting}, {name}. Welcome!'

print(message)

# to see all the attributes available
print(dir(name))