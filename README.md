# Usable Functions

A collection of utility functions for common programming tasks in Python.

## 🚀 Installation

### From PyPI (recommended)

```bash
pip install usable-functions
```

### From GitHub (latest version)

```bash
pip install git+https://github.com/Artemon0/UsableFunctions.git
```

### Development setup

```bash
git clone https://github.com/Artemon0/UsableFunctions.git
cd UsableFunctions
pip install -e '.[dev]'
```

## ✨ Quick Start

```python
from UsableFunctions import UsableFunctions as uf

# Calculator
result = uf.calculator(5, 7, '+')  # Returns: 12

# Generate random password
password = uf.get_random_password(12)

# Check if number is even or odd
print(uf.even_odd(42))  # Returns: "Even"

# Play a quest game
uf.quest("Player1", difficulty=2)
```

## 🎮 Interactive Examples

Try it live in your browser!

```python
from UsableFunctions import UsableFunctions as uf

# Calculate factorial
print(f"Factorial of 5: {uf.factorial(5)}")

# Generate a random color
print(f"Random color: {uf.get_random_color()}")

# Check if string is palindrome
print(f"Is 'radar' a palindrome? {uf.is_palindrome('radar')}")
```

## 📚 Documentation

Visit our [documentation website](https://artemon0.github.io/UsableFunctions/) for interactive examples and complete API reference.

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

## 📜 License

This project is licensed under the GPL v3.0 - see the [LICENSE](LICENSE) file for details.
- Dark/Light theme support
- Multi-language support (EN/RU)

## 🚀 Functions:

- **calculator(\***a, b, operator**\*)**
- **quest(\***player, difficulty(1-3)**\*)**
- **say_hello(\***name**\*)**
- **say_goodbye(\***name**\*)**
- **py_to_exe(\***file**\*)** _// converts .py -> .exe_
- **even_odd(\***number**\*)**
- **game()**
- **write_in_new_file(\***file name, what?**\*)**
- **read_from_file(\***file name**\*)**
- **delete_file(\***file name**\*)**
- **rename_file(\***old name, new name**\*)**
- **move_file(\***source, destination**\*)**
- **get_random_password() ->** str // random password
- **factorial(n) ->** int // factorial
- **math-factorial(n)** -> int // math.factorial(n)
- **while_calculator()** -> None // calculator in while True
- **get_progress_bar(iterable, desc="Processing", ncols=60)**
- **update_this_program(visual: bool)** // updating UsableFunctions visual/not visual
- **create_new_file(filename: str, content: str="", filepath: str=".")** // updated version of write_in_new_file
- **read_file_content(filepath: str) -> str** // reads file
- **is_pressed(key) -> bool** // key - pygame. **...**
- **install_package(package: str)** // pip install **...**
- **uninstall_package(package: str)** // pip uninstall **...**
- **install_package_git(GitHub_full_https: str, package_name: str = "UsableFunctions", creator_name: str = "Artemon0")** // pip install **git+...**
- **Update_this_program_visual()** // updates UF with tqdm
- **run_py_file(filepath: str)** // runnes py file
- **run_py_file_with_args(filepath: str, args: list = []**)
- **run_python_code(code: str)** // runnes py code
- **token(token: str, valid_token: str) -> dict** // token and valid token
- **users(users: list(dict), user(dict)) -> dict** // is user un users
- **register(users: list(dict()), user: dict) -> dict{new_users}**
- **check_password(username: str, password: str, correct_username: str,correct_password: str, password_long: int = 0) -> bool:** // returns is your password valid :)

# 👨‍💻 About Me

I am Artem, 12 y.o. Python developer.
- **Telegram:** [@Artemon0000](https://t.me/Artemon0000)
- **Channel:** [Telegram](https://t.me/AOGames888)
- **GitHub:** [Artemon0](https://github.com/Artemon0)
