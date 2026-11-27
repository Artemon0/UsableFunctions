# UsableFunctions

[![Version](https://img.shields.io/github/v/release/Artemon0/UsableFunctions)](https://github.com/Artemon0/UsableFunctions/releases)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![CI](https://github.com/Artemon0/UsableFunctions/actions/workflows/python-package.yml/badge.svg)](https://github.com/Artemon0/UsableFunctions/actions/workflows/python-package.yml)

A single-import Python toolkit that bundles the utility functions you end up rewriting in every project: math helpers, file operations, package management, system/network info, file conversion, and a couple of small games.

**[Full documentation & interactive examples](https://artemon0.github.io/UsableFunctions/)** — dark/light theme, EN/RU

---

## Table of Contents

- [Installation](#installation)
- [Project structure](#project-structure)
- [Quick Start](#quick-start)
- [Function Reference](#function-reference)
  - [Math](#math)
  - [Games](#games)
  - [Files](#files)
  - [File Conversion](#file-conversion)
  - [Packages & Scripts](#packages--scripts)
  - [Auth Helpers](#auth-helpers)
  - [System & Network Info](#system--network-info)
  - [Circle](#circle-helper-class)
- [Known Issues](#known-issues)
- [Ideas for New Functions](#ideas-for-new-functions)
- [About](#about)

---

[![GitHub stars](https://img.shields.io/github/stars/Artemon0/UsableFunctions?style=social)](https://github.com/Artemon0/UsableFunctions/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Artemon0/UsableFunctions?style=social)](https://github.com/Artemon0/UsableFunctions/network/members)
[![GitHub last commit](https://img.shields.io/github/last-commit/Artemon0/UsableFunctions)](https://github.com/Artemon0/UsableFunctions/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Artemon0/UsableFunctions)](https://github.com/Artemon0/UsableFunctions)

## Installation

### From GitHub (recommended)

```bash
python -m pip install --upgrade git+https://github.com/Artemon0/UsableFunctions.git
```

### From source

```bash
git clone https://github.com/Artemon0/UsableFunctions.git
cd UsableFunctions
python -m pip install -e .
```

### Development setup

```bash
python -m pip install -e .
python -m pip install build twine
python devbuild.py test
```

New tagged releases include a wheel and source archive on [GitHub Releases](https://github.com/Artemon0/UsableFunctions/releases).

## Project structure

- `UsableFunctions/UF.py` exposes the public class. Both `from UsableFunctions import UsableFunctions` and `from UsableFunctions.UF import UsableFunctions` work.
- `math_utils.py` handles arithmetic and `Circle`. `games.py` contains console games and keyboard input.
- `files.py` handles file operations, downloads, and archives. `converters.py` contains file converters and their Tkinter launcher.
- `packages.py` installs and updates packages. `scripts.py` runs and bundles Python scripts.
- `auth.py` contains demo credential helpers. `network.py` handles network information, and `system.py` contains system information and the system panel.
- `tests/` contains package tests. `docs/` contains the documentation site.

See [DEPLOYMENT.md](DEPLOYMENT.md) for CI and release instructions.

---

## Quick Start

```python
from UsableFunctions import UsableFunctions as u

# Calculator
result = u.calculator(5, 7, '+')          # 12

# Generate a random password
password = u.get_random_password(12)

# Check if a number is even or odd
print(u.even_odd(42))                     # "Even"

# Play the quest mini-game
u.quest("Player1", difficulty=2)
```

---

## Function Reference

### Math

| Function | Description |
|---|---|
| `calculator(a, b, op) -> float \| str` | Basic arithmetic: `+ - * / % **` |
| `even_odd(number) -> str` | Returns `"Even"` or `"Odd"` |
| `factorial(n) -> int \| str` | Manual factorial implementation |
| `math_factorial(n) -> int` | Factorial via `math.factorial` |
| `while_calculator() -> None` | Interactive calculator loop (runs until exit) |
| `Circle` | Helper class for circular-motion calculations — [see below](#circle-helper-class) |

### Games

| Function | Description |
|---|---|
| `quest(player="Unnamed", difficulty=1) -> str` | Text-based math quiz, difficulty `1–3` |
| `game() -> str` | Number-guessing game |
| `say_hello(name) -> str` | Returns a greeting |
| `say_goodbye(name) -> str` | Returns a farewell |

### Files

| Function | Description |
|---|---|
| `write_in_new_file(filename, content) -> str` | Create a file and write to it |
| `read_from_file(filename) -> str` | Read a file's contents |
| `delete_file(filename) -> str` | Delete a file |
| `rename_file(old_name, new_name) -> str` | Rename a file |
| `move_file(source, destination) -> str` | Move a file |
| `create_new_file(filename, content="", filepath=".") -> str` | Newer version of `write_in_new_file`, with a target directory |
| `read_file_content(filepath) -> str` | Newer version of `read_from_file` |
| `download_file(url, file_path) -> str` | Stream-download a file from a URL |
| `compress_folder(folder_path, archive_file_path, password="") -> None` | Zip a folder |
| `extract_archive(archive_path, extract_to=".") -> str` | Extract a `.zip` archive |
| `get_file_hash(filepath, algorithm="sha256") -> str` | Hash a file (`sha256`, `md5`, etc.) |
| `get_folder_size(folder_path) -> str` | Total size of a folder, formatted in MB |

### File Conversion

All under `UsableFunctions.FileConverter`:

| Function | Description |
|---|---|
| `png_to_jpg(png_file, jpg_file) -> str` | Convert PNG → JPG |
| `jpg_to_png(jpg_file, png_file) -> str` | Convert JPG → PNG |
| `txt_to_pdf(txt_file, pdf_file) -> str` | Convert TXT → PDF |
| `pdf_to_txt(pdf_file, txt_file) -> str` | Convert PDF → TXT |
| `jpgs_to_pdf(*jpg_files, pdf_file) -> str` | Combine multiple JPGs into a single PDF |
| `FileConverter.gui.gui()` | Universal Tkinter GUI launcher for the converters above |
| `FileConverter.gui.converter(mode="png_to_jpg")` | Open a specific converter's GUI directly |

### Packages & Scripts

| Function | Description |
|---|---|
| `install_package(package) -> str` | `pip install <package>` |
| `uninstall_package(package) -> str` | `pip uninstall <package>` |
| `install_package_git(full_git_url="", creator_name="Artemon0", repo_name="UsableFunctions") -> dict` | Install a package straight from a Git repo, with a progress bar |
| `update_this_program() -> str` | Update UsableFunctions to the latest version |
| `update_this_program_visual() -> str` | Same as above, with a `tqdm` progress bar |
| `py_to_exe(file="main.py") -> str` | Bundle a `.py` script into a standalone `.exe` via PyInstaller |
| `run_py_file(filepath="") -> str` | Run a Python file in a subprocess |
| `run_py_file_with_args(filepath="", args=None) -> str` | Same, with CLI arguments |
| `run_python_code(code) -> str` | Execute a Python code string |
| `get_progress_bar(iterable, desc="Processing", ncols=60)` | Wrap an iterable in a `tqdm` progress bar |
| `is_pressed(key) -> bool` | Check whether a key is currently pressed (via `pygame`) |
| `function_time(function) -> float` | Time how long a callable takes to run |

### Auth Helpers

> These are lightweight helpers for prototypes/learning projects, **not** a replacement for a real auth system (no hashing, no salting — don't use them to store real user passwords).

| Function | Description |
|---|---|
| `token(token, valid_token=...) -> dict` | Compare a token against an expected value |
| `users(users, user) -> dict` | Check whether a user dict exists in a list of users |
| `register(users, new_user) -> list` | Append a new user, auto-incrementing `id` on collision |
| `check_password(username, password, correct_username, correct_password, password_min_length=0) -> bool` | Validate credentials, with an optional minimum length check |

### System & Network Info

| Function | Description |
|---|---|
| `get_ip_address() -> str` | Local IP address |
| `get_external_ip() -> str` | Public IP address (via ipify) |
| `get_mac_address() -> str` | MAC address |
| `get_machine_info() -> dict` | Hostname, IP, MAC, platform, Python version |
| `get_memory_info() -> dict` | Total/available/used RAM and usage percent |
| `get_disk_info() -> dict` | Disk usage stats |
| `get_cpu_info() -> dict` | CPU core count, frequency, usage |
| `ping_host(host="8.8.8.8") -> bool` | Ping a host, returns reachability |
| `optimize_system() -> dict` | ⚠️ Clears memory cache, DNS cache, and temp files. **Use with caution** — this can affect system stability and drops your network connection briefly. |
| `system_panel()` | Tkinter GUI panel showing live system info, with an "optimize" button |

### Circle (helper class)

`UsableFunctions.Circle(radius=0, T=0, N=0, t=0)` — circular-motion calculations for physics problems.

| Method | Description |
|---|---|
| `calculate_v(radius, T) -> float` | Velocity (circumference) |
| `calculate_T(t=0, N=0, n=0) -> float` | Period |
| `calculate_n(N, t) -> float` | Frequency |
| `calculate_N(n, t) -> float` | Number of rotations |
| `calculate_t(N, t) -> float` | Time |

---

## Known Issues

- **`compress_folder`** raises `TypeError` because `shutil.make_archive` does not accept a `password` argument.
- **Auth helpers** (`token`, `users`, `register`, `check_password`) store/compare credentials in plain text with no hashing — fine for demos, risky if used for real accounts. Worth a one-line warning wherever these are documented (added above).

---

## Ideas for New Functions

A few directions that would fit the existing style of the library:

**Files & data**
- `read_json` / `write_json` — load/save JSON with one call instead of boilerplate `open()` + `json.load`/`dump`
- `read_csv` / `write_csv` — thin wrapper around `csv`/`pandas` for quick tabular I/O
- `merge_files(files, output)` — concatenate multiple text files into one
- `watch_folder(path, callback)` — call a function whenever a folder's contents change

**Text & strings**
- `slugify(text) -> str` — turn a string into a URL-safe slug
- `generate_lorem(paragraphs=1) -> str` — placeholder text generator
- `count_words(text) -> dict` — word frequency counter

**Networking**
- `is_port_open(host, port) -> bool` — quick TCP port check, complements `ping_host`
- `get_weather(city) -> dict` — thin wrapper over a public weather API
- `shorten_url(url) -> str` — URL shortener via a public API

**Security & validation**
- `validate_email(email) -> bool`
- `hash_password(password) -> str` / `verify_password(password, hashed) -> bool` — proper salted hashing (e.g. via `bcrypt`), to responsibly replace the current plain-text `check_password` for real use cases

**Dev tooling**
- `benchmark(function, runs=1) -> dict` — run `function_time` multiple times and return min/max/avg
- `retry(function, attempts=3, delay=1)` — decorator/wrapper for retrying flaky calls
- `env(key, default=None)` — typed `.env` / environment-variable reader

**Fun / games**
- `rock_paper_scissors(player_choice) -> str`
- `tic_tac_toe()` — console-based two-player game, similar spirit to `quest`/`game`

---

## About

I'm Artem, a Python developer working on open-source tools and libraries.

- **Telegram:** [@Artemon0000](https://t.me/Artemon0000)
- **GitHub:** [Artemon0](https://github.com/Artemon0)

Русская версия документации: [README_ru.md](README_ru.md)
