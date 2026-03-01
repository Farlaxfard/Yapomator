import json
import subprocess
import sys
import importlib.util
import os
import time
from Modules import installer
import requests


def is_module_installed(module_name):
    """Checks if a module is already available in the current environment."""
    # Handle cases like 'tkinter' which might be under different names or built-in
    spec = importlib.util.find_spec(module_name)
    return spec is not None


def run_smart_install(json_filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, json_filename)

    try:
        with open(full_path, "r") as f:
            data = json.load(f)
            commands = data.get("commands", [])

        for cmd in commands:
            # Extract the package name (e.g., 'tqdm' from 'pip install tqdm')
            parts = cmd.split()
            if "install" in parts:
                package_name = parts[parts.index("install") + 1]
            else:
                continue  # Skip if it's not an install command

            if is_module_installed(package_name):
                print(f"✅ {package_name} is already available. Skipping...")
                continue

            print(f"🚀 Installing {package_name}...")
            # Use sys.executable to ensure the correct environment is targeted
            pip_cmd = [sys.executable, "-m", "pip", "install", package_name]

            try:
                subprocess.check_call(
                    pip_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
                )
                print(f"Successfully installed {package_name}!")
            except subprocess.CalledProcessError:
                print(
                    f"⚠️  Could not install {package_name}. It might be a built-in or system-level module."
                )

    except FileNotFoundError:
        print(f"Error: {json_filename} not found.")


def downloadInstaller():
    pass


if __name__ == "__main__":
    run_smart_install("Modules/requirements.json")
    downloadInstaller()

    time.sleep(0.5)
    print("\n Launching WISDOM Installer...")

    installer.install()
