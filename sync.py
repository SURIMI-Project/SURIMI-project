from github import Github
from pathlib import Path
import subprocess
import shutil
import os

ORG = "Official-EwE"
WIKI_REPO = "SURIMI-project"

token = os.environ["GITHUB_TOKEN"]

g = Github(token)


print("get all repo names")
org = g.get_organization("Official-EwE")

for repo in org.get_repos():
    print(repo.full_name)

print("printed all repo names")

repos = list(org.get_repos())
print(f"Visible repos: {len(repos)}")

wiki_dir = Path("wiki")

subprocess.run(
    [
        "git",
        "clone",
        f"https://x-access-token:{token}@github.com/{ORG}/{WIKI_REPO}.wiki.git",
        str(wiki_dir),
    ],
    check=True,
)

results = g.search_code(
    query=f"org:{ORG} filename:_architecture.md"
)

for result in results:

    print(f"Syncing {result.repository.name}/{result.path}")

    content = result.repository.get_contents(result.path)
    text = content.decoded_content.decode("utf-8")

    target = wiki_dir / result.name

    # Create or overwrite only this file
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)

subprocess.run(
    ["git", "-C", str(wiki_dir), "add", "*.md"],
    check=False
)

status = subprocess.run(
    ["git", "-C", str(wiki_dir), "status", "--porcelain"],
    capture_output=True,
    text=True,
)

if status.stdout.strip():

    subprocess.run(
        ["git", "-C", str(wiki_dir), "config", "user.name", "github-actions"],
        check=True,
    )

    subprocess.run(
        ["git", "-C", str(wiki_dir), "config", "user.email", "github-actions@github.com"],
        check=True,
    )

    subprocess.run(
        ["git", "-C", str(wiki_dir), "commit", "-m", "Sync architecture documents"],
        check=True,
    )

    subprocess.run(
        ["git", "-C", str(wiki_dir), "push"],
        check=True,
    )

    print("Wiki updated")
else:
    print("No changes")
