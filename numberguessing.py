import random

def main():
    print("--- Number Guessing Game ---")
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("I have generated a random number between 1 and 100.")
    print(f"Can you guess what it is? You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break
                
            if attempts == max_attempts:
                print(f"Game over! You've used all {max_attempts} attempts. The number was {target_number}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
