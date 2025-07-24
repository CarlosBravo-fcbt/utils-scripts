Write-Host "🚀 Starting bootstrap..."

# Step 1: Install Chocolatey if missing
if (!(Get-Command choco.exe -ErrorAction SilentlyContinue)) {
    Write-Host "🔧 Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "✅ Chocolatey installed."

    # Add choco to current session PATH
    $chocoPath = "$env:ALLUSERSPROFILE\chocolatey\bin"
    $env:Path += ";$chocoPath"
    Write-Host "♻️ Added Chocolatey to PATH for this session."
} else {
    Write-Host "✅ Chocolatey is already installed."
}

# Step 2: Install / fix Python
Write-Host "🐍 Installing or fixing Python installation..."
choco install python --pre -y --force

# Step 3: Find real python.exe (skip WindowsApps)
Write-Host "🔍 Looking for real python.exe..."
$allPythons = Get-Command python.exe -All -ErrorAction SilentlyContinue
$python = $null

foreach ($p in $allPythons) {
    if ($p.Source -notlike "*WindowsApps*") {
        $python = $p.Source
        break
    }
}

# If still not found, try common install path
if ($null -eq $python) {
    $possiblePython = "C:\Python311\python.exe"
    if (Test-Path $possiblePython) {
        $python = $possiblePython
    } else {
        Write-Host "❌ Could not find real python.exe. Please check installation and PATH."
        exit 1
    }
}

Write-Host "📦 Running setup_dev_env.py with $python ..."
& $python setup_dev_env.py

Write-Host "🎉 All done!"
