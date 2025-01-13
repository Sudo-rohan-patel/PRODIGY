def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    
    for char in plain_text:
        # Check if the character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, just add it as it is (punctuation, spaces, etc.)
            encrypted_text += char
    
    return encrypted_text


def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        # Check if the character is an uppercase letter
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # If it's not a letter, just add it as it is (punctuation, spaces, etc.)
            decrypted_text += char
    
    return decrypted_text


def print_welcome_banner():
    print("""
    ##############################################
    #                                            #
    #      Welcome to the Caesar Cipher Tool!     #
    #                                            #
    ##############################################
    """)
    
    print("""
    ************************************************
    *                                              *
    *               Caesar Cipher                  *
    *                                              *
    ************************************************
    """)


def main():
    # Display the welcome banner with some special symbolic design
    print_welcome_banner()

    # Ask the user for input
    operation = input("Would you like to Encrypt or Decrypt? (E/D): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (an integer): "))
    
    if operation == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"\nEncrypted Message: {encrypted_message}")
    elif operation == 'd':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"\nDecrypted Message: {decrypted_message}")
    else:
        print("\nInvalid operation! Please enter 'E' for encryption or 'D' for decryption.")

    # Display the creator's name with an extra line of design
    print("""
    ************************************************
    *      Thank you for using the Caesar Cipher!   *
    *      Created by: Rohan Patel                 *
    ************************************************
    """)


# Run the program
if __name__ == "__main__":
    main()
