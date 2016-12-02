# 7. Write a Python program to accept a filename from the user print the extension of that.

file_name = input("Enter a filename: ")
f_extns = file_name.split(".")
print("The filename extention is: " + repr(f_extns[-1]))
