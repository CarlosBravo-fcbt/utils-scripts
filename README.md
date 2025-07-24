# ⚙️ Dev Environment Bootstrap — *Install smarter, not harder*

[![PowerShell](https://img.shields.io/badge/PowerShell-%23177--blue?logo=powershell&logoColor=white)](https://docs.microsoft.com/powershell/)
[![Chocolatey](https://img.shields.io/badge/Chocolatey-%2348963F?logo=chocolatey&logoColor=white)](https://chocolatey.org/)
[![Python](https://img.shields.io/badge/Python-%233776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](#-license)

Why waste time downloading and clicking through installers by hand?  
With [**Chocolatey**](https://chocolatey.org/) you can automate your Windows dev environment safely, repeatably, and fast — using just one script. 🚀

This project helps you:
✅ Install Chocolatey (Windows package manager)  
✅ Install Python (if missing)  
✅ Install your favorite dev tools: **Git, Node.js LTS, nvm-windows, VSCode, Java JDK, Maven**

All automated — no browser downloads, no next-next-finish clicking.

---

## 🛠 What you get

| Tool        | Installed via                | Why                                      |
|------------:|-----------------------------:|-----------------------------------------:|
| Chocolatey  | PowerShell script            | Repeatable Windows package manager       |
| Python      | Chocolatey                   | Needed to run the automation script     |
| Node.js LTS | Chocolatey                   | Stable Node ready to go                 |
| nvm-windows | Chocolatey + script setup    | Easily manage multiple Node versions    |
| Git         | Chocolatey                   | Industry-standard VCS                    |
| VSCode      | Chocolatey                   | Popular, lightweight IDE                |
| Java JDK    | Chocolatey (`temurin`)       | Modern OpenJDK for Java projects        |
| Maven       | Chocolatey                   | Build tool for Java                      |

---

## 🚀 Quick start

> ✅ **Run as Administrator**:  
> Right-click → _Run with PowerShell_ or open an Admin terminal

```powershell
.\install_chocolatey_python.ps1
