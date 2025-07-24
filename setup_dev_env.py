
---

## 🐍 **Updated `setup_dev_env.py`** (with version checks)

```python
import subprocess
import shutil

def check_chocolatey_installed():
    return shutil.which("choco") is not None

def install_packages():
    packages = [
        "git",
        "nodejs-lts",
        "vscode",
        "temurin",       # OpenJDK
        "maven"
    ]

    for pkg in packages:
        print(f"📦 Installing {pkg}...")
        subprocess.run(["choco", "install", pkg, "-y"], check=True)

def show_versions():
    print("\n✅ Installed tool versions:")
    cmds = [
        ["git", "--version"],
        ["node", "--version"],
        ["code", "--version"],
        ["java", "-version"],
        ["mvn", "-version"]
    ]
    for cmd in cmds:
        try:
            subprocess.run(cmd, check=True)
        except Exception:
            print(f"⚠️ Could not get version for: {' '.join(cmd)}")

def main():
    print("🚀 Setting up developer environment...")

    if not check_chocolatey_installed():
        print("❌ Chocolatey is not installed. Please run install_chocolatey_python.ps1 first.")
        return

    install_packages()
    show_versions()
    print("\n🎉 All dev tools installed successfully!")

if __name__ == "__main__":
    main()
