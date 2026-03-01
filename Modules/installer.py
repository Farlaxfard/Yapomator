from tqdm import tqdm
import pyfiglet
import time
import os
import requests

installed = False
installationCompleted = False


def install():
    print(pyfiglet.figlet_format("WISDOM INSTALL", "doom"))
    print("Installing Wise Intelligence & Support Decision-Oriented Model...\n")
    time.sleep(2)

    ##Download Yapomator and display stream progress

    for i in tqdm(range(100), desc="WISDOM INSTALL", ncols=150):
        time.sleep(0.05)  # Simulating a task
    print("\nInstallation completed!")
    installationCompleted = True
    if installationCompleted:
        os.remove("../reqInstall.py")
        os.remove("requirements.json")


def check():
    if not installed:
        inst = input("Install without dependencies? (y/n)")
        if inst == "y":
            print("\nOverriding...\n")
            time.sleep(1)
            install()
        if inst == "n" or inst == "y":
            exit()
        else:
            print(f"\nuh-huh buddy, {inst} indeed.\nbut,")
            check()


if __name__ == "__main__":
    install()
    check()
