# Function to log keystrokes
def log_keystrokes():
    # Display a welcome message with symbolic design
    print("""
    ##################################################
    #                                                #
    #   Welcome to the Keyboard Input Logger Tool    #
    #    (This tool logs characters you type.)       #
    #                                                #
    ##################################################
    """)
    print("""
    ****************************************************
    *                                                  *
    *    Keyboard Input Logger - Created by Rohan      *
    *    Patel (for educational purposes)             *
    *    Press 'Ctrl + C' to stop the program.         *
    *                                                  *
    ****************************************************
    """)

    # Get user input for the log file name
    log_file_name = input("Enter the file name to save the log (e.g., 'key_log.txt'): ")

    # Open the log file for writing
    with open(log_file_name, "a") as log_file:
        print("\nStart typing below (everything will be logged to the file)...")
        print("Press 'Ctrl + C' to stop.\n")
        
        # Logging loop
        try:
            while True:
                # Capture each key press from the user
                char = input()
                
                # Log the keystroke to the file
                log_file.write(char + '\n')
                log_file.flush()  # Ensure that the log file is updated immediately

                # Display feedback in real-time
                print(f"Logged: {char}")
        except KeyboardInterrupt:
            print("\nLogging stopped. Exiting the program...")

# Run the logging session
if __name__ == "__main__":
    log_keystrokes()
