import os
import subprocess
import sys
import json

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
    print("\n✅ Choose by number (e.g., 1,3,5), by name (e.g., fvhome-auth,fvhome-crm-api), or type 'all' to clone all:")

def prompt_with_default(message, default):
    user_input = input(f"{message} (default: '{default}'): ").strip()
    return user_input if user_input else default

def clone_repo(repo, target_dir):
    repo_path = os.path.join(target_dir, repo)
    if os.path.exists(repo_path):
        print(f"✅ {repo} already exists in '{target_dir}', skipping.")
        return
    url = f"{BASE_URL}/{repo}"
    print(f"🚀 Cloning {repo} into '{target_dir}'...")
    try:
        subprocess.run(["git", "clone", url, repo_path], check=True)
        print(f"✅ Successfully cloned {repo}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to clone {repo}: {e}")

def parse_choice(choice):
    choice = choice.strip().lower()
    if choice == "all":
        return REPOS

    parts = [part.strip() for part in choice.split(",")]
    selected = []

    for part in parts:
        if part.isdigit():
            idx = int(part) - 1
            if 0 <= idx < len(REPOS):
                selected.append(REPOS[idx])
        elif part in [repo.lower() for repo in REPOS]:
            matched_repo = next(repo for repo in REPOS if repo.lower() == part)
            selected.append(matched_repo)
        else:
            print(f"⚠️ Invalid selection ignored: '{part}'")

    return list(dict.fromkeys(selected))  # remove duplicates

def main():
    # Prompt for root folder name (default: current folder name)
    default_folder = os.path.basename(os.getcwd())
    root_folder = prompt_with_default("Enter root folder name to create", default_folder)

    print_menu()
    choice = input("\nYour choice: ")
    selected_repos = parse_choice(choice)

    if not selected_repos:
        print("⚠️ No valid repositories selected. Exiting.")
        return

    print(f"\n🛠 Will clone {len(selected_repos)} repositories into folder '{root_folder}'...")
    os.makedirs(root_folder, exist_ok=True)

    for repo in selected_repos:
        clone_repo(repo, root_folder)

    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
