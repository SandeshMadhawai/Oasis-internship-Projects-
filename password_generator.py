import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "❌ No character set selected."

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print(" Random Password Generator")

    length = int(input("Enter password length: "))

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    print("\nGenerated Password:")
    print(password)

main()
