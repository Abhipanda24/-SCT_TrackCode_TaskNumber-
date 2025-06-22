import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length criteria
    length = len(password)
    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g. !, @, #).")

    # Determine strength level
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    print("=== Password Strength Checker ===")
    pwd = input("Enter password to check: ")

    strength, tips = check_password_strength(pwd)
    print(f"\nPassword strength: {strength}")

    if tips:
        print("Suggestions to improve your password:")
        for tip in tips:
            print(f"- {tip}")

if _name_ == "_main_":
    main()