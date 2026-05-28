email_text = input("Paste the email content here: ")
email_text = email_text.lower()

risk_score = 0
warnings = ""

if "urgent" in email_text or "suspended" in email_text or "24 hours" in email_text:
    risk_score = risk_score + 30
    warnings = warnings + " - Threat or urgency detected\n"

if "password" in email_text or "verify" in email_text or "bank" in email_text:
    risk_score = risk_score + 30
    warnings = warnings + " - Asks for sensitive data/login\n"

if "http" in email_text or "www." in email_text:
    risk_score = risk_score + 40
    warnings = warnings + " - Contains a web link\n"

print("\n--- ANALYZING EMAIL ---")

if risk_score >= 60:
    print("VERDICT: 🔴 HIGH RISK (Likely a scam)")
elif risk_score >= 30:
    print("VERDICT: 🟡 MEDIUM RISK (Be careful)")
else:
    print("VERDICT: 🟢 LOW RISK (Looks okay)")

print("Total Risk Score:", risk_score, "/ 100")
print("Reasons Found:")
print(warnings)