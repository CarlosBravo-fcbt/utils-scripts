# ⚙️ Dev Environment Bootstrap

[![PowerShell](https://img.shields.io/badge/PowerShell-%23177--blue?logo=powershell&logoColor=white)](https://docs.microsoft.com/powershell/)
[![Chocolatey](https://img.shields.io/badge/Chocolatey-%2348963F?logo=chocolatey&logoColor=white)](https://chocolatey.org/)
[![Python](https://img.shields.io/badge/Python-%233776AB?logo=python&logoColor=white)](https://www.python.org/)

Automate setting up your Windows dev machine with:
- **Chocolatey** (package manager)
- **Python**
- Popular dev tools: Git, Node.js (LTS), nvm-windows, VSCode, Java JDK, Maven

---

## 📦 Files

| File                                | Purpose                                                        |
|------------------------------------:|----------------------------------------------------------------|
| `install_chocolatey_python.ps1`     | PowerShell script to install Chocolatey & Python, then run Python script |
| `setup_dev_env.py`                  | Python script to install dev tools & print versions            |

---

## 🚀 How to use

> **Run as Administrator**  
> Right-click → _Run with PowerShell_ or open Admin terminal

```powershell
.\install_chocolatey_python.ps1
