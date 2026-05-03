import secrets
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    # Always include at least one lowercase
    password.append(secrets.choice(string.ascii_lowercase))

    # Fill remaining length
    remaining = length - len(password)
    password.extend(secrets.choice(characters) for _ in range(remaining))

    # Shuffle password
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def get_valid_length():
    while True:
        try:
            length = int(input("\nEnter password length (4 - 64): "))
            if 4 <= length <= 64:
                return length
            print("❌ Enter a number between 4 and 64.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")


def ask_option(message):
    return input(message).strip().lower() == 'y'


def main():
    print("=" * 45)
    print("        🔐 SECURE PASSWORD GENERATOR")
    print("             Made by Ayush Rai")
    print("=" * 45)

    while True:
        length = get_valid_length()

        print("\nSelect character types:")
        use_upper = ask_option(" Include UPPERCASE? (y/n): ")
        use_digits = ask_option(" Include DIGITS? (y/n): ")
        use_symbols = ask_option(" Include SYMBOLS? (y/n): ")

        print("\n" + "-" * 45)
        print(" ✅ Generated Passwords:")
        print("-" * 45)

        for i in range(5):
            print(f" {i+1}. {generate_password(length, use_upper, use_digits, use_symbols)}")

        print("-" * 45)

        again = input("\nGenerate again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for using Password Generator!")
            break


if __name__ == "__main__":
    main()
