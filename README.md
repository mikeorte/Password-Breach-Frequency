# Password Pwned Checker

This project checks if a given password has been pwned using the [Have I Been Pwned](https://haveibeenpwned.com) API. It provides secure password input, validation, and user-friendly interaction through a graphical user interface (GUI) built with Tkinter.

## Features

- **Secure Password Input**: Uses hidden input for passwords.
- **Password Validation**: Ensures the password is not empty.
- **User-Friendly Interaction**: Provides clear prompts and feedback through a GUI.
- **API Integration**: Connects to the Have I Been Pwned API to check if the password has been compromised.

## Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/mikeorte/Password-Breach-Frequency.git
   cd password-pwned-checker
   \`\`\`

2. **Create a virtual environment (optional but recommended)**:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate # On Windows use \`venv\Scripts\activate\`
   \`\`\`

3. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage

Run the script using Python:

\`\`\`bash
python check_password_gui.py
\`\`\`

The script will launch a graphical user interface where you can securely enter a password and check if it has been pwned.

### Example

![GUI Example](/Password-Breach-Frequency.png)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Have I Been Pwned](https://haveibeenpwned.com)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
