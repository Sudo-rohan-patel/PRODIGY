import re

# Function to check password complexity
def check_password_strength(password):
    # Length check (password should be at least 8 characters)
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Check for the presence of both uppercase and lowercase letters
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    
    # Check for the presence of digits
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number."
    
    # Check for the presence of special characters
    if not re.search(r'[@$!%*?&]', password):
        return False, "Password must contain at least one special character (e.g., @, $, !, %)."
    
    return True, "Password is strong!"

# Function to print a welcome banner with special symbolic design
def print_welcome_banner():
    print("""
    ##################################################
    #                                                #
    #   Welcome to the Password Complexity Checker   #
    #                                                #
    ##################################################
    """)

    print("""
    ****************************************************
    *                                                  *
    *    Password Strength Checker - Created by Rohan  *
    *                                                  *
    ****************************************************
    """)

def main():
    # Display the welcome banner with design
    print_welcome_banner()

    # Ask the user to enter their password
    password = input("Enter your password to check its strength: ")

    # Check the password strength
    is_strong, message = check_password_strength(password)
    
    # Display feedback based on password strength
    if is_strong:
        print("\n🎉 Your password is strong! 🎉")
    else:
        print(f"\n⚠️ Weak Password! {message} ⚠️")

    # Display the creator's name
    print("\n****************************************************")
    print("*      Thank you for using the Password Checker!   *")
    print("*      Created by: Rohan Patel                    *")
    print("****************************************************")

# Run the program
if __name__ == "__main__":
    main()
