"""Python execution, packaging, progress, and timing helpers."""

import os
import shutil
import subprocess
import sys
import time

from tqdm import tqdm


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

    import PyInstaller.__main__

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


def run_py_file(filepath: str = "") -> str:
    """Run a Python file."""
    try:
        subprocess.run([sys.executable, filepath], check=True)
        return "Success"
    except (subprocess.CalledProcessError, Exception) as e:
        return f"Error: {e}"


def run_py_file_with_args(filepath: str = "", args: list[str] | None = None) -> str:
    """Run a Python file with command-line arguments."""
    if args is None:
        args = []
    try:
        subprocess.run([sys.executable, filepath, *args], check=True)
        return "Success"
    except (subprocess.CalledProcessError, Exception) as e:
        return f"Error: {e}"


def run_python_code(code: str) -> str:
    """Execute Python code dynamically."""
    try:
        exec(code)
        return "Code executed successfully"
    except Exception as e:
        return f"Error executing code: {e}"


def get_progress_bar(iterable, desc: str = "Processing", ncols: int = 60):
    """Create a progress bar for an iterable."""
    return tqdm(iterable, desc=desc, ncols=ncols)


def function_time(function: object) -> float:
    time_b = time.time()
    function()
    time_a = time.time()
    return time_b - time_a
