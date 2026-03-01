user={'username':'user123','password':'****'}

uid=input("Enter username: ")

if uid==user['username']:
    if input("Enter password: ")==user['password']:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Username not found")