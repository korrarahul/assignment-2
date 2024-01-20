def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(full_name):
    return full_name[::2]


first_name = input("Enter first name: ")
last_name = input("Enter  last name: ")
full_name = fullname(first_name, last_name)

result = string_alternative(input("enter string : "))

print("Full Name :{}".format(full_name))
print("Output :{}".format(result))