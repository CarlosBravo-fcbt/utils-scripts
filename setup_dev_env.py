import subprocess
import shutil

def check_chocolatey_installed():
    return shutil.which("choco") is not None

def is_package_installed(pkg: str) -> bool:
    try:
        result = subprocess.run(
            ["choco", "list", "--local-only", "--exact", pkg],
            capture_output=True, text=True, check=True
        )
        return pkg.lower() in result.stdout.lower()
    except subprocess.CalledProcessError:
        return False

def run_command(cmd, check=True):
    return subprocess.run(cmd, shell=True, check=check)

def install_packages():
    packages = [
        "git",
        "nodejs-lts",    # Install stable Node.js version directly
        "nvm",           # Also install nvm-windows for version management
        "vscode",
        "temurin",
        "maven"
    ]

    for pkg in packages:
        if is_package_installed(pkg):
            print(f"✅ {pkg} is already installed, skipping.")
        else:
            print(f"📦 Installing {pkg}...")
            subprocess.run(["choco", "install", pkg, "-y"], check=True)

def setup_node_with_nvm(node_version="lts"):
    print(f"🐙 Setting up Node.js {node_version} using nvm...")
    try:
        run_command(f"nvm install {node_version}")
        run_command(f"nvm use {node_version}")
        print(f"✅ Node.js {node_version} installed and set as default in nvm.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install or use Node.js via nvm: {e}")

def show_versions():
    print("\n✅ Installed tool versions:")
    cmds = [
        (["git", "--version"], "Git"),
        (["node", "--version"], "Node.js"),
        (["code", "--version"], "VSCode"),
        (["java", "-version"], "Java"),
        (["mvn", "-version"], "Maven")
    ]

    for cmd, name in cmds:
        print(f"\n🔍 {name}:")
        try:
            subprocess.run(cmd, check=True)
        except Exception:
            print(f"⚠️ Could not get version for {name}")

def main():
    print("🚀 Setting up developer environment...")

    if not check_chocolatey_installed():
        print("❌ Chocolatey is not installed. Please run install_chocolatey_python.ps1 first.")
        return

    install_packages()
    setup_node_with_nvm("lts")  # You can specify version like "18.17.1" if preferred
    show_versions()
    print("\n🎉 All done! Your development environment is ready.")

if __name__ == "__main__":
    main()
