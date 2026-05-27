secret_message = input("Type your secret message: ")
password_lock = input("Create a password to lock it: ")

protected_text = ""
for letter in secret_message:
    protected_text = protected_text + chr(ord(letter) + 2)

print("\n🔒 Data Protected!")
print("Scrambled text looks like this: " + protected_text)
print("--------------------------------------------------\n")

user_guess = input("Enter the password to restore the message: ")

if user_guess == password_lock:
    restored_text = ""
    for letter in protected_text:
        restored_text = restored_text + chr(ord(letter) - 2)
    
    print("✅ ACCESS GRANTED!")
    print("Restored Message: " + restored_text)
else:
    print("❌ ACCESS DENIED!")
    print("The text stays scrambled: " + protected_text)