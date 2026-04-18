#validate username input
#instagram username requirements:
#nomore than 20 characters
#at least 6 characters
#only letters, numbers, underscores, and periods allowed
#no spaces allowed
#must be in lowercase

import re
username = input("Enter your username: ").strip()
if not (6 <= len(username) <= 20):
    print("Username must be between 6 and 20 characters long.")
elif not re.fullmatch(r'[a-z0-9_.]+', username):
    print("Username must contain only letters, numbers, underscores, and periods.")
elif not username.lower() == username:
    print("Username must be in lowercase.")
else:
    print(f"welcome {username}!")