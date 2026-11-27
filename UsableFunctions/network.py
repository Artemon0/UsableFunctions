"""Network address and reachability helpers."""

import socket
import subprocess
import uuid

import requests


def get_ip_address() -> str:
    """Get the IP address of the current machine."""
    return socket.gethostbyname(socket.gethostname())


def get_mac_address() -> str:
    """Get the MAC address of the current machine."""
    return ":".join(
        [
            "{:02x}".format((uuid.getnode() >> ele) & 0xFF)
            for ele in range(0, 8 * 6, 8)
        ][::-1]
    )


def get_external_ip() -> str:
    """Get your public IP using shared API"""
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except Exception as e:
        return f"Error (No internet?): {e}"


def ping_host(host: str = "8.8.8.8") -> bool:
    """Check host"""
    import platform

    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return (
        subprocess.run(
            command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        ).returncode
        == 0
    )
