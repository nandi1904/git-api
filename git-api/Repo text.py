import requests
from pprint import pprint
username = "nandi1904"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)

from linguist import Repository
repo = Repository.from_directory("https://api.github.com/users/{username}")
 languages = repo.languages
for language, percentage in languages.items():
print(f"{language}: {percentage}%")



