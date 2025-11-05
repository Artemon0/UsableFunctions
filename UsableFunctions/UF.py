"""
The `UsableFunctions` class in the provided Python code contains various functions for tasks like
printing a single word, performing calculations, running a quest game, greeting users, converting
Python files to executables, determining even or odd numbers, and playing a number guessing game.
"""

import math
import os
import random
import shutil
import subprocess
import sys
import time
from random import randint

import PyInstaller.__main__
from tqdm import tqdm

__version__ = "1.5.4"
__author__ = "Artem Onyshchenko"
__email__ = "artemon888.com@gmail.com"
__license__ = "GPL v3.0"
__url__ = "https://github.com/Artemon0/UsableFunctions.git"
__download_url__ = (
    "https://github.com/Artemon0/UsableFunctions/archive/refs/tags/1.5.4.tar.gz"
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
            return a**b

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
        elif n <= 1:
            return 1
        else:
            return n * UsableFunctions.factorial(n - 1)

    def math_factorial(n: int) -> int:
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

    @staticmethod
    def get_progress_bar(iterable, desc="Processing", ncols=60):
        return tqdm(iterable, desc=desc, ncols=ncols)

    @staticmethod
    def update_this_program():
        try:
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    "git+https://github.com/Artemon0/UsableFunctions.git",
                ],
                check=True,
            )

            subprocess.run(
                [sys.executable, "-m", "pip", "show", "UsableFunctions"], check=True
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
        import pygame  # ! Need to not pygame 2.6.1 (SDL 2.28.4, Python 3.13.7) Hello from the pygame community. https://www.pygame.org/contribute.html

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

    def install_package(package: str) -> str:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            return "Success"
        except subprocess.CalledProcessError as e:
            return f"Installation failed: {e}"
        except Exception as e:
            return f"Installation failed: {e}"

    def uninstall_package(package: str) -> str:
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "uninstall", "-y", package]
            )
            return "Success"
        except subprocess.CalledProcessError as e:
            return f"Uninstallation failed: {e}"
        except Exception as e:
            return f"Uninstallation failed: {e}"

    @staticmethod
    def install_package_git(
        full_git_url: str = "",
        creator_name: str = "Artemon0",
        repo_name: str = "UsableFunctions",
    ) -> dict:
        with tqdm(total=100, desc="Installing", ncols=60) as pbar:
            if not full_git_url:
                full_git_url = f"https://github.com/{creator_name}/{repo_name}.git"
            pbar.update(20)
            try:
                subprocess.check_call(
                    [
                        sys.executable,
                        "-m",
                        "pip",
                        "install",
                        "--upgrade",
                        f"git+{full_git_url}",
                    ],
                    stdout=False,
                    stderr=False,
                )
                for _ in range(80):
                    time.sleep(0.02)
                    pbar.update(1)
                return {"status": "Success", "url": full_git_url}
            except subprocess.CalledProcessError as e:
                pbar.update(80)
                return {
                    "status": "Installation failed",
                    "error": str(e),
                    "url": full_git_url,
                }
            except Exception as e:
                pbar.update(80)
                return {
                    "status": "Installation failed",
                    "error": str(e),
                    "url": full_git_url,
                }

    @staticmethod
    def update_this_program_visual():
        try:
            with tqdm(total=100, desc="Updating", ncols=60, smoothing=True) as pbar:
                pbar.update(20)

                try:
                    result = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "pip",
                            "install",
                            "--upgrade",
                            "git+https://github.com/Artemon0/UsableFunctions.git",
                        ],
                        capture_output=True,
                        check=False,
                    )

                    for _ in range(60):
                        time.sleep(0.02)
                        pbar.update(1)

                    if result.returncode == 0:
                        pbar.update(20)

                        subprocess.run(
                            [sys.executable, "-m", "pip", "show", "UsableFunctions"],
                            check=True,
                        )
                        return "Update successful"
                    else:
                        pbar.update(20)
                        return f"Update failed: {result.stderr}"

                except subprocess.CalledProcessError as e:
                    pbar.update(80)
                    return f"Update failed: {e.stderr}"

        except Exception as e:
            return f"Update failed: {str(e)}"

    @staticmethod
    def run_py_file(filepath: str = ""):
        try:
            subprocess.run([sys.executable, filepath], check=True)
            return "Success"
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def run_py_file_with_args(filepath: str = "", args: list = []):
        try:
            subprocess.run([sys.executable, filepath, *args], check=True)
            return "Success"
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Error: {e}"

    def run_python_code(sefl, code: str):
        try:
            exec(code)
            return "Code executed successfully"
        except Exception as e:
            return f"Error executing code: {e}"

    @staticmethod
    def token(
        token: str,
        valid_token: str = "22kc6MhrlSrzpJSbLcSzggFFOYoitIjWreePqqv7U1igIiAZ1PmlxHCgS5v4",
    ) -> dict:
        def is_token_valid(self) -> bool:
            if token == valid_token:
                return True
            return False

        def get_token(self):
            return token

        return {"valid": is_token_valid(), "tocken": get_token()}

    @staticmethod
    def users(
        users: list[dict["name":str, "password":str, "id":int]],  # noqa: F821
        user: dict[str : str | int],
    ) -> dict[str : bool | int]:
        if user in users:
            res = {"success": True} | user
            return res
        else:
            return {"success": False}

    def register(
        users: list[dict["name":str, "password":str, "id":int]],  # noqa: F821
        new_user: dict["name":str, "password":str, "id":int],  # noqa: F821
    ) -> dict:
        a = [i for i in users]
        r = []
        for q in a:
            d = q["id"]
            r.append(d)

        if new_user["id"] in r:
            new_user["id"] += 1
        users.append(new_user)
        return users

    def check_password(
        username: str,
        password: str,
        correct_username: str,
        correct_password: str,
        password_long: int = 0,
    ) -> bool:
        if len(password) < password_long and password_long != 0:
            print(f"Password may by > {password_long} char long!")
        try:
            if correct_username == username and correct_password == password:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
