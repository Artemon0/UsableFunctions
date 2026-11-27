"""Credential checks and password generation for demos."""

import random


def get_random_password(length: int = 8) -> str:
    """Generate a random password with printable ASCII characters."""
    return "".join(chr(random.randint(33, 126)) for _ in range(length))


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


def users(
    users: list[dict[str, str | int]],
    user: dict[str, str | int],
) -> dict[str, bool | str | int]:
    """Check if a user exists in the users list."""
    if user in users:
        return {"success": True, **user}
    return {"success": False}


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
