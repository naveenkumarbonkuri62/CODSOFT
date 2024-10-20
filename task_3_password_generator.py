import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected!")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? : ").lower() == 'y'
    use_digits = input("Include digits? : ").lower() == 'y'
    use_special = input("Include special characters? : ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
