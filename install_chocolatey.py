import subprocess

def install_chocolatey():
    # Set execution policy to Bypass for the current process
    subprocess.run([
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-Command",
        "Set-ExecutionPolicy Bypass -Scope Process -Force;"
        "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    ], check=True)

if __name__ == "__main__":
    install_chocolatey()
