import os

# Define colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def clear_screen():
    os.system('clear')

def display_logo():
    logo = f"""
    {Colors.OKCYAN}
         _____        _              _     _       
        / ____|      | |            | |   | |      
       | |     __ _ | |_  __ _  ___| |__ | |_ ___ 
       | |    / _` || __|/ _` |/ __| '_ \| __/ _ \\
       | |___| (_| || |_| (_| | (__| | | | ||  __/
        \_____\__,_| \__|\__,_|\___|_| |_|\__\___|

              C16
     {Colors.OKGREEN}by Tebogo Moraba{Colors.ENDC}
    {Colors.ENDC}
    """
    print(logo)

class Encryptor:
    def __init__(self):
        # Mappings for letters to numbers
        self.letter_to_number = {chr(i): i - 64 for i in range(65, 91)}  # A-Z -> 1-26
        # Reverse mapping for numbers to symbols
        self.number_to_symbol = {
            1: " ° ", 2: " °_", 3: " °°_", 4: " °_° ", 5: " °`", 6: " ' ",
            7: " ' ° ", 8: " ' °° ", 9: " ' ° _", 10: " ' °_° ", 11: " `' ",
            12: " `'_ ", 13: "  `° ", 14: " `¬", 15: " `|", 16: " |` ",
            17: " |`' ", 18: " |° ", 19: " |_° ", 20: " ~° ",
            21: " ~`", 22: " '~ ", 23: " ¬° ", 24: "~¬ ",
            25: " ~| ", 26: " ¬| ", "¡": " "  # Space representation
        }

    def encrypt(self, input_text):
        encrypted_text = ""
        for char in input_text.upper():
            if char in self.letter_to_number:
                number = self.letter_to_number[char]
                encrypted_text += self.number_to_symbol[number] + "®"
            elif char == ' ':
                encrypted_text += "¡®"  # Use ¡ for spaces
            else:
                encrypted_text += "?"  # For unrecognized characters

        return encrypted_text.strip()

    def decrypt(self, encrypted_text):
        decrypted_text = ""
        encrypted_parts = encrypted_text.split("®")  # Split by the separator

        for part in encrypted_parts:
            symbol = part.strip()
            if symbol:  # Check if the symbol is not empty
                found = False
                for number, symbol_value in self.number_to_symbol.items():
                    if symbol_value.strip() == symbol:
                        decrypted_text += chr(number + 64)  # Convert number back to letter A-Z
                        found = True
                        break
                if not found:
                    decrypted_text += "?"  # For unrecognized symbols
            else:
                decrypted_text += " "  # Preserve empty parts as spaces

        decrypted_text = decrypted_text.replace("¡", " ").strip()  # Replace "¡" back to space
        decrypted_text = decrypted_text.replace("?", " ")  # Final checkpoint for "?"

        return decrypted_text

def encryption_mode(encryptor):
    while True:
        text = input("Enter text to encrypt (or type 'back' to return to the main menu): ")
        if text.lower() == 'back':
            break
        encrypted = encryptor.encrypt(text)
        print("Original:", text)
        print("Encrypted:", encrypted)

def decryption_mode(encryptor):
    while True:
        text = input("Enter text to decrypt (or type 'back' to return to the main menu): ")
        if text.lower() == 'back':
            break
        decrypted = encryptor.decrypt(text)
        print("Encrypted:", text)
        print("Decrypted:", decrypted)

def main_menu():
    clear_screen()
    display_logo()
    print(f"{Colors.OKBLUE}Welcome to CueCircle C16!{Colors.ENDC}\n")
    print("Select an option:")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice

def run_program():
    encryptor = Encryptor()
    while True:
        choice = main_menu()

        if choice == '1':
            clear_screen()
            display_logo()
            print(f"{Colors.OKBLUE}Encryption mode selected.{Colors.ENDC}")
            encryption_mode(encryptor)
        elif choice == '2':
            clear_screen()
            display_logo()
            print(f"{Colors.OKBLUE}Decryption mode selected.{Colors.ENDC}")
            decryption_mode(encryptor)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print(f"{Colors.FAIL}Invalid option. Please try again.{Colors.ENDC}")

if __name__ == "__main__":
    run_program()
