import random
import string

#TESTING LINE. THIS SHOULD BE BLATANTLY VISIBLE! hello. NEW TEST JAN 23

# Function to get and validate user input
def get_user_input(prompt, min_value, max_value):
    # Boolean for checking if input is an integer
    input_valid = False

    # Variable for the output of the chosen input prompt
    output = 0

    # Integer identification; loops every time invalid input is entered
    while not input_valid:
        # If output is valid as int, run rest of input loop.
        try:
            output = int(input(f"{prompt}: "))

            # Conditions regarding if min/max value parameters are not met properly
            if max_value < output:
                print(f"You've exceeded the character limit. Please try again within {min_value} and {max_value}.")
            elif output < min_value:
                print(f"The entered number is too low. Please try again within {min_value} and {max_value}.")

            else:
                input_valid = True
        # Catches error for if user does not enter number
        except ValueError:
            print("Value Error: Please enter a number.\n")

    return output

# Function to generate a password
def generate_password(length, num_letters, num_digits, num_specials):
    # String variable for the password
    password = ""
    # Set of letters to be randomly added to the password
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Range of numbers (0 to 9) will be set within its own loop.

    # Set of special characters to be randomly added to the password
    special_characters = "#$%&'\"()*+,-./:;<=>?@[]^_`{|}~"

    #
    for i in range(num_letters):
        random_letter = random.choice(letters)
        password += random_letter

    for i in range(num_digits):
        password += str(random.randint(0, 9))

    for i in range(num_specials):
        random_special = random.choice(special_characters)
        password += random_special

    # Turns unshuffled password into a list to shuffle
    # Turns it back to a string afterwards
    unshuffled_password = list(password)
    random.shuffle(unshuffled_password)
    result = ''.join(unshuffled_password)
    password = result

    # Displays the generated password
    print(f"Your Password: {password}")

# Main function
def main():

    print("\n--- Secure Password Generator ---\n")
    # Validates if password length matches sum of all requested character counts
    password_length_equals_character_sum = False

    # In order: Password length, number of letters, number of digits
    # and number of special characters in password
    length = 0
    num_letters = 0
    num_digits = 0
    num_specials = 0

    # While condition running until character sum matches password length
    while not password_length_equals_character_sum:
        # In order: Password length, number of letters, number of digits
        # and number of special characters in password
        length = get_user_input("Enter the total length of the password", 8, 16)
        num_letters = get_user_input(f"Enter the number of letters desired in the password ({length} characters remaining)", 0, length)
        num_digits = get_user_input(f"Enter the number of numbers desired in the password ({length - num_letters} characters remaining)", 0, length - num_letters)
        num_specials = get_user_input(f"Enter the number of special characters desired in the password ({length - num_letters - num_digits} characters remaining)", 0, length - num_letters - num_digits)

        # Step 2: Validate user inputs
        # Condition regarding if user-requested password length
        # matches sum of requested character counts
        if length != (num_letters + num_digits + num_specials):
            print("The sum of letters, digits and special characters exceeds or precedes the requested length .\nPlease try again.\n")
        else:
            password_length_equals_character_sum = True


    # Step 3: Generate the password

    generate_password(length, num_letters, num_digits, num_specials)

    # Step 4: Display the generated password

    # Step 5: Save password to file

# Entry point of the script
if __name__ == "__main__":
    main()