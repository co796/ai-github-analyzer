import requests

REPO = "octocat/Hello-World"

url = f"https://api.github.com/repos/{REPO}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Repository:", data["full_name"])
    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Language:", data["language"])
else:
    print("Error:", response.status_code)
