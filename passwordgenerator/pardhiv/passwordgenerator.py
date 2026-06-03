import random
import string

print("=== Secure Password Generator ===")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

password = [
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]

remaining = length - 4

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password.extend(random.choice(characters) for _ in range(remaining))

random.shuffle(password)

print("\nGenerated Password:")
print(''.join(password))
