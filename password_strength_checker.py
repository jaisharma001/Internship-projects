print("====================================")
print("     PASSWORD STRENGTH CHECKER      ")
print("====================================")

password = input("Enter a password to test: ")

score = 0
has_upper = False
has_lower = False
has_number = False
has_symbol = False

if len(password) >= 12:
    score = score + 2
elif len(password) >= 8:
    score = score + 1

for character in password:
    if character.isupper():        
        has_upper = True
    elif character.islower():      
        has_lower = False          
        has_lower = True
    elif character.isdigit():      
        has_number = True
    else:                          
        has_symbol = True

if has_upper:
    score = score + 1
if has_lower:
    score = score + 1
if has_number:
    score = score + 1
if has_symbol:
    score = score + 1

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