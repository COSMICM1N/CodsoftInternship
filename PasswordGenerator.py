import random
import string

def generate_password(length=8):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    complexity = input("Select complexity level (low, medium, high): ")
    if complexity.lower() == "low":
        characters = lowercase_letters + digits
    elif complexity.lower() == "medium":
        characters = lowercase_letters + uppercase_letters + digits
    elif complexity.lower() == "high":
        characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        print("Invalid complexity level. Using low complexity by default.")
        characters = lowercase_letters + digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()