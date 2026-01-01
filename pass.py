import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("--- Random Password Generator ---")
    
    while True:
        try:
            user_input = input("Enter password length (or type 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                print("Exiting program.")
                break
            
            length = int(user_input)
            
            if length < 6:
                print("Password too short! Recommended length is at least 6.")
                continue

            new_password = generate_password(length)
            print(f"Your Password: {new_password}")
            print("-" * 30)
            
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()