"""System information, maintenance, and the Tkinter panel."""

import os
import shutil
import socket
import subprocess
import sys

import psutil

from .network import get_ip_address, get_mac_address


def get_machine_info() -> dict[str, str]:
    """Get basic machine information."""
    return {
        "hostname": socket.gethostname(),
        "ip_address": get_ip_address(),
        "mac_address": get_mac_address(),
        "platform": sys.platform,
        "python_version": sys.version,
    }


def get_memory_info() -> dict[str, str]:
    """Get memory information."""
    return {
        "total": str(round(psutil.virtual_memory().total / (1024**3), 2)) + " GB",
        "available": str(round(psutil.virtual_memory().available / (1024**3), 2))
        + " GB",
        "used": str(round(psutil.virtual_memory().used / (1024**3), 2)) + " GB",
        "percent": str(psutil.virtual_memory().percent) + " %",
    }


def get_disk_info() -> dict[str, str]:
    """Get disk information."""
    return {
        "total": str(round(psutil.disk_usage("/").total / (1024**3), 2)) + " GB",
        "used": str(round(psutil.disk_usage("/").used / (1024**3), 2)) + " GB",
        "free": str(round(psutil.disk_usage("/").free / (1024**3), 2)) + " GB",
        "percent": str(psutil.disk_usage("/").percent) + " %",
    }


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


def optimize_system() -> {str, bool | str}:
    """
    Optimize system performance by clearing memory, DNS, temp files, and Recycle Bin.
    """
    try:
        if sys.platform == "win32":
            import ctypes

            # 1. Clear clipboard (use shell=True due to the pipe operator '|')
            subprocess.run("echo off | clip", shell=True, capture_output=True)

            # 2. Network optimization
            subprocess.run(["ipconfig", "/flushdns"], capture_output=True)
            subprocess.run(["ipconfig", "/release"], capture_output=True)
            subprocess.run(
                ["ipconfig", "/renew"], capture_output=True
            )  # Restores internet connection

            # 3. Clean Temp files using pure Python
            # This fixes the "can't clear!" issue by safely skipping currently locked files
            temp_dir = os.environ.get("TEMP")
            if temp_dir and os.path.exists(temp_dir):
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        try:
                            os.remove(os.path.join(root, file))
                        except Exception:
                            continue  # File is locked, skip it
                    for folder in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, folder))
                        except Exception:
                            continue  # Folder is locked, skip it

            # 4. NEW FEATURE: Empty Windows Recycle Bin silently
            # Flag 7 means: SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND
            try:
                ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 7)
            except Exception:
                pass

            # 5. Restart Windows Explorer safely
            subprocess.run(
                ["taskkill", "/f", "/im", "explorer.exe"], capture_output=True
            )
            # Use Popen instead of run so the script doesn't freeze waiting for explorer window to close
            subprocess.Popen(["explorer.exe"])

        elif sys.platform in ("linux", "darwin"):
            # Use shell=True for command chains with ';' and redirection '>'
            subprocess.run(
                "sync; echo 3 > /proc/sys/vm/drop_caches",
                shell=True,
                capture_output=True,
            )

        return {"sucess": True, "error": False}

    except Exception as e:
        return {"sucess": False, "error": e}


def system_panel():
    """System Information Panel."""
    import tkinter as tk

    tk_root = tk.Tk()
    tk_root.title("System Information Panel")
    tk_root.geometry("600x820")

    tk_root.resizable(True, True)
    info = get_machine_info()
    memory = get_memory_info()
    disk = get_disk_info()
    cpu = get_cpu_info()
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
        command=optimize_system,
        font=("Arial", 12),
    ).pack(pady=20)

    # relod after pressing button
    def reload():
        tk_root.destroy()
        system_panel()

    tk.Button(tk_root, text="Reload", command=reload, font=("Arial", 12)).pack()

    tk_root.mainloop()
