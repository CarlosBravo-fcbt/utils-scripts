Write-Host "🚀 Starting bootstrap..."

# Step 1: Install Chocolatey if missing
if (!(Get-Command choco.exe -ErrorAction SilentlyContinue)) {
    Write-Host "🔧 Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "✅ Chocolatey installed."
} else {
    Write-Host "✅ Chocolatey is already installed."
}

# Step 2: Install Python if missing
if (!(Get-Command python.exe -ErrorAction SilentlyContinue)) {
    Write-Host "🐍 Installing Python..."
    choco install python -y
    Write-Host "✅ Python installed."

    Write-Host "♻️ Reloading PATH so python is available..."
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
} else {
    Write-Host "✅ Python is already installed."
}

# Step 3: Run Python script to install dev tools
Write-Host "📦 Running setup_dev_env.py..."
python setup_dev_env.py

Write-Host "🎉 All done!"
