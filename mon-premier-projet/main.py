#python
# main.py
import requests

def main():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("Connected to GitHub API successfully!")
    else:
        print("Failed to connect to GitHub API")

if __name__ == "__main__":
    main()

