print("====================================")
print("     PASSWORD STRENGTH CHECKER      ")
print("====================================")

# 1. Ask the user for their password
password = input("Enter a password to test: ")

# 2. Setup our scoring variables
score = 0
has_upper = False
has_lower = False
has_number = False
has_symbol = False

# 3. Check the LENGTH of the password
if len(password) >= 12:
    score = score + 2
elif len(password) >= 8:
    score = score + 1

# 4. Look at EACH CHARACTER in the password one by one
for character in password:
    if character.isupper():        # Checks for A-Z
        has_upper = True
    elif character.islower():      # Checks for a-z
        has_lower = False          # Fix: should be True
        has_lower = True
    elif character.isdigit():      # Checks for 0-9
        has_number = True
    else:                          # If it's none of the above, it's a symbol (!, @, #, etc.)
        has_symbol = True

# 5. Add points for variety
if has_upper:
    score = score + 1
if has_lower:
    score = score + 1
if has_number:
    score = score + 1
if has_symbol:
    score = score + 1

# 6. Show the final result and tips
print("\n--- RESULTS ---")

if score >= 5:
    print("Strength: STRONG 💪")
    print("Great job! Your password is highly secure.")
elif score >= 3:
    print("Strength: MODERATE ⚠️")
    print("Tips to improve:")
    if len(password) < 12:   print("- Make it longer (12+ characters is best).")
    if not has_upper:        print("- Add a CAPITAL letter.")
    if not has_number:       print("- Add a number.")
    if not has_symbol:       print("- Add a symbol (like ! or @).")
else:
    print("Strength: WEAK ❌")
    print("Warning: This password is easy to crack! Please make it longer and mix in numbers/symbols.")

print("====================================")