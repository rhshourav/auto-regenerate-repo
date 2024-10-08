import datetime

def generate_readme():
    content = f"# Auto Regenerate Repository\n\nThis README was last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    content += f"\n ![TryHackMe](https://tryhackme.com/badge/533634)"

    with open("README.md", "w") as readme_file:
        readme_file.write(content)

if __name__ == "__main__":
    generate_readme()
