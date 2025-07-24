import os
import subprocess

# 🔧 Set your DevOps base URL here
BASE_URL = "https://fcbtdev@dev.azure.com/fcbtdev/FarmView/_git"

# 📦 List of repos
REPOS = [
    "farmview-gitops",
    "farmview-pipeline",
    "fcbt-react-component-library",
    "fvhome-auth",
    "fvhome-auth-loaniq-utils",
    "fvhome-breadcrumbs",
    "fvhome-calendar",
    "fvhome-cme",
    "fvhome-cme-api",
    "fvhome-crm",
    "fvhome-crm-api",
    "fvhome-daily-wire",
    "fvhome-dashboard",
    "fvhome-deal-team",
    "fvhome-entity-maintenance",
    "fvhome-favorites",
    "fvhome-floify",
    "fvhome-hub",
    "fvhome-las-api",  
    "fvhome-leads",
    "fvhome-loaniq-utils",
    "fvhome-loaninquiry",
    "fvhome-menu-ql",
    "fvhome-mywork",
    "fvhome-notifications",
    "fvhome-onbehalf",
    "fvhome-portfolio-management",
    "fvhome-regression-tests",
    "fvhome-risk-management",
    "fvhome-search",
    "fvhome-settings-api",
    "fvhome-shell",
]

def print_menu():
    print("\n📦 Available Repositories:")
    for idx, repo in enumerate(REPOS, start=1):
        print(f"{idx}. {repo}")
    print("\nType numbers separated by commas (e.g., 1,3,5) or type 'all' to clone all:")

def clone_repo(repo):
    if os.path.exists(repo):
        print(f"✅ {repo} already exists, skipping.")
        return
    url = f"{BASE_URL}/{repo}"
    print(f"🚀 Cloning {repo}...")
    try:
        subprocess.run(["git", "clone", url], check=True)
        print(f"✅ Successfully cloned {repo}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clone {repo}: {e}")

def main():
    print_menu()
    choice = input("\nYour choice: ").strip().lower()

    if choice == "all":
        selected = REPOS
    else:
        try:
            indices = [int(i.strip()) - 1 for i in choice.split(",")]
            selected = [REPOS[i] for i in indices if 0 <= i < len(REPOS)]
        except ValueError:
            print("⚠️ Invalid input. Exiting.")
            return

    if not selected:
        print("⚠️ No valid repositories selected. Exiting.")
        return

    print(f"\n🛠 Cloning {len(selected)} repositories...\n")
    for repo in selected:
        clone_repo(repo)

    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
