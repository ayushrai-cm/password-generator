import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=" * 45)
    print("      🔐 SECURE PASSWORD GENERATOR")
    print("         Made by Arindam Pal")
    print("=" * 45)

    while True:
        try:
            length = int(input("\nEnter password length (4 - 64): "))
            if length < 4 or length > 64:
                print("❌ Please enter a length between 4 and 64.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    print("\nSelect character types to include:")
    use_upper   = input("  Include UPPERCASE letters? (y/n): ").strip().lower() == 'y'
    use_digits  = input("  Include DIGITS (0-9)?        (y/n): ").strip().lower() == 'y'
    use_symbols = input("  Include SYMBOLS (!@#$)?      (y/n): ").strip().lower() == 'y'

    print("\n" + "-" * 45)
    print("  ✅ Generated Passwords:")
    print("-" * 45)
    for i in range(5):
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"  {i+1}. {pwd}")
    print("-" * 45)

    while True:
        again = input("\nGenerate more passwords? (y/n): ").strip().lower()
        if again == 'y':
            print("\n" + "-" * 45)
            print("  ✅ New Passwords:")
            print("-" * 45)
            for i in range(5):
                pwd = generate_password(length, use_upper, use_digits, use_symbols)
                print(f"  {i+1}. {pwd}")
            print("-" * 45)
        else:
            print("\n👋 Thank you for using Password Generator!")
            print("   Made by Arindam Pal | Chitkara University")
            break

if __name__ == "__main__":
    main()