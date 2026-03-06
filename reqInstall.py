import json
import subprocess
import sys
import importlib.util
import os
import time
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
                continue  # Skip if it's not an installation command

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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    installer_path = os.path.join(script_dir, "Modules", "installer.py")

    installer_url = "https://github.com/Farlaxfard/Yapomator/raw/refs/heads/main/Modules/installer.py"

    print("\n📦 Downloading installer module...")

    try:
        r = requests.get(installer_url, stream=True, timeout=15)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to download installer: {e}")
        return False

    total_size = int(r.headers.get("content-length", 0))
    chunk_size = 8192

    os.makedirs(os.path.dirname(installer_path), exist_ok=True)

    with open(installer_path, "wb") as f:
        downloaded = 0
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)

    print("Installer module downloaded successfully.")
    return True


if __name__ == "__main__":
    run_smart_install("Modules/requirements.json")
    if not downloadInstaller():
        sys.exit(1)

    time.sleep(0.5)
    print("\n Launching WISDOM Installer...")

    from Modules import installer

    # installer.install()
exit(0)
