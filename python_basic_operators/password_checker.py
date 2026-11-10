def password_checker():
    attempts = 0
    while attempts < 3:
        password = input("Enter your password: ")
        if password == "abc123" and len(password) >= 6:
            print("Access granted.")
            return True
        elif password != "abc123" and len(password) < 6:
            print(f"Incorrect password. Password must be at least 6 characters long. You have {3 - attempts} attempts left.")    
        else:
            print(f"Incorrect password. You have {3 - attempts} attempts left.")
        attempts += 1
    else:
        print("Access denied. You have exceeded the maximum number of attempts.")
        return False
password_checker()