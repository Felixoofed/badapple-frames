#!/usr/bin/env python3
import os
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    if os.path.exists("tools/.git"):
        run("git submodule update --remote --merge")
    else:
        print("No tools submodule found.")