import subprocess
import shutil

def check_chocolatey_installed():
    return shutil.which("choco") is not None

def install_packages():
    packages = [
        "git",
        "nodejs-lts",
        "vscode",
        "temurin",       # Latest OpenJDK
        "maven"
    ]

    for pkg in packages:
        print(f"📦 Installing {pkg}...")
        subprocess.run(["choco", "install", pkg, "-y"], check=True)

def main():
    print("🚀 Setting up developer environment...")

    if not check_chocolatey_installed():
        print("❌ Chocolatey is not installed. Please run bootstrap.ps1 first.")
        return

    install_packages()
    print("✅ All dev tools installed successfully!")

if __name__ == "__main__":
    main()
