"""File operations, downloads, hashes, and ZIP archives."""

import os
import shutil

import requests


def write_in_new_file(filename: str, content: str) -> str:
    """Write content to a new file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return "Success"
    except Exception as e:
        return f"Error: {e}"


def read_from_file(filename: str) -> str:
    """Read content from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error: {e}"


def delete_file(filename: str) -> str:
    """Delete a file if it exists."""
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return "File deleted successfully"
        return "File does not exist"
    except Exception as e:
        return f"Error: {e}"


def rename_file(old_name: str, new_name: str) -> str:
    """Rename a file."""
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            return "File renamed successfully"
        return "File does not exist"
    except Exception as e:
        return f"Error: {e}"


def move_file(source: str, destination: str) -> str:
    """Move a file to a new location."""
    try:
        if os.path.exists(source):
            shutil.move(source, destination)
            return "File moved successfully"
        return "File does not exist"
    except Exception as e:
        return f"Error: {e}"


def create_new_file(filename: str, content: str = "", filepath: str = ".") -> str:
    """Create a new file with optional content."""
    try:
        full_path = os.path.join(filepath, filename)
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(content)
        return "Success"
    except Exception as e:
        return f"Error: {e}"


def read_file_content(filepath: str) -> str:
    """Read content from a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error: {e}"


def download_file(url: str, file_path: str):
    """Download a file from a URL."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return "Success"
    else:
        return f"Failed to download. Status Code: {response.status_code}"


def compress_folder(folder_path: str, archive_file_path: str, password: str = ""):
    """Compress a folder using shutil."""
    shutil.make_archive(archive_file_path, "zip", folder_path, password=password)


def get_file_hash(filepath: str, algorithm: str = "sha256") -> str:
    """Computing hash (sha256, md5 and others)."""
    import hashlib

    if not os.path.exists(filepath):
        return "Error: File does not exist"
    try:
        hash_func = hashlib.new(algorithm)
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        return f"Error: {e}"


def extract_archive(archive_path: str, extract_to: str = ".") -> str:
    """Unzip .zip archive."""
    try:
        shutil.unpack_archive(archive_path, extract_to)
        return "Success"
    except Exception as e:
        return f"Error: {e}"


def get_folder_size(folder_path: str) -> str:
    """Get folder size in MB."""
    size = 0
    if not os.path.exists(folder_path):
        return "Folder does not exist"
    for dirpath, _, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                size += os.path.getsize(fp)
    return f"{round(size / (1024**2), 2)} MB"
