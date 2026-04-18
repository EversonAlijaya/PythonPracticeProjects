#validate username input
#instagram username requirements:
#nomore than 20 characters
#at least 6 characters
#only letters, numbers, underscores, and periods allowed
#no spaces allowed
#must be in lowercase

username = input("Enter your username: ").strip()
if len(username) < 6:
    print("Username must be at least 6 characters long.")
elif len(username) > 20:
    print("Username must be less than 20 characters long.")
elif not username.replace("_", "").replace(".", "").isalnum():
    print("Username must contain only letters, numbers, underscores, and periods.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif not username.lower() == username:
    print("Username must be in lowercase.")
else:
    print(f"welcome {username}!")

