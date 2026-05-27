correct_password = "secure123"
failed_attempts = 0
max_attempts = 3

while failed_attempts < max_attempts:
    user_guess = input("Enter your password: ")
    
    if user_guess == correct_password:
        print("✅ ACCESS GRANTED! Welcome to the system.")
        break
    else:
        failed_attempts = failed_attempts + 1
        remaining = max_attempts - failed_attempts
        print("❌ Incorrect password.")
        if remaining > 0:
            print("Attempts remaining: " + str(remaining))
            print("-----------------------------------")

if failed_attempts == max_attempts:
    print("\n🚨 ACCESS DENIED! You have been locked out due to too many failed attempts.")