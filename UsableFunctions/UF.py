"""
The `UsableFunctions` class in the provided Python code contains various functions for tasks like
printing a single word, performing calculations, running a quest game, greeting users, converting
Python files to executables, determining even or odd numbers, and playing a number guessing game.
"""

import os
import random
import shutil
import subprocess
import sys
import time
from random import randint

import PyInstaller.__main__
from tqdm import tqdm

__version__ = "1.4.2"
__author__ = "Artem Onyshchenko"
__email__ = "artemon888.com@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/Artemon0/UsableFunctions.git"
__download_url__ = (
    "https://github.com/Artemon0/UsableFunctions/archive/refs/tags/1.4.2.tar.gz"
)


class UsableFunctions:
    # ! Prints only one word !
    def print_one(self) -> None:
        print(self)
        return None

    # * Typical calculator
    def calculator(a: float, b: float, op: str):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            try:
                return a / b
            except ZeroDivisionError:
                return ZeroDivisionError
        elif op == "%":
            try:
                return a % b
            except ZeroDivisionError:
                return ZeroDivisionError
        elif op == "**":
            return a ** b

        return "Invalid operator"

    # * Quest with difficulty
    # ! Difficulty is from 1 to 3 !
    def quest(player: str = "Unnamed", difficulty: int = 1):
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

    # * Greeting functions
    def say_hello(name: str):
        return f"Hello, {name}!"

    def say_goodbye(name: str):
        return f"Goodbye, {name}!"

    @staticmethod
    # * Converts .py to .exe using PyInstaller
    def py_to_exe(file: str = "main.py"):
        try:
            if os.path.exists(file):
                pass
        except Exception:
            print(f"File {file} does not exist.")
            return "Failed"
        time.sleep(1)
        import warnings

        warnings.filterwarnings("ignore")

        try:
            # * Создаем прогресс-бар
            with tqdm(total=100, desc="Converting", ncols=60) as pbar:
                # * Подготовка
                pbar.update(10)

                # * Конвертация
                pbar.update(40)
                PyInstaller.__main__.run(
                    [
                        file,
                        "--onefile",
                        # '--windowed',
                        "--clean",
                        "--noconfirm",
                    ]
                )

                # * Очистка и финализация
                pbar.update(40)
                exe_name = file.replace(".py", ".exe")
                if os.path.exists(f"./dist/{exe_name}"):
                    shutil.move(f"./dist/{exe_name}", f"./{exe_name}")

                # * Удаляем временные файлы
                if os.path.exists("./build"):
                    shutil.rmtree("./build")
                if os.path.exists("./dist"):
                    shutil.rmtree("./dist")
                spec_file = file.replace(".py", ".spec")
                if os.path.exists(spec_file):
                    os.remove(spec_file)

                pbar.update(10)
                time.sleep(1)  # Плавность
                for _ in tqdm(range(10), desc="Cleaning", ncols=60):
                    time.sleep(0.2)

            print(f"\n✅ Successfully created: {exe_name}")
            return "Success"

        except Exception as e:
            print(f"\n❌ Error during conversion: {str(e)}")
            return "Failed"

    def even_odd(number: int):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def game():

        number_to_guess = random.randint(1, 100)
        attempts = 0
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            user_input = input("Make a guess: ")
            try:
                guess = int(user_input)
                attempts += 1
                if guess < 1 or guess > 100:
                    print("Please guess a number within the range of 1 to 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
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

        return "Game Over"

    # todo: Add more functions here
    def write_in_new_file(filename: str, content: str):
        try:
            with open(filename, "w") as file:
                file.write(content)
            return "Success"
        except Exception as e:
            return f"Error: {e}"

    def read_from_file(filename: str):
        try:
            with open(filename, "r") as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error: {e}"

    def delete_file(filename: str):
        try:
            if os.path.exists(filename):
                os.remove(filename)
                return "File deleted successfully"
            else:
                return "File does not exist"
        except Exception as e:
            return f"Error: {e}"

    def rename_file(old_name: str, new_name: str):
        try:
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                return "File renamed successfully"
            else:
                return "File does not exist"
        except Exception as e:
            return f"Error: {e}"

    def move_file(source: str, destination: str):
        try:
            if os.path.exists(source):
                shutil.move(source, destination)
                return "File moved successfully"
            else:
                return "File does not exist"
        except Exception as e:
            return f"Error: {e}"

    # TODO: More functions can be added here
    def get_random_password(length: int = 8) -> str:
        password = ""
        for _ in range(length):  # Length of the password
            char = chr(randint(33, 126))  # Printable ASCII characters
            password += char
        return password

    def factorial(n: int) -> str | int:
        if n < 0:
            return "Undefined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

    def math_factorial(n: int) -> int:
        import math

        return math.factorial(n)

    def while_calculator():
        print("Welcome to the While Calculator!")
        print("Type 'exit' to quit.")
        while True:
            a = input("Enter first number: ")
            if a.lower() == "exit":
                break
            op = input("Enter operator (+, -, *, /, %): ")
            if op.lower() == "exit":
                break
            b = input("Enter second number: ")
            if b.lower() == "exit":
                break
            try:
                a = float(a)
                b = float(b)
                result = UsableFunctions.calculator(a, b, op)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")


def get_progress_bar(iterable, desc="Processing", ncols=60):
    return tqdm(iterable, desc=desc, ncols=ncols)


def update_this_program(self):
    try:
        # subprocess.run(
        #     [
        #         sys.executable,
        #         "-m",
        #         "pip",
        #         "install",
        #         "--upgrade",
        #         "UsableFunctions",
        #     ],
        #     check=True,
        # )
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "git+https://github.com/Artemon0/UsableFunctions.git",
            ]
        )

        subprocess.run(
            [sys.executable, "-m", "pip", "show", "UsableFunctions", ""], check=True
        )
        return "Update successful"
    except subprocess.CalledProcessError as e:
        return f"Update failed: {e}"
    except Exception as e:
        return f"Update failed: {e}"


def create_new_file(filename: str, content: str = "", filepath: str = "."):
    try:
        full_path = os.path.join(filepath, filename)
        with open(full_path, "w") as file:
            file.write(content)
        return "Success"
    except Exception as e:
        return f"Error: {e}"


def read_file_content(filepath: str) -> str:
    try:
        with open(filepath, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error: {e}"


# ! example: key = pygame.K_a
def is_pressed(key) -> bool:
    import \
        pygame  # ! Need to not pygame 2.6.1 (SDL 2.28.4, Python 3.13.7) Hello from the pygame community. https://www.pygame.org/contribute.html
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
            elif event.type == pygame.KEYDOWN:
                if event.key == key:
                    pressed = True
                    running = False

        clock.tick(30)

    pygame.quit()
    return pressed
