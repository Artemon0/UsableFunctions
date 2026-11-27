"""Python package installation and updates."""

import subprocess
import sys
import time

from tqdm import tqdm


def install_package(package: str) -> str:
    """Install a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return "Success"
    except (subprocess.CalledProcessError, Exception) as e:
        return f"Installation failed: {e}"


def uninstall_package(package: str) -> str:
    """Uninstall a Python package using pip."""
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "uninstall", "-y", package]
        )
        return "Success"
    except (subprocess.CalledProcessError, Exception) as e:
        return f"Uninstallation failed: {e}"


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
