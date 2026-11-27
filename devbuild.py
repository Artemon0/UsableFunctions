#!/usr/bin/env python
"""Build script for UsableFunctions package."""

import shutil
import subprocess
import sys
from pathlib import Path


def clean():
    """Remove build artifacts."""
    print("🧹 Cleaning build artifacts...")
    dirs_to_remove = ["build", "dist", "*.egg-info", "__pycache__"]
    
    for pattern in dirs_to_remove:
        for path in Path(".").rglob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"  Removed: {path}")


def build():
    """Build the package."""
    print("📦 Building package...")
    subprocess.run([sys.executable, "-m", "build"], check=True)
    print("✅ Build complete!")


def install_local():
    """Install package in editable mode."""
    print("📥 Installing package locally (editable mode)...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-e", "."], check=True)
    print("✅ Installation complete!")


def test():
    """Run the package tests."""
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        check=True,
    )
    

def main():
    """Main build process."""
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "clean":
            clean()
        elif command == "build":
            build()
        elif command == "install":
            install_local()
        elif command == "test":
            test()
        elif command == "all":
            clean()
            build()
            install_local()
            test()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: clean, build, install, test, all")
            sys.exit(1)
    else:
        print("Usage: python devbuild.py [clean|build|install|test|all]")
        print("\nCommands:")
        print("  clean   - Remove build artifacts")
        print("  build   - Build the package")
        print("  install - Install package locally (editable)")
        print("  test    - Run package tests")
        print("  all     - Run all steps")


if __name__ == "__main__":
    main()
