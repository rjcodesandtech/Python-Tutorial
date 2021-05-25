#Python code for control operations (if elif else), created by rjcodesandtech
#if statements
a = 1
b = 0
if a == 1 and b == 0: #since the value of a is set to 1 and b is set to 0, therefore the statement a == 1 and b == 0 is True and it will print out "a is 1 and b is 0"
    print("a is 1 and b is 0")
#now let us change the values
a = 2
b = 1
if a == 1 and b == 0: #since the value of a is set to 2 and b is set to 1, therefore the statement a == 1 and b == 0 is False and it will skip the print statement under its codeblocks
    print("a is 1 and b is 0")
elif a == 2 and b == 1: #since the value of a is set to 2 and b is set to 1, therefore the statement a == 2 and b == 1 is True and it will print out "a is 2 and b is 1"
    print("a is 2 and b is 1")
#again let us change values
a = 5
b = 3
if a == 1 and b == 0: #since the value of a is set to 5 and b is set to 3, therefore the statement a == 1 and b == 0 is False and it will skip the print statement under its codeblocks
    print("a is 1 and b is 0")
elif a == 2 and b == 1: #since the value of a is set to 5 and b is set to 3, therefore the statement a == 2 and b == 1 is False and it will skip the print statement under its codeblocks
    print("a is 2 and b is 1")
else: #if none of the above condition was True, the program will consider else and do the statement underneath it.
    print("none of the combinations was correct")
