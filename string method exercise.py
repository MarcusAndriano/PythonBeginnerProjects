# Quick exercise for string methoding
user_name = input("Enter a username: ")

if len(user_name) > 12:
    print("The username is too long")
elif not user_name.find(" ") == -1:
    print("Your username can't contain spaces")
elif not user_name.isalpha():
    print("Your username can't contain numbers")
else:
    print(f" Welcome {user_name}")

