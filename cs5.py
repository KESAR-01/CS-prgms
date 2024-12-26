import re

def k_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    complexity_criteria = (bool(re.search(r"[a-z]", password)) and 
                           bool(re.search(r"[A-Z]", password)) and
                           bool(re.search(r"\d", password)) and
                           bool(re.search(r"[!@#$%^&*(),.?\":{}[<>]", password)))
    randomness_criteria = len(set(password)) >= len(password) * 0.8  # 80% unique characters

    # Check overall strength
    if length_criteria and complexity_criteria and randomness_criteria:
        return "Strong"
    else:
        return "Weak"

def suggest_improvements(password):
    suggestions = []

    # Length suggestion
    if len(password) < 8:
        suggestions.append("Add more characters to meet the minimum length requirement.")
    
    if not re.search(r"[a-z]", password):
        suggestions.append("Include lowercase letters.")
    
    if not re.search(r"[A-Z]", password):
        suggestions.append("Include uppercase letters.")
    
    if not re.search(r"\d", password):
        suggestions.append("Include digits.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}[<>]", password):
        suggestions.append("Include special characters.")

    # Randomness suggestion
    if len(set(password)) < len(password) * 0.8:
        suggestions.append("Increase the variety of characters for better randomness.")

    return suggestions

def main():
    # Get user input for password
    password = input("Enter your password: ")

    # Check password strength
    strength = k_password_strength(password)
    print(f"Password Strength: {strength}")

    if strength == "Weak":
        improvements = suggest_improvements(password)
        print("Suggestions for improvement:")
        for suggestion in improvements:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
