import hashlib
import requests
import getpass

def is_password_pwned(password):
    """Check if the given password has been pwned using the HIBP API."""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            lines = response.text.splitlines()

        hash_dict = {}
        for line in lines:
            hash_suffix, count = line.split(':')
            hash_dict[hash_suffix] = int(count)

        return hash_dict.get(suffix, 0)

    except requests.RequestException as e:
        print(f"An error occurred while connecting to the HIBP API: {e}")
        return -1

def get_password_from_user():
    """Prompt the user to enter a password securely."""
    while True:
        password = getpass.getpass("Enter password: ")
        if password:
            return password
        else:
            print("Password cannot be empty. Please try again.")

def main():
    while True:
        password = get_password_from_user()

        pwned_count = is_password_pwned(password)

        if pwned_count == -1:
            print("An error occurred during the check.")
        elif pwned_count > 0:
            print(f"Your password hash has appeared {pwned_count:,} times in known data breaches.")
        else:
            print("Your password hash has not appeared in a known data breach.")

        run_again = input("Do you want to check another password? (yes/no): ").strip().lower()
        if run_again != 'yes':
            print("Exiting the program. Stay safe!")
            break

if __name__ == "__main__":
    main()