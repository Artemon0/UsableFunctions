"""Console games, greetings, and keyboard input."""

import random


def quest(player: str = "Unnamed", difficulty: int = 1) -> str:
    """
    Run a math quiz game with different difficulty levels.

    Args:
        player: Player name
        difficulty: Difficulty level (1-3)

    Returns:
        Final score message
    """
    score = 0
    print(f"{player}, welcome to the quest!")

    if difficulty == 1:
        user_answer = input("2 + 2 = ")
        if user_answer == "4":
            print("Correct!")
            print("Your score 1")
            score += 1
        else:
            print("Try again")
        user_answer = input("30+80*50=")
        if user_answer == "4030":
            print("Correct!")
            score += 1
        else:
            print("Try again")
            return "Your score 1"
    elif difficulty == 2:
        user_answer = input("2 + 2 * 2 = ")
        if user_answer == "6":
            print("Correct!")
            score += 1
            print("Your score 1")
        else:
            print("Try again")
            return "Your score 0"
        user_answer = input("30 + 80 * 50 - 20 / 2 = ")
        if user_answer == "4020":
            print("Correct!")
            score += 1
        else:
            print("Try again")
            return "Your score 1"
    elif difficulty == 3:
        user_answer = input("2 + 2 * (2 + 2) = ")
        if user_answer == "10":
            print("Correct!")
            score += 1
            print("Your score 1")
        else:
            print("Try again")
        user_answer = input("(30 + 80) * 50 - 20 / 2 = ")
        if user_answer == "5490":
            print("Correct!")
            score += 1
        else:
            print("Try again")
            return "Your score 1"
    else:
        print("Invalid difficulty")
        return "Your score 0"
    return f"Quest completed, {player}! Your score is {score} points!"


def game() -> str:
    """
    Play a number guessing game.

    Returns:
        "Game Over" when finished
    """
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_input = input("Make a guess: ")
        try:
            guess = int(user_input)
            attempts += 1

            if not 1 <= guess <= 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(
                    f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts."
                )
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    return "Game Over"


def say_hello(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def say_goodbye(name: str) -> str:
    """Return a goodbye message."""
    return f"Goodbye, {name}!"


def is_pressed(key) -> bool:
    """
    Detect if a specific key is pressed using pygame.

    Args:
        key: Pygame key constant (e.g., pygame.K_a)

    Returns:
        True if key was pressed, False otherwise
    """
    import pygame

    pygame.init()
    pygame.display.set_mode((100, 100))
    pygame.display.set_caption("Key Press Detector")
    clock = pygame.time.Clock()
    pressed = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == key:
                pressed = True
                running = False

        clock.tick(30)

    pygame.quit()
    return pressed
