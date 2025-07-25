Write-Host "🚀 Starting Dev Environment bootstrap..."

# Step 1: Install Chocolatey if missing
if (!(Get-Command choco.exe -ErrorAction SilentlyContinue)) {
    Write-Host "🔧 Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "✅ Chocolatey installed."

    # Add to PATH for current session
    $env:Path += ";$env:ALLUSERSPROFILE\chocolatey\bin"
} else {
    Write-Host "✅ Chocolatey is already installed."
}

# Step 2: Install packages in recommended order
$packages = @(
    @{ name = "nvm"; display = "NVM (Node Version Manager)" },
    @{ name = "nodejs-lts"; display = "Node.js LTS" },
    @{ name = "git"; display = "Git" },
    @{ name = "vscode"; display = "Visual Studio Code" },
    @{ name = "openjdk"; display = "Java JDK (OpenJDK)" },
    @{ name = "maven"; display = "Apache Maven" }
)

foreach ($pkg in $packages) {
    Write-Host "📦 Installing $($pkg.display)..."
    choco install $($pkg.name) -y --force
}

# Step 3: Install Visual Studio Enterprise with Node.js & Python workloads
Write-Host "📦 Installing Visual Studio 2022 Enterprise with Node.js and Python workloads..."
choco install visualstudio2022enterprise -y --force --package-parameters "--add Microsoft.VisualStudio.Workload.Node --add Microsoft.VisualStudio.Workload.Python"

# Step 4: Verify Node & NVM
$nvmPath = "C:\Program Files\nvm\nvm.exe"
if (Test-Path $nvmPath) {
    Write-Host "🔧 Using NVM to install latest Node LTS..."
    & $nvmPath install lts
    & $nvmPath use lts
    Write-Host "✅ Node version set with NVM."
} else {
    Write-Host "⚠ NVM not found; skipping Node version setup."
}

Write-Host "🎉 All done! Happy coding! 🚀"
