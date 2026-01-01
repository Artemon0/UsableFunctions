"""
UsableFunctions - A collection of utility functions for common programming tasks.

This module provides various utilities including:
- Mathematical operations (calculator, factorial)
- File operations (read, write, delete, move)
- Game functions (quest, number guessing)
- Python package management
- File conversion (py to exe)
- User authentication helpers
"""

import math
import os
import random
import shutil
import subprocess
import sys
import time
import socket
import uuid
import psutil
import tkinter as tk

import PyInstaller.__main__
from tqdm import tqdm

__version__ = "1.6.0"
__author__ = "Artem Onyshchenko"
__email__ = "artemon888.com@gmail.com"
__license__ = "GPL v3.0"
__url__ = "https://github.com/Artemon0/UsableFunctions.git"
__download_url__ = (
    "https://github.com/Artemon0/UsableFunctions/archive/refs/tags/1.6.0.tar.gz"
)


class UsableFunctions:
    """A collection of utility functions for various programming tasks."""

    def __init__(self):
        """Initialize UsableFunctions instance."""
        pass

    def print_one(self) -> None:
        """Print a single word or value."""
        print(self)

    @staticmethod
    def calculator(a: float, b: float, op: str) -> float | str:
        """
        Perform basic arithmetic operations.

        Args:
            a: First operand
            b: Second operand
            op: Operator (+, -, *, /, %, **)

        Returns:
            Result of the operation or error message
        """
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "**": lambda x, y: x**y,
        }

        if op in operations:
            return operations[op](a, b)
        elif op in ("/", "%"):
            try:
                return a / b if op == "/" else a % b
            except ZeroDivisionError:
                return "Error: Division by zero"

        return "Invalid operator"

    @staticmethod
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

    @staticmethod
    def say_hello(name: str) -> str:
        """Return a greeting message."""
        return f"Hello, {name}!"

    @staticmethod
    def say_goodbye(name: str) -> str:
        """Return a goodbye message."""
        return f"Goodbye, {name}!"

    @staticmethod
    def py_to_exe(file: str = "main.py") -> str:
        """
        Convert Python file to executable using PyInstaller.

        Args:
            file: Path to Python file

        Returns:
            "Success" or "Failed"
        """
        if not os.path.exists(file):
            print(f"File {file} does not exist.")
            return "Failed"

        import warnings

        warnings.filterwarnings("ignore")

        try:
            with tqdm(total=100, desc="Converting", ncols=60) as pbar:
                pbar.update(10)

                PyInstaller.__main__.run(
                    [
                        file,
                        "--onefile",
                        "--clean",
                        "--noconfirm",
                    ]
                )
                pbar.update(40)

                exe_name = file.replace(".py", ".exe")
                if os.path.exists(f"./dist/{exe_name}"):
                    shutil.move(f"./dist/{exe_name}", f"./{exe_name}")

                # Clean up temporary files
                for path in ["./build", "./dist"]:
                    if os.path.exists(path):
                        shutil.rmtree(path)

                spec_file = file.replace(".py", ".spec")
                if os.path.exists(spec_file):
                    os.remove(spec_file)

                pbar.update(40)

                for _ in tqdm(range(10), desc="Cleaning", ncols=60):
                    time.sleep(0.2)
                pbar.update(10)

            print(f"\n✅ Successfully created: {exe_name}")
            return "Success"

        except Exception as e:
            print(f"\n❌ Error during conversion: {str(e)}")
            return "Failed"

    @staticmethod
    def even_odd(number: int) -> str:
        """Check if a number is even or odd."""
        return "Even" if number % 2 == 0 else "Odd"

    @staticmethod
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

    @staticmethod
    def write_in_new_file(filename: str, content: str) -> str:
        """Write content to a new file."""
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            return "Success"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def read_from_file(filename: str) -> str:
        """Read content from a file."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def delete_file(filename: str) -> str:
        """Delete a file if it exists."""
        try:
            if os.path.exists(filename):
                os.remove(filename)
                return "File deleted successfully"
            return "File does not exist"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def rename_file(old_name: str, new_name: str) -> str:
        """Rename a file."""
        try:
            if os.path.exists(old_name):
                os.rename(old_name, new_name)
                return "File renamed successfully"
            return "File does not exist"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def move_file(source: str, destination: str) -> str:
        """Move a file to a new location."""
        try:
            if os.path.exists(source):
                shutil.move(source, destination)
                return "File moved successfully"
            return "File does not exist"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_random_password(length: int = 8) -> str:
        """Generate a random password with printable ASCII characters."""
        return "".join(chr(random.randint(33, 126)) for _ in range(length))

    @staticmethod
    def factorial(n: int) -> str | int:
        """Calculate factorial recursively."""
        if n < 0:
            return "Undefined for negative numbers"
        if n <= 1:
            return 1
        return n * UsableFunctions.factorial(n - 1)

    @staticmethod
    def math_factorial(n: int) -> int:
        """Calculate factorial using math library."""
        return math.factorial(n)

    @staticmethod
    def while_calculator() -> None:
        """Run an interactive calculator in a loop."""
        print("Welcome to the While Calculator!")
        print("Type 'exit' to quit.")

        while True:
            a_input = input("Enter first number: ")
            if a_input.lower() == "exit":
                break

            op = input("Enter operator (+, -, *, /, %, **): ")
            if op.lower() == "exit":
                break

            b_input = input("Enter second number: ")
            if b_input.lower() == "exit":
                break

            try:
                a = float(a_input)
                b = float(b_input)
                result = UsableFunctions.calculator(a, b, op)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    @staticmethod
    def get_progress_bar(iterable, desc: str = "Processing", ncols: int = 60):
        """Create a progress bar for an iterable."""
        return tqdm(iterable, desc=desc, ncols=ncols)

    @staticmethod
    def update_this_program() -> str:
        """Update UsableFunctions package from GitHub."""
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
        except (subprocess.CalledProcessError, Exception) as e:
            return f"Update failed: {e}"

    @staticmethod
    def create_new_file(filename: str, content: str = "", filepath: str = ".") -> str:
        """Create a new file with optional content."""
        try:
            full_path = os.path.join(filepath, filename)
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(content)
            return "Success"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def read_file_content(filepath: str) -> str:
        """Read content from a file."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
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

    @staticmethod
    def install_package(package: str) -> str:
        """Install a Python package using pip."""
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            return "Success"
        except (subprocess.CalledProcessError, Exception) as e:
            return f"Installation failed: {e}"

    @staticmethod
    def uninstall_package(package: str) -> str:
        """Uninstall a Python package using pip."""
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "uninstall", "-y", package]
            )
            return "Success"
        except (subprocess.CalledProcessError, Exception) as e:
            return f"Uninstallation failed: {e}"

    @staticmethod
    def install_package_git(
        full_git_url: str = "",
        creator_name: str = "Artemon0",
        repo_name: str = "UsableFunctions",
    ) -> dict[str, str]:
        """
        Install a Python package from a Git repository.

        Args:
            full_git_url: Full Git URL (optional)
            creator_name: GitHub username
            repo_name: Repository name

        Returns:
            Dictionary with status and URL
        """
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
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

                for _ in range(80):
                    time.sleep(0.02)
                    pbar.update(1)

                return {"status": "Success", "url": full_git_url}
            except (subprocess.CalledProcessError, Exception) as e:
                pbar.update(80)
                return {
                    "status": "Installation failed",
                    "error": str(e),
                    "url": full_git_url,
                }

    @staticmethod
    def update_this_program_visual() -> str:
        """Update UsableFunctions package with visual progress bar."""
        try:
            with tqdm(total=100, desc="Updating", ncols=60, smoothing=True) as pbar:
                pbar.update(20)

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

                pbar.update(20)
                return f"Update failed: {result.stderr.decode()}"

        except Exception as e:
            return f"Update failed: {str(e)}"

    @staticmethod
    def run_py_file(filepath: str = "") -> str:
        """Run a Python file."""
        try:
            subprocess.run([sys.executable, filepath], check=True)
            return "Success"
        except (subprocess.CalledProcessError, Exception) as e:
            return f"Error: {e}"

    @staticmethod
    def run_py_file_with_args(filepath: str = "", args: list[str] | None = None) -> str:
        """Run a Python file with command-line arguments."""
        if args is None:
            args = []
        try:
            subprocess.run([sys.executable, filepath, *args], check=True)
            return "Success"
        except (subprocess.CalledProcessError, Exception) as e:
            return f"Error: {e}"

    @staticmethod
    def run_python_code(code: str) -> str:
        """Execute Python code dynamically."""
        try:
            exec(code)
            return "Code executed successfully"
        except Exception as e:
            return f"Error executing code: {e}"

    @staticmethod
    def token(
        token: str,
        valid_token: str = "22kc6MhrlSrzpJSbLcSzggFFOYoitIjWreePqqv7U1igIiAZ1PmlxHCgS5v4",
    ) -> dict[str, bool | str]:
        """
        Validate a token against a valid token.

        Returns:
            Dictionary with validation status and token
        """
        return {"valid": token == valid_token, "token": token}

    @staticmethod
    def users(
        users: list[dict[str, str | int]],
        user: dict[str, str | int],
    ) -> dict[str, bool | str | int]:
        """Check if a user exists in the users list."""
        if user in users:
            return {"success": True, **user}
        return {"success": False}

    @staticmethod
    def register(
        users: list[dict[str, str | int]],
        new_user: dict[str, str | int],
    ) -> list[dict[str, str | int]]:
        """Register a new user, auto-incrementing ID if it already exists."""
        existing_ids = {user["id"] for user in users}

        while new_user["id"] in existing_ids:
            new_user["id"] += 1

        users.append(new_user)
        return users

    @staticmethod
    def check_password(
        username: str,
        password: str,
        correct_username: str,
        correct_password: str,
        password_min_length: int = 0,
    ) -> bool:
        """
        Validate username and password.

        Args:
            username: Provided username
            password: Provided password
            correct_username: Expected username
            correct_password: Expected password
            password_min_length: Minimum password length requirement

        Returns:
            True if credentials match, False otherwise
        """
        if password_min_length > 0 and len(password) < password_min_length:
            print(f"Password must be at least {password_min_length} characters long!")
            return False

        return username == correct_username and password == correct_password

    class Circle:
        """Helper class for circle-related calculations."""

        def __init__(self, radius: float = 0, T: float = 0, N: float = 0, t: float = 0):
            """
            Initialize Circle with parameters.

            Args:
                radius: Circle radius
                T: Period
                N: Number of rotations
                t: Time
            """
            self.radius = radius
            self.T = T
            self.N = N
            self.t = t

        def calculate_v(self, radius: float, T: float) -> float:
            """Calculate velocity (circumference)."""
            return 2 * math.pi * radius

        def calculate_T(self, t: float = 0, N: float = 0, n: float = 0) -> float:
            """Calculate period T."""
            if n != 0:
                return 1 / n
            return t / N if N != 0 else 0

        def calculate_n(self, N: float, t: float) -> float:
            """Calculate frequency n."""
            return N / t if t != 0 else 0

        def calculate_N(self, n: float, t: float) -> float:
            """Calculate number of rotations N."""
            return n * t

        def calculate_t(self, N: float, t: float) -> float:
            """Calculate time t."""
            return N * t if N != 0 else 0

    @staticmethod
    def get_ip_address() -> str:
        """Get the IP address of the current machine."""
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def get_mac_address() -> str:
        """Get the MAC address of the current machine."""
        return ":".join(
            [
                "{:02x}".format((uuid.getnode() >> ele) & 0xFF)
                for ele in range(0, 8 * 6, 8)
            ][::-1]
        )

    @staticmethod
    def get_machine_info() -> dict[str, str]:
        """Get basic machine information."""
        return {
            "hostname": socket.gethostname(),
            "ip_address": UsableFunctions.get_ip_address(),
            "mac_address": UsableFunctions.get_mac_address(),
            "platform": sys.platform,
            "python_version": sys.version,
        }

    @staticmethod
    def get_memory_info() -> dict[str, str]:
        """Get memory information."""
        return {
            "total": str(round(psutil.virtual_memory().total / (1024**3), 2)) + " GB",
            "available": str(round(psutil.virtual_memory().available / (1024**3), 2))
            + " GB",
            "used": str(round(psutil.virtual_memory().used / (1024**3), 2)) + " GB",
            "percent": str(psutil.virtual_memory().percent) + " %",
        }

    @staticmethod
    def optimize_system() -> str:  # i need MORE FUNCTIONS IN THIS func
        """Optimize system performance by clearing memory cache. WARNING: Use with caution! This may affect system stability and you need to reload the internet(like me)."""
        try:
            if sys.platform == "win32":
                os.system("echo off | clip")  # Clear clipboard
                os.system("ipconfig /flushdns")  # Flush DNS cache
                os.system("ipconfig /release")  # Release IP address
                # I need to stop process before cleaing temp files(can't clear!)
                os.system("ipconfig /flushdns")  # Flush DNS cache

                os.system("del /q %temp%\\*")  # Delete temporary files
                os.system("taskkill /f /im explorer.exe")  # Restart Explorer process
                os.system("start explorer")
            elif sys.platform == "linux" or sys.platform == "darwin":
                os.system(
                    "sync; echo 3 > /proc/sys/vm/drop_caches"
                )  # Clear cache (Linux)
            return "System optimized successfully"
        except Exception as e:
            return f"Optimization failed: {e}"

    @staticmethod
    def get_disk_info() -> dict[str, str]:
        """Get disk information."""
        return {
            "total": str(round(psutil.disk_usage("/").total / (1024**3), 2)) + " GB",
            "used": str(round(psutil.disk_usage("/").used / (1024**3), 2)) + " GB",
            "free": str(round(psutil.disk_usage("/").free / (1024**3), 2)) + " GB",
            "percent": str(psutil.disk_usage("/").percent) + " %",
        }

    @staticmethod
    def get_cpu_info() -> dict[str, str]:
        """Get CPU information."""
        return {
            "physical_cores": str(psutil.cpu_count(logical=False)),
            "total_cores": str(psutil.cpu_count(logical=True)),
            "max_frequency": str(psutil.cpu_freq().max) + " MHz",
            "min_frequency": str(psutil.cpu_freq().min) + " MHz",
            "current_frequency": str(psutil.cpu_freq().current) + " MHz",
            "usage_percent": str(psutil.cpu_percent(interval=1)) + " %",
        }

    @staticmethod
    def system_panel():
        tk_root = tk.Tk()
        tk_root.title("System Information Panel")
        tk_root.geometry("600x820")

        tk_root.resizable(False, False)
        info = UsableFunctions.get_machine_info()
        memory = UsableFunctions.get_memory_info()
        disk = UsableFunctions.get_disk_info()
        cpu = UsableFunctions.get_cpu_info()
        tk.Label(
            tk_root,
            text="WARNING: Use with caution! \nThis may affect system stability and you need to reload the internet(like me).",
            font=("Arial", 10, "bold"),
        ).pack(pady=10)
        tk.Label(tk_root, text="System Information", font=("Arial", 16, "bold")).pack(
            pady=10
        )
        tk.Label(
            tk_root, text=f"Hostname: {info['hostname']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root, text=f"IP Address: {info['ip_address']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root, text=f"MAC Address: {info['mac_address']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root, text=f"Platform: {info['platform']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root,
            text=f"Python Version: {info['python_version']}",
            font=("Arial", 12),
        ).pack()
        tk.Label(tk_root, text="Memory Information", font=("Arial", 16, "bold")).pack(
            pady=10
        )
        tk.Label(tk_root, text=f"Total: {memory['total']}", font=("Arial", 12)).pack()
        tk.Label(
            tk_root, text=f"Available: {memory['available']}", font=("Arial", 12)
        ).pack()
        tk.Label(tk_root, text=f"Used: {memory['used']}", font=("Arial", 12)).pack()
        tk.Label(
            tk_root, text=f"Percent: {memory['percent']}", font=("Arial", 12)
        ).pack()
        tk.Label(tk_root, text="Disk Information", font=("Arial", 16, "bold")).pack(
            pady=10
        )
        tk.Label(tk_root, text=f"Total: {disk['total']}", font=("Arial", 12)).pack()
        tk.Label(tk_root, text=f"Used: {disk['used']}", font=("Arial", 12)).pack()
        tk.Label(tk_root, text=f"Free: {disk['free']}", font=("Arial", 12)).pack()
        tk.Label(tk_root, text=f"Percent: {disk['percent']}", font=("Arial", 12)).pack()
        tk.Label(tk_root, text="CPU Information", font=("Arial", 16, "bold")).pack(
            pady=10
        )
        tk.Label(
            tk_root, text=f"Physical Cores: {cpu['physical_cores']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root, text=f"Total Cores: {cpu['total_cores']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root, text=f"Max Frequency: {cpu['max_frequency']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root, text=f"Min Frequency: {cpu['min_frequency']}", font=("Arial", 12)
        ).pack()
        tk.Label(
            tk_root,
            text=f"Current Frequency: {cpu['current_frequency']}",
            font=("Arial", 12),
        ).pack()
        tk.Label(
            tk_root, text=f"Usage Percent: {cpu['usage_percent']}", font=("Arial", 12)
        ).pack()
        tk.Button(
            tk_root,
            text="Optimize System",
            command=UsableFunctions.optimize_system,
            font=("Arial", 12),
        ).pack(pady=20)

        # relod after pressing button
        def reload():
            tk_root.destroy()
            UsableFunctions.system_panel()

        tk.Button(tk_root, text="Reload", command=reload, font=("Arial", 12)).pack()

        tk_root.mainloop()

    class FileConverter:
        """Helper class for file conversion operations."""

        @staticmethod
        def png_to_jpg(png_file: str, jpg_file: str) -> str:
            """
            Convert PNG image to JPG format.

            Args:
                png_file: Path to the PNG file
                jpg_file: Path to save the JPG file

            Returns:
                "Success" or "Error" message
            """
            from PIL import Image

            try:
                with Image.open(png_file) as img:
                    rgb_img = img.convert("RGB")
                    rgb_img.save(jpg_file, "JPEG")
                    return "Success"
            except Exception as e:
                return f"Error: {e}"

        @staticmethod
        def jpg_to_png(jpg_file: str, png_file: str) -> str:
            """
            Convert JPG image to PNG format.

            Args:
                jpg_file: Path to the JPG file
                png_file: Path to save the PNG file

            Returns:
                "Success" or "Error" message
            """
            from PIL import Image

            try:
                with Image.open(jpg_file) as img:
                    img.save(png_file, "PNG")
                    return "Success"
            except Exception as e:
                return f"Error: {e}"

        @staticmethod
        def txt_to_pdf(txt_file: str, pdf_file: str) -> str:
            """
            Convert TXT file to PDF format.

            Args:
                txt_file: Path to the TXT file
                pdf_file: Path to save the PDF file

            Returns:
                "Success" or "Error" message
            """
            from fpdf import FPDF

            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.set_font("Arial", size=12)

                with open(txt_file, "r", encoding="utf-8") as file:
                    for line in file:
                        pdf.cell(
                            0,
                            10,
                            txt=line.encode("latin-1", "replace").decode("latin-1"),
                            ln=True,
                        )

                pdf.output(pdf_file)
                return "Success"
            except Exception as e:
                return f"Error: {e}"

        @staticmethod
        def pdf_to_txt(pdf_file: str, txt_file: str) -> str:
            """
            Convert PDF file to TXT format.

            Args:
                pdf_file: Path to the PDF file
                txt_file: Path to save the TXT file

            Returns:
                "Success" or "Error" message
            """
            from PyPDF2 import PdfReader

            try:
                reader = PdfReader(pdf_file)
                with open(txt_file, "w", encoding="utf-8") as file:
                    for page in reader.pages:
                        file.write(page.extract_text() + "\n")
                return "Success"
            except Exception as e:
                return f"Error: {e}"

        @staticmethod
        def jpgs_to_pdf(jpg_files: list, pdf_file: str) -> str:
            """
            Convert multiple JPG images to a single PDF file.

            Args:
                jpg_files: List of paths to JPG files
                pdf_file: Path to save the PDF file

            Returns:
                "Success" or "Error" message
            """
            from PIL import Image

            try:
                image_list = []
                for jpg in jpg_files:
                    img = Image.open(jpg).convert("RGB")
                    image_list.append(img)

                if image_list:
                    image_list[0].save(
                        pdf_file,
                        save_all=True,
                        append_images=image_list[1:],
                    )
                    return "Success"
                else:
                    return "Error: No JPG files provided"
            except Exception as e:
                return f"Error: {e}"

        @staticmethod
        def pdf_to_jpgs(pdf_file: str, jpg_files: list) -> str:
            """
            Convert a PDF file to multiple JPG images.

            Args:
                pdf_file: Path to the PDF file
                jpg_files: List of paths to save the JPG files

            Returns:
                "Success" or "Error" message
            """
            from pdf2image import convert_from_path

            try:
                images = convert_from_path(pdf_file)
                for i, image in enumerate(images):
                    image.save(jpg_files[i], "JPEG")
                return "Success"
            except Exception as e:
                return f"Error: {e}"
